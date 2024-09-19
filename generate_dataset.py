import json
import logging
import os
import shutil
from concurrent.futures import ProcessPoolExecutor, as_completed
from concurrent.futures.process import BrokenProcessPool
from multiprocessing import Lock, Manager

import gemmi
import mrcfile
import numpy as np
import splitfolders
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

from atom_in_models import residues_protein
from helper_funcs import calculate_title_padding, read_csv_info


def data_to_npy(normalized_map_path: str,
                model_path: str,
                label_group: list,
                temp_sample_path: str,
                group_names: list,
                sample_num = 0,
                lock = None,
                npy_size: int = 64,
                generate_test: bool = False,
                classes: int = 24):
    """
    Converts map and model data to numpy arrays and labels them.

    Parameters:
    - normalized_map_path: Path to the MRC map file.
    - model_path: Path to the PDB model file.
    - label_group: List of label groups.
    - temp_sample_path: Directory to save the samples.
    - group_names: List of group names.
    - sample_num: Counter for the number of samples (default is 0).
    - lock: Lock for multiprocessing (default is None).
    - npy_size: Size of the numpy arrays (default is 64).
    - generate_test: Flag to generate test maps (default is False).
    - classes: Number of classes for labeling (default is 24).

    Functionality:
    1. Initializes lists to store map data and labels.
    2. Reads the MRC map file and adjusts the coordinate order to [z, y, x].
    3. Reads the PDB model file and ensures the model size does not exceed the map size.
    4. Computes grid parameters for splitting the volume.
    5. Creates labels for the data based on the provided label groups.
    6. Generates test maps if the generate_test flag is set to True.
    7. Appends the map data to the data list and 'map_sample' to the labels list.
    8. Uses a lock to split the data into numpy arrays and save them.
    9. Returns the number of labels.
    """
    # Save map data and labeled data
    data = []
    labels = []

    try:
        # Read the MRC map file and change the coordinates order to [z, y, x]
        map_data, map_size = check_mrc_coordinates_order(normalized_map_path)

        # Read the PDB model file
        structure = gemmi.read_structure(model_path)
    except FileNotFoundError:
        raise BrokenProcessPool('Normailzed Map or Model File not Found')
    except ValueError:
        raise BrokenProcessPool('Broken MRC Map or Model File')

    # Ensure the size of the model is not larger than the map
    box = structure.calculate_box()
    # box coord is [x, y, z] so change the order to [z, y, x]
    box_min = list(box.minimum)[::-1]
    box_max = list(box.maximum)[::-1]
    if box_max[2] > map_size[2] or box_max[1] > map_size[2] or box_max[
        0] > map_size[0]:
        raise ValueError("The model box size exceeds that of the map.")

    # Compute the grid parameters for splitting the volume
    start_coords, n_samples = compute_grid_params(box_min, box_max, map_size,
                                                  npy_size)
                                                  
    # Creating labels
    helices, sheets = protein_2nd_structure_lists(structure)
    for member_idx, member in enumerate(label_group):
        # initialize datastruct for every member
        member_data = np.zeros(map_size, np.int8)  
        dis_array = np.array([])
        label_coords = None

        for label in member:
            secondary_type, residue_type, atom_type, element_type, metal_type, tag = label['secondary_type'].split(','), \
                label['residue_type'].split(','), label['atom_type'].split(','), label['element_type'].split(','),\
                    label['metal_type'].split(','), label['label']
            
            if residue_type == ['']:
                residue_type = None
            if atom_type == ['']:
                atom_type = None
            if element_type == ['']:
                element_type = None
            if metal_type == ['']:
                metal_type = None

            if secondary_type == ['']:
                if atom_type is None and element_type is None and metal_type is None or\
                    atom_type is not None:
                    label_coords = atom_coord_cif(structure, residue_type, atom_type)
                    member_data, dis_array = label_npy(member_data, label_coords, tag, dis_array)
                if element_type is not None:
                    label_coords = element_coord_cif(structure, residue_type, element_type)
                    member_data, dis_array = label_npy(member_data, label_coords, tag, dis_array)
                if metal_type is not None:
                    for metal in metal_type:
                        label_coords = element_coord_cif(structure, residue_type, metal)
                        member_data, dis_array = label_npy(member_data, label_coords, tag, dis_array, gemmi.Element(metal).vdw_r)
            else:
                if atom_type is None and element_type is None or atom_type is not None:             
                    protein_2nd_structure_coords = atom_coord_cif_protein_secondary(
                            structure, helices, sheets, residue_type, atom_type)
                    if 'Helix' in secondary_type:
                        member_data, dis_array = label_npy(member_data, protein_2nd_structure_coords[0], tag, dis_array)
                    if 'Sheet' in secondary_type:
                        member_data, dis_array = label_npy(member_data, protein_2nd_structure_coords[1], tag, dis_array)
                    if 'Loop' in secondary_type:
                        member_data, dis_array = label_npy(member_data, protein_2nd_structure_coords[2], tag, dis_array)
                if element_type is not None:  
                    protein_2nd_structure_coords = element_coord_cif_protein_secondary(
                        structure, helices, sheets, residue_type, element_type)
                    if 'Helix' in secondary_type:
                        member_data, dis_array = label_npy(member_data, protein_2nd_structure_coords[0], tag, dis_array)
                    if 'Sheet' in secondary_type:
                        member_data, dis_array = label_npy(member_data, protein_2nd_structure_coords[1], tag, dis_array)
                    if 'Loop' in secondary_type:
                        member_data, dis_array = label_npy(member_data, protein_2nd_structure_coords[2], tag, dis_array)
        data.append(member_data)
        labels.append(group_names[member_idx])

        if generate_test is True:
            for label in range(1, classes + 1):
                out_map = f"{normalized_map_path.split('.mrc')[0]}_EXAMPLE_{label}.mrc"
                print("=> Writing new map")
                shutil.copy(normalized_map_path, out_map)
                with mrcfile.open(out_map, mode='r+') as mrc:
                    TEST_data = np.zeros_like(member_data)
                    TEST_data = np.where(member_data == label, member_data, 0)
                    mrc.set_data(TEST_data)
                print("New map is writen.")
                continue
            
            '''out_map = f"{normalized_map_path.split('.mrc')[0]}_EXAMPLE_{label}.mrc"
            print("=> Writing new map")
            shutil.copy(normalized_map_path, out_map)
            with mrcfile.open(out_map, mode='r+') as mrc:
                TEST_data = member_data
                mrc.set_data(TEST_data)
                mrc.header.mz = member_data.shape[0]
            print("New map is writen.")

                #logger.info('Successfully generated test mrc(s).')
            #except Exception as e:
                #logger.error(f'Generation failed. Exception: {e}.')'''
            exit()

    data.append(map_data)
    labels.append('map_sample')

    with lock:
        num_labels = split_to_npy(data, temp_sample_path, start_coords,
                                        n_samples, npy_size, sample_num,
                                        labels)

    return num_labels



def check_mrc_coordinates_order(mrc_path):
    """
    Checks and corrects the coordinate order of an MRC file to "z, y, x".

    Parameters:
    - mrc_path: Path to the MRC file.

    Functionality:
    1. Opens the MRC file and reads the header information.
    2. Extracts the map size and data from the MRC file.
    3. Checks the coordinate order (mapc, mapr, maps) in the header.
    4. If the coordinate order is not "z, y, x", swaps the axes accordingly.
    5. Returns the corrected map data and map size.
    """
    with mrcfile.open(mrc_path, permissive=True) as mrc:
        map_size = [int(mrc.header.nz), int(mrc.header.ny), int(mrc.header.nx)]
        map_data = np.array(mrc.data)
        maps, mapr, mapc = mrc.header.maps, mrc.header.mapr, mrc.header.mapc
        if not (mapc == 1 and mapr == 2 and maps == 3):
            #print('Swap the mrc coordinates to "z, y, x"')
            if mapc == 1 and mapr == 3 and maps == 2:
                map_data = map_data.swapaxes(1, 2)
            elif mapc == 2 and mapr == 1 and maps == 3:
                map_data = map_data.swapaxes(0, 1)
            elif mapc == 2 and mapr == 3 and maps == 1:
                map_data = map_data.swapaxes(1, 2)
                map_data = map_data.swapaxes(0, 1)
            elif mapc == 3 and mapr == 1 and maps == 2:
                map_data = map_data.swapaxes(0, 1)
                map_data = map_data.swapaxes(1, 2)
            elif mapc == 3 and mapr == 2 and maps == 1:
                map_data = map_data.swapaxes(0, 2)
            else:
                raise ValueError('Error When Reading Mrc File')

    return map_data, map_size


def compute_grid_params(box_min_list, box_max_list, axis_length_list,
                        grid_size):
    """
    Computes the starting coordinates and number of samples for grid extraction.

    Parameters:
    - box_min_list: List of minimum coordinates for each axis.
    - box_max_list: List of maximum coordinates for each axis.
    - axis_length_list: List of lengths for each axis.
    - grid_size: Size of the grid for extraction.

    Functionality:
    1. Initializes lists to store starting coordinates and number of samples.
    2. Iterates through the provided lists to calculate the midpoint of each box.
    3. Calculates the number of samples along each axis.
    4. Adjusts the number of samples if the midpoint is not within the valid range.
    5. Computes the starting coordinates for each axis.
    6. Returns the starting coordinates and number of samples.
    """
    start_coords = []
    n_samples = []
    for box_min, box_max, axis_length in zip(box_min_list, box_max_list,
                                             axis_length_list):
        box_mid = (box_min + box_max) // 2

        # num of samples along one axis
        n_samples_axis = (box_max - box_min) // grid_size + 1

        if not (32 * n_samples_axis <= box_mid <
                axis_length - 32 * n_samples_axis):
            n_samples_axis -= 1
        start_coord = box_mid - 32 * n_samples_axis
        start_coords.append(int(start_coord))
        n_samples.append(int(n_samples_axis))
    return start_coords, n_samples



def split_to_npy(data,
                 temp_sample_path,
                 start_coords,
                 n_samples,
                 npy_size,
                 sample_num,
                 labels,
                 extract_stride=32):
    """
    Splits 3D data into smaller numpy arrays and saves them as .npy files.

    Parameters:
    - data: List of 3D numpy arrays to be split.
    - temp_sample_path: Directory to save the .npy files.
    - start_coords: Starting coordinates for splitting.
    - n_samples: Number of samples to generate in each dimension.
    - npy_size: Size of each .npy file.
    - sample_num: Shared counter for the number of samples.
    - labels: List of labels for the data.
    - extract_stride: Stride for extracting samples (default is 32).

    Functionality:
    1. Initializes a list to store the number of labels.
    2. Adjusts the number of samples based on the npy_size and extract_stride.
    3. Creates directories for each label if they do not exist.
    4. Iterates through the data to extract and save samples as .npy files.
    5. Updates the count of labels in each sample.
    6. Saves separated files for map data.
    7. Increments the sample counter.
    8. Returns the list of the number of labels.
    """
    num_labels = [0] * len(data)
    sample_start_z, sample_start_y, sample_start_x = start_coords
    for i in range(3):
        n_samples[i] = int(n_samples[i] * npy_size / extract_stride) - 1
    for label in labels:
        os.makedirs(os.path.join(temp_sample_path, label), exist_ok=True)
    for n_z in range(n_samples[0]):
        idx_z = sample_start_z + extract_stride * n_z
        for n_y in range(n_samples[1]):
            idx_y = sample_start_y + extract_stride * n_y
            for n_x in range(n_samples[2]):
                idx_x = sample_start_x + extract_stride * n_x
                for idx in range(0, len(data) - 1):
                    sample = data[idx][idx_z:idx_z + npy_size,
                             idx_y:idx_y + npy_size,
                             idx_x:idx_x + npy_size]
                    file_name = os.path.join(
                        temp_sample_path, labels[idx],
                        f"model_{labels[idx]}.{sample_num.value}.npy")
                    np.save(file_name, sample)

                    count = np.bincount(sample.flatten())
                    count = np.pad(count, (0, max(0, 27 - len(count))),
                                   'constant')
                    num_labels[idx] += count

                # Save separated files for map data
                sample = data[len(data) - 1][idx_z:idx_z + npy_size,
                         idx_y:idx_y + npy_size,
                         idx_x:idx_x + npy_size]
                file_name = os.path.join(temp_sample_path, labels[len(data) - 1],
                                         f"map.{sample_num.value}.npy")
                np.save(file_name, sample)

                sample_num.value += 1

    return num_labels



def label_npy(member_data,
            label_coords,
            label_id,
            dis_array=np.array([]),
            atom_grid_radius=1.5):
    """
    Labels a 3D numpy array with specified coordinates and label ID.

    Parameters:
    - member_data: 3D numpy array to be labeled.
    - label_coords: List of coordinates to be labeled.
    - label_id: ID to label the coordinates with.
    - dis_array: Optional distance array for distance calculations (default is an empty array).
    - atom_grid_radius: Radius for labeling grid (default is 1.5).

    Functionality:
    1. Initializes the distance array if not provided.
    2. Calculates the index grid and creates a range for extensions.
    3. Generates a list of surrounding coordinates within the atom grid radius.
    4. Iterates through the label coordinates and calculates the floor coordinates.
    5. Labels the member_data array with the label_id for coordinates within the atom grid radius.
    6. Updates the distance array with the calculated distances.
    7. Returns the labeled member_data array and the updated distance array.
    """
    if dis_array.size == 0:
        dis_array = np.full(member_data.shape, atom_grid_radius ** 2)

    index_grid = int(atom_grid_radius) + 1
    extension = range(-index_grid, index_grid + 1)
    arounds = []
    for dz in extension:
        for dy in extension:
            for dx in extension:
                dist = dz ** 2 + dy ** 2 + dx ** 2
                if dist <= atom_grid_radius ** 2:
                    arounds.append([dz, dy, dx])
    arounds = np.array(arounds)
    arounds = np.vstack((arounds, arounds + np.array([0, 0, 1])))
    arounds = np.vstack((arounds, arounds + np.array([0, 1, 0])))
    arounds = np.vstack((arounds, arounds + np.array([1, 0, 0])))
    arounds = np.unique(arounds, axis=0).astype(int)

    for coord in np.array(label_coords):
        floor_coord = np.floor(coord).astype(int)
        for around in arounds:
            around_coord = floor_coord + around
            dist = np.sum((around_coord - coord) ** 2)
            if dist <= dis_array[around_coord[0], around_coord[1],
            around_coord[2]]:
                member_data[around_coord[0], around_coord[1],
                around_coord[2]] = label_id
                dis_array[around_coord[0], around_coord[1],
                around_coord[2]] = dist

    return member_data, dis_array



def atom_coord_cif(structure, RESIDUE=None, ATOM=None):
    """
    Extracts coordinates of specified atoms from a protein structure.

    Parameters:
    - structure: The protein structure.
    - RESIDUE: Optional list of residue names to filter (default is None).
    - ATOM: Optional list of atom names to filter (default is None).

    Functionality:
    1. Initializes a list to store coordinates.
    2. Iterates through the structure to extract coordinates for specified residues and atoms.
    3. Filters residues and atoms based on RESIDUE and ATOM if provided.
    4. Appends the coordinates of the atoms to the list.
    5. Returns the list of coordinates.
    """
    coords = []
    for model in structure:
        for chain in model:
            for residue in chain:
                if RESIDUE is not None and residue.name not in RESIDUE:
                    continue
                for atom in residue:
                    if ATOM is not None and atom.name not in ATOM:
                        continue
                    coords.append([atom.pos.z, atom.pos.y, atom.pos.x])
    return coords


def element_coord_cif(structure, RESIDUE=None, ATOM=None):
    """
    Extracts coordinates of specified elements from a protein structure.

    Parameters:
    - structure: The protein structure.
    - RESIDUE: Optional list of residue names to filter (default is None).
    - ATOM: Optional list of atom elements to filter (default is None).

    Functionality:
    1. Initializes a list to store coordinates.
    2. Iterates through the structure to extract coordinates for specified residues and elements.
    3. Filters residues and elements based on RESIDUE and ATOM if provided.
    4. Appends the coordinates of the elements to the list.
    5. Returns the list of coordinates.
    """
    coords = []
    for model in structure:
        for chain in model:
            for residue in chain:
                if RESIDUE is not None and residue.name not in RESIDUE:
                    continue
                for atom in residue:
                    if ATOM is not None and atom.element.name not in ATOM:
                        continue
                    coords.append([atom.pos.z, atom.pos.y, atom.pos.x])
    return coords


def protein_2nd_structure_lists(structure):
    """
    Extracts lists of helices and sheets from a protein structure.

    Parameters:
    - structure: The protein structure.

    Functionality:
    1. Initializes lists to store helices and sheets information.
    2. Iterates through the helices in the structure and extracts the start and end residue sequence IDs and chain names. Appends this information to the helices list.
    3. Iterates through the sheets in the structure and extracts the start and end residue sequence IDs and chain names for each strand. Appends this information to the sheets list.
    4. Returns the lists of helices and sheets.
    """
    helices, sheets, = [], []

    for helix_index in range(len(structure.helices)):
        start = structure.helices[helix_index].start.res_id.seqid.num
        end = structure.helices[helix_index].end.res_id.seqid.num
        chain_name = structure.helices[helix_index].start.chain_name
        helices.append([chain_name, start, end])

    for sheet_index in range(len(structure.sheets)):
        for strand_index in range(len(structure.sheets[sheet_index].strands)):
            start = structure.sheets[sheet_index].strands[
                strand_index].start.res_id.seqid.num
            end = structure.sheets[sheet_index].strands[
                strand_index].end.res_id.seqid.num
            chain_name = structure.sheets[sheet_index].strands[
                strand_index].start.chain_name
            sheets.append([chain_name, start, end])

    return helices, sheets


def atom_coord_cif_protein_secondary(structure,
                                     helices,
                                     sheets,
                                     RESIDUE=None,
                                     ATOM=None):
    """
    Extracts coordinates of atoms in helices, sheets, and loops from a protein structure.

    Parameters:
    - structure: The protein structure.
    - helices: List of helices information.
    - sheets: List of sheets information.
    - RESIDUE: Optional list of residue names to filter (default is None).
    - ATOM: Optional list of atom names to filter (default is None).

    Functionality:
    1. Initializes lists to store coordinates for helices, sheets, and loops.
    2. Extracts chain names for helices and sheets.
    3. Calls atom_coord_cif to get coordinates of all residues if RESIDUE is None.
    4. Iterates through the structure to extract coordinates for helices and sheets based on the provided information.
    5. Filters residues and atoms based on RESIDUE and ATOM if provided.
    6. Collects coordinates for helices and sheets.
    7. Identifies coordinates for loops by excluding helices and sheets coordinates from the overall coordinates.
    8. Returns a list containing coordinates for helices, sheets, and loops.
    """
    coords, coords_helices, coords_sheets = [], [], []
    chain_helices = [row[0] for row in helices]
    chain_sheets = [row[0] for row in sheets]

    if RESIDUE is None:
        coords = atom_coord_cif(structure, residues_protein, ATOM)
    else:
        coords = atom_coord_cif(structure, RESIDUE, ATOM)

    for model in structure:
        for chain in model:
            # helices
            for index, helix_chian_name in enumerate(chain_helices):
                if chain.name != helix_chian_name:
                    continue
                chain_info = helices[index]
                for residue in chain:
                    if residue.seqid.num in range(chain_info[1], chain_info[2] + 1):
                            if RESIDUE is not None and residue.name not in RESIDUE:
                                continue
                            for atom in residue:
                                if ATOM is not None and atom.name not in ATOM:
                                    continue
                                atom_coord = [atom.pos.z, atom.pos.y, atom.pos.x]
                                coords_helices.append(atom_coord)
            # sheets
            for index, sheet_chian_name in enumerate(chain_sheets):
                if chain.name != sheet_chian_name:
                    continue
                chain_info = sheets[index]
                for residue in chain:
                    if residue.seqid.num in range(chain_info[1], chain_info[2] + 1):
                            if RESIDUE is not None and residue.name not in RESIDUE:
                                continue
                            for atom in residue:
                                if ATOM is not None and atom.name not in ATOM:
                                    continue
                                atom_coord = [atom.pos.z, atom.pos.y, atom.pos.x]
                                coords_sheets.append(atom_coord)
    coords_loops = [
        x for x in coords if not (x in coords_sheets or x in coords_helices)
    ]
    return [coords_helices, coords_sheets, coords_loops]


def element_coord_cif_protein_secondary(structure,
                                     helices,
                                     sheets,
                                     RESIDUE=None,
                                     ATOM=None):
    """
    Extracts coordinates of atoms in helices, sheets, and loops from a protein structure.

    Parameters:
    - structure: The protein structure.
    - helices: List of helices information.
    - sheets: List of sheets information.
    - RESIDUE: Optional list of residue names to filter (default is None).
    - ATOM: Optional list of atom names to filter (default is None).

    Functionality:
    1. Initializes lists to store coordinates for helices, sheets, and loops.
    2. Extracts chain names for helices and sheets.
    3. Calls element_coord_cif to get coordinates of all residues if RESIDUE is None.
    4. Iterates through the structure to extract coordinates for helices and sheets based on the provided information.
    5. Filters residues and atoms based on RESIDUE and ATOM if provided.
    6. Collects coordinates for helices and sheets.
    7. Identifies coordinates for loops by excluding helices and sheets coordinates from the overall coordinates.
    8. Returns a list containing coordinates for helices, sheets, and loops.
    """
    coords, coords_helices, coords_sheets = [], [], []
    chain_helices = [row[0] for row in helices]
    chain_sheets = [row[0] for row in sheets]

    if RESIDUE is None:
        coords = element_coord_cif(structure, residues_protein, ATOM)
    else:
        coords = element_coord_cif(structure, RESIDUE, ATOM)

    for model in structure:
        for chain in model:
            # helices
            for index, helix_chian_name in enumerate(chain_helices):
                if chain.name != helix_chian_name:
                    continue
                chain_info = helices[index]
                for residue in chain:
                    if residue.seqid.num in range(chain_info[1], chain_info[2] + 1):
                            if RESIDUE is not None and residue.name not in RESIDUE:
                                continue
                            for atom in residue:
                                if ATOM is not None and atom.element.name not in ATOM:
                                    continue
                                atom_coord = [atom.pos.z, atom.pos.y, atom.pos.x]
                                coords_helices.append(atom_coord)
            # sheets
            for index, sheet_chian_name in enumerate(chain_sheets):
                if chain.name != sheet_chian_name:
                    continue
                chain_info = sheets[index]
                for residue in chain:
                    if residue.seqid.num in range(chain_info[1], chain_info[2] + 1):
                            if RESIDUE is not None and residue.name not in RESIDUE:
                                continue
                            for atom in residue:
                                if ATOM is not None and atom.element.name not in ATOM:
                                    continue
                                atom_coord = [atom.pos.z, atom.pos.y, atom.pos.x]
                                coords_sheets.append(atom_coord)
    coords_loops = [
        x for x in coords if not (x in coords_sheets or x in coords_helices)
    ]
    return [coords_helices, coords_sheets, coords_loops]


def split_folders(temp_sample_path, sample_path, ratio_t_t_v=(.8, .1, .1)):
    """
    Splits the dataset into training, testing, and validation sets.

    Parameters:
    - temp_sample_path: Path for temporary samples.
    - sample_path: Path for final samples.
    - ratio_t_t_v: Tuple representing the ratio for splitting the dataset into training, testing, and validation sets (default is (0.8, 0.1, 0.1)).

    Functionality:
    1. Checks if the sample_path exists and deletes it if it does.
    2. Creates the sample_path directory.
    3. Uses the splitfolders library to split the dataset from temp_sample_path to sample_path based on the provided ratio.
    4. Deletes the temporary sample path after splitting.
    """
    if os.path.exists(sample_path):
        # Delete the directory
        shutil.rmtree(sample_path)
    # Create the directory again
    os.makedirs(sample_path)
    splitfolders.ratio(input=temp_sample_path,
                       output=sample_path,
                       seed=44,
                       ratio=ratio_t_t_v,  # we set the ratio / let users do it
                       group_prefix=None,
                       move=True)
    shutil.rmtree(temp_sample_path)


def label_maps(label_group,
               metadata_path,
               raw_path,
               group_names,
               temp_sample_path = 'Temp_Sample',
               sample_path = 'Training',
               ratio_t_t_v = (.8, .1, .1)):
    """
    Generates and manages datasets for training models.

    Parameters:
    - label_group: List of label groups.
    - map_paths: Paths to the map files.
    - model_paths: Paths to the model files.
    - emdb_ids: List of EMDB IDs.
    - training_set_name: Name of the file for logging.
    - group_names: Names of the groups.
    - temp_sample_path: Path for temporary samples (default is './temp_sample').
    - sample_path: Path for final samples (default is './Training').
    - ratio_t_t_v: Tuple representing the ratio for splitting the dataset into training, testing, and validation sets (default is (0.8, 0.1, 0.1)).

    Functionality:
    1. Configures a logger to log the process of dataset generation.
    2. Logs the label groups and their respective labels.
    3. Initiates the process of generating the dataset and logs the start of the process.
    4. Uses a ProcessPoolExecutor to parallelize the generation of label files from the provided map and model paths. Logs the progress and results.
    5. Splits the generated data into training, testing, and validation sets based on the provided ratio.
    6. Logs statistical results, including the number of labels in each group and the total dataset size.
    7. Calculates the weight of each label group and saves it to a file.
    8. Logs the completion of the dataset generation process and moves the log file to the final sample path.
    """
    try:
        assert(len(label_group)==len(group_names))
    except AssertionError:
        raise ValueError('!!! The number of label groups and group names should be the same !!!')
    
    # read csv
    csv_info, path_info = read_csv_info(metadata_path, raw_path)
    _, _, _, emdb_ids = csv_info
    _, model_paths, normalized_map_paths = path_info
    training_set_name = metadata_path.split('/')[-1].split('.')[0]

    # configure logger
    logger = logging.getLogger('Dataset_Generation_Logger')
    logger.setLevel(logging.DEBUG)
    std_out_hdlr = logging.StreamHandler()
    std_out_hdlr.setLevel(logging.INFO)
    log_file_path = training_set_name+'_generate_dataset.log'
    file_hdlr = logging.FileHandler(log_file_path)
    file_hdlr.setLevel(logging.DEBUG)
    file_hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'))
    logger.addHandler(std_out_hdlr)
    logger.addHandler(file_hdlr)

    title = '-'*50+'Generating dataset'+'-'*50
    logger.info(title)
    msg = 'Label Groups:\n'
    for idx, name in enumerate(group_names):
        msg += f'    Group {name}:\n'
        for label in label_group[idx]:
            msg += f'       Label: {label}\n'
    logger.debug(msg)

    # num of label in each group for all models
    num_of_label_in_each_group_for_all_models = [0 for _ in range(len(label_group))]
    
    
    logger.info('Start Generating Label Files from Maps and Models')
    with Manager() as manager:
        sample_num_shared = manager.Value('i', 0)
        lock = manager.Lock()
        futures = []
        try:
            with ProcessPoolExecutor() as executor:
                futures = [executor.submit(data_to_npy, normalized_map_paths[idx], model_paths[idx], label_group,
                        temp_sample_path, group_names, sample_num_shared, lock) for idx in range(len(emdb_ids))]
                
                # Process the results as they complete
                with logging_redirect_tqdm([logger]):
                    i = 0
                    for future in tqdm(as_completed(futures), total=len(futures), desc='Labeling Maps'):
                        logger.info(f'Start Generating Label Files from EMDB-{emdb_ids[i]}')
                        num_labels = future.result()
                        num_of_label_in_each_group_for_all_models = [num_of_label_in_each_group_for_all_models[idx]+num_labels[idx]\
                                                                for idx in range(len(label_group))]
                        i += 1
        except BrokenProcessPool as e:
            logger.error(f'Error Generating Label Files: {e}')
            logger.error('!!! Please Check the Input Map/Model Paths and Try Again !!!')
            logger.error(calculate_title_padding(title, 'Dataset Generation Failed'))
            return
        sample_num = sample_num_shared.value
    logger.info('Successfully Generated All Label Files')

    # 3.3 Split data into training and validation dataset
    sample_path = os.path.join(sample_path,training_set_name)
    logger.info('')
    logger.info('Start Splitting Data into Training, Testing, and Validation Sets')
    try:
        split_folders(temp_sample_path, sample_path, ratio_t_t_v)
        logger.info('Successfully Splitted Data')
    except Exception as e:
        logger.error(f'Splitting Failed. Error: {e}')

    # Stats
    msg = 'Statistical results:\n'
    msg += f"Dataset Size (Number of .npy Files): {sample_num}\n"
    #trim_array = lambda arr: np.trim_zeros(arr[1:], 'b')
    num_of_label_in_each_group_for_all_models = [np.trim_zeros(sub_array, 'b') \
                                                 for sub_array in num_of_label_in_each_group_for_all_models]
    msg += "Number of Labels in Each Group:\n"
    ratio_of_label = {key: [] for key in group_names}
    for group_idx in range(len(label_group)):
        group_name = group_names[group_idx]
        msg += f'    Group {group_name}:\n'
        sum_label_per_group = 0
        member = num_of_label_in_each_group_for_all_models[group_idx]
        if len(member) != 0:
            for label in range(len(member)):
                label_num = member[label]
                msg += f'        Label-{label}: {label_num}\n'
                sum_label_per_group += label_num
                ratio_of_label[group_name].append(int(member[0]//label_num))
                if label == len(member)-1:
                    msg += f'        Total: {sum_label_per_group}\n'
        else:
            msg += '     The group is empty.\n'
            continue
    print('\n'+msg)
    stats_path = os.path.join(sample_path, 'statistics.txt')
    with open(stats_path, "w") as file:
        file.write(msg)
    logger.info(f'Statistics Results Written into "{stats_path}"')

    # 3.4 Calculate weight, create weight file and save it (ratio of labels)
    weight_path = os.path.join(sample_path, 'class_weight_for_training.txt')
    with open(weight_path, "w") as file:
        json.dump(ratio_of_label, file)
    logger.info(f'Weights Written into "{weight_path}"')
    
    logger.info(calculate_title_padding(title,'Dataset generation completed'))
    shutil.move('./'+training_set_name+'_generate_dataset.log',\
                sample_path+'/'+training_set_name+'_generate_dataset.log')


if __name__ == "__main__":
    '''
    # For Running Dataset Generation
    metadata_path = 'path_to_metadata_file'
    group_names = ['foo']
    label_group = [[{'secondary_type': '', 'residue_type': ','.join(residues_protein), 'atom_type': 'N', 'element_type': '', 'metal_type': '', 'label': 1},\
                   {'secondary_type': '', 'residue_type': ','.join(residues_protein), 'atom_type': 'C', 'element_type': '', 'metal_type': '', 'label': 2},\
                   {'secondary_type': '', 'residue_type': ','.join(residues_protein), 'atom_type': 'CA', 'element_type': '', 'metal_type': '', 'label': 3}]]
    label_maps(label_group=label_group,
               metadata_path=metadata_path,
               raw_path='Raw',
               group_names=group_names)
    '''

    # for testing data_to_npy()
    # not for running dataset generation
    normalized_map_path = r'path_to_save_downloaded_map_and_model/EMD-3145_re_3.3/emd_3145_normalized.mrc'
    model_path = r'path_to_save_downloaded_map_and_model/EMD-3145_re_3.3/5an9.cif'
    #normalized_map_path = r'path_to_save_downloaded_map_and_model/EMD-41587_re_2.92/emd_41587_normalized.mrc'
    #odel_path = r'path_to_save_downloaded_map_and_model/EMD-41587_re_2.92/8ts1.cif'
    # different label_group
    '''label_group = [[{'secondary_type': 'Helix', 'residue_type': '', 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 1},\
                   {'secondary_type': 'Sheet', 'residue_type': '', 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 2},\
                   {'secondary_type': 'Loop', 'residue_type': '', 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 3}]]'''
    '''label_group = [[{'secondary_type': '', 'residue_type': residues_protein[0], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 1},\
                    {'secondary_type': '', 'residue_type': residues_protein[1], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 2},\
                    {'secondary_type': '', 'residue_type': residues_protein[2], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 3},\
                    {'secondary_type': '', 'residue_type': residues_protein[3], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 4},\
                    {'secondary_type': '', 'residue_type': residues_protein[4], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 5},\
                    {'secondary_type': '', 'residue_type': residues_protein[5], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 6},\
                    {'secondary_type': '', 'residue_type': residues_protein[6], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 7},\
                    {'secondary_type': '', 'residue_type': residues_protein[7], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 8},\
                    {'secondary_type': '', 'residue_type': residues_protein[8], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 9},\
                    {'secondary_type': '', 'residue_type': residues_protein[9], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 10},\
                    {'secondary_type': '', 'residue_type': residues_protein[10], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 11},\
                    {'secondary_type': '', 'residue_type': residues_protein[11], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 12},\
                    {'secondary_type': '', 'residue_type': residues_protein[12], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 13},\
                    {'secondary_type': '', 'residue_type': residues_protein[13], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 14},\
                    {'secondary_type': '', 'residue_type': residues_protein[14], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 15},\
                    {'secondary_type': '', 'residue_type': residues_protein[15], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 16},\
                    {'secondary_type': '', 'residue_type': residues_protein[16], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 17},\
                    {'secondary_type': '', 'residue_type': residues_protein[17], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 18},\
                    {'secondary_type': '', 'residue_type': residues_protein[18], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 19},\
                    {'secondary_type': '', 'residue_type': residues_protein[19], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 20},\
                    ]]'''
    '''label_group = [[{'secondary_type': '', 'residue_type': ','.join(residues_protein), 'atom_type': 'CA', 'element_type': '', 'metal_type': '', 'label': 1},\
                   {'secondary_type': '', 'residue_type': ','.join(residues_protein), 'atom_type': '', 'element_type': 'N', 'metal_type': '', 'label': 2},\
                   {'secondary_type': '', 'residue_type': ','.join(residues_protein), 'atom_type': '', 'element_type': 'O', 'metal_type': '', 'label': 3}]]'''
    '''label_group = [[{'secondary_type': '', 'residue_type': 'A', 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 1},\
                   {'secondary_type': '', 'residue_type': 'U', 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 2},\
                   {'secondary_type': '', 'residue_type': 'C', 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 3},\
                   {'secondary_type': '', 'residue_type': 'G', 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 4}]]'''
    label_group = [[{'secondary_type': '', 'residue_type': ','.join(residues_protein), 'atom_type': 'CA', 'element_type': '', 'metal_type': '', 'label': 1},\
                    {'secondary_type': '', 'residue_type': ','.join(residues_protein), 'atom_type': 'N', 'element_type': '', 'metal_type': '', 'label': 2},\
                    {'secondary_type': '', 'residue_type': ','.join(residues_protein), 'atom_type': 'O', 'element_type': '', 'metal_type': '', 'label': 3}]]
    temp_sample_path = 'Temp_Sample'
    group_names = ['foo']

    data_to_npy(normalized_map_path, model_path, label_group, temp_sample_path,
                group_names, generate_test=True, classes=24)

