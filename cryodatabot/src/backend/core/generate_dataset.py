import atexit
import json
import logging
import os
import shutil
from concurrent.futures import (BrokenExecutor, ProcessPoolExecutor,
                                as_completed)
from concurrent.futures.process import BrokenProcessPool
from configparser import ConfigParser

import gemmi
import mrcfile
import numpy as np
import splitfolders
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from cryodatabot.src.backend.helper.atom_in_models import residues_protein
from cryodatabot.src.backend.helper.helper_funcs import calculate_title_padding, move_log_file, read_csv_info


def data_to_npy(label_groups: list,
                group_names: list,
                normalized_map_path: str,
                model_path: str,
                temp_sample_path: str,
                emdb_id: str,
                npy_size: int = 64,
                extract_stride: int = 32,
                atom_grid_radius: float = 1.5,
                generate_test: bool = False
                ):
    """
    Converts map and model data to numpy arrays and labels them.

    Parameters:
    - normalized_map_path: Path to the MRC map file.
    - model_path: Path to the PDB model file.
    - label_groups: List of label groups.
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
    for group in label_groups:
        # initialize datastruct for every group
        group_data = np.zeros(map_size, np.int8)
        dis_array = None
        label_coords = None

        for label in group:
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
                    group_data, dis_array = label_npy(group_data, label_coords, tag, dis_array, atom_grid_radius)
                if element_type is not None:
                    label_coords = element_coord_cif(structure, residue_type, element_type)
                    group_data, dis_array = label_npy(group_data, label_coords, tag, dis_array, atom_grid_radius)
                if metal_type is not None:
                    for metal in metal_type:
                        label_coords = element_coord_cif(structure, residue_type, metal)
                        group_data, dis_array = label_npy(group_data, label_coords, tag, dis_array, gemmi.Element(metal).vdw_r, atom_grid_radius)
            else:
                if atom_type is None and element_type is None or atom_type is not None:
                    protein_2nd_structure_coords = atom_coord_cif_protein_secondary(
                            structure, helices, sheets, residue_type, atom_type)
                    if 'Helix' in secondary_type:
                        group_data, dis_array = label_npy(group_data, protein_2nd_structure_coords[0], tag, dis_array, atom_grid_radius)
                    if 'Sheet' in secondary_type:
                        group_data, dis_array = label_npy(group_data, protein_2nd_structure_coords[1], tag, dis_array, atom_grid_radius)
                    if 'Loop' in secondary_type:
                        group_data, dis_array = label_npy(group_data, protein_2nd_structure_coords[2], tag, dis_array, atom_grid_radius)
                if element_type is not None:
                    protein_2nd_structure_coords = element_coord_cif_protein_secondary(
                        structure, helices, sheets, residue_type, element_type)
                    if 'Helix' in secondary_type:
                        group_data, dis_array = label_npy(group_data, protein_2nd_structure_coords[0], tag, dis_array, atom_grid_radius)
                    if 'Sheet' in secondary_type:
                        group_data, dis_array = label_npy(group_data, protein_2nd_structure_coords[1], tag, dis_array, atom_grid_radius)
                    if 'Loop' in secondary_type:
                        group_data, dis_array = label_npy(group_data, protein_2nd_structure_coords[2], tag, dis_array, atom_grid_radius)
        data.append(group_data)

        if generate_test is True:
            print(f'Generating Test Maps for "{normalized_map_path}"')
            for idx, group_name in enumerate(group_names):
                print(f'Generating Test Maps for Group: {group_name}')
                classes = len(label_groups[idx])
                for label in range(1, classes + 1):
                    out_map = os.path.join(os.path.dirname(normalized_map_path),f"EMD_{emdb_id}_{group_name}_{label}.mrc")
                    shutil.copy(normalized_map_path, out_map)
                    with mrcfile.open(out_map, mode='r+') as mrc:
                        TEST_data = np.zeros_like(group_data)
                        TEST_data = np.where(group_data == label, group_data, 0)
                        mrc.set_data(TEST_data)
                    print( f'   Label-{label} Written')
            return None

    data.append(map_data)
    group_names.append('map_sample')

    num_labels, sample_num = split_to_npy(data, temp_sample_path, start_coords,
                              n_samples, npy_size, group_names, emdb_id, extract_stride)

    return num_labels, sample_num



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
        mapc, mapr, maps = mrc.header.mapc, mrc.header.mapr, mrc.header.maps
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
                 group_names,
                 emdb_id,
                 extract_stride=32,
                 test_zero_ratio=0.001
):
    """
    Splits 3D data into smaller numpy arrays and saves them as .npy files.

    Parameters:
    - data: List of 3D numpy arrays to be split.
    - temp_sample_path: Directory to save the .npy files.
    - start_coords: Starting coordinates for splitting.
    - n_samples: Number of samples to generate in each dimension.
    - npy_size: Size of each .npy file.
    - sample_num: Shared counter for the number of samples.
    - group_names: List of group_names for the data.
    - extract_stride: Stride for extracting samples (default is 32).

    Functionality:
    1. Initializes a list to store the number of group_names.
    2. Adjusts the number of samples based on the npy_size and extract_stride.
    3. Creates directories for each label if they do not exist.
    4. Iterates through the data to extract and save samples as .npy files.
    5. Updates the count of group_names in each sample.
    6. Saves separated files for map data.
    7. Increments the sample counter.
    8. Returns the list of the number of group_names.
    """

    for idx in range(0, len(data) - 1):
        test_zero = sum((arr != 0).astype(np.uint8) for arr in data[:-1])

    sample_num = 0
    num_labels = np.array([np.zeros(30, dtype=np.int64) for _ in range(len(data)-1)])
    sample_start_z, sample_start_y, sample_start_x = start_coords
    for i in range(3):
        n_samples[i] = int(n_samples[i] * npy_size / extract_stride) - 1
    for group_name in group_names:
        os.makedirs(os.path.join(temp_sample_path, group_name), exist_ok=True)
    for n_z in range(n_samples[0]):
        idx_z = sample_start_z + extract_stride * n_z
        for n_y in range(n_samples[1]):
            idx_y = sample_start_y + extract_stride * n_y
            for n_x in range(n_samples[2]):
                idx_x = sample_start_x + extract_stride * n_x
                if test_zero[idx_z:idx_z + npy_size,
                             idx_y:idx_y + npy_size,
                             idx_x:idx_x + npy_size].sum() <= npy_size ** 3 * test_zero_ratio:
                    continue

                for idx in range(len(data)):
                    sample = data[idx][idx_z:idx_z + npy_size,
                             idx_y:idx_y + npy_size,
                             idx_x:idx_x + npy_size]
                    file_name = os.path.join(
                        temp_sample_path, group_name:=group_names[idx],
                        f"{group_name}_{emdb_id}_{sample_num}.npy")
                    np.save(file_name, sample)
                    if idx < len(data) - 1:  # Skip the last group (map_sample)
                        # Count the number of labels in the sample
                        count = np.bincount(sample.flatten())
                        count = np.pad(count, (0, max(0, 30 - len(count))),
                                    'constant')
                        num_labels[idx] += count

                # for idx in range(0, len(data) - 1):
                #     sample = data[idx][idx_z:idx_z + npy_size,
                #              idx_y:idx_y + npy_size,
                #              idx_x:idx_x + npy_size]
                #     file_name = os.path.join(
                #         temp_sample_path, group_name:=group_names[idx],
                #         f"{group_name}_{emdb_id}_{sample_num}.npy")
                #     np.save(file_name, sample)

                #     count = np.bincount(sample.flatten())
                #     count = np.pad(count, (0, max(0, 30 - len(count))),
                #                    'constant')
                #     num_labels[idx] += count

                # # Save separated files for map data
                # sample = data[len(data) - 1][idx_z:idx_z + npy_size,
                #          idx_y:idx_y + npy_size,
                #          idx_x:idx_x + npy_size]
                # file_name = os.path.join(temp_sample_path, group_name:=group_names[len(data) - 1],
                #                          f"{group_name}_{emdb_id}_{sample_num}.npy")
                # np.save(file_name, sample)

                sample_num += 1

    return num_labels, sample_num



def label_npy(group_data,
            label_coords,
            label_id,
            dis_array=None,
            atom_grid_radius=1.5):
    """
    Labels a 3D numpy array with specified coordinates and label ID.

    Parameters:
    - group_data: 3D numpy array to be labeled.
    - label_coords: List of coordinates to be labeled.
    - label_id: ID to label the coordinates with.
    - dis_array: Optional distance array for distance calculations (default is an empty array).
    - atom_grid_radius: Radius for labeling grid (default is 1.5).

    Functionality:
    1. Initializes the distance array if not provided.
    2. Calculates the index grid and creates a range for extensions.
    3. Generates a list of surrounding coordinates within the atom grid radius.
    4. Iterates through the label coordinates and calculates the floor coordinates.
    5. Labels the group_data array with the label_id for coordinates within the atom grid radius.
    6. Updates the distance array with the calculated distances.
    7. Returns the labeled group_data array and the updated distance array.
    """
    if dis_array is None:
        dis_array = np.full(group_data.shape, atom_grid_radius ** 2)

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
            try:
                if dist <= dis_array[around_coord[0], around_coord[1],
                around_coord[2]]:
                    group_data[around_coord[0], around_coord[1],
                    around_coord[2]] = label_id
                    dis_array[around_coord[0], around_coord[1],
                    around_coord[2]] = dist
            except IndexError:
                pass

    return group_data, dis_array



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


def split_folders(temp_sample_path,
                  final_sample_path,
                  ratio_t_t_v=(.8, .1, .1)):
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
    # return None
    # if os.path.exists(final_sample_path):
    #     # Delete the directory
    #     shutil.rmtree(final_sample_path)
    # # Create the directory again
    # os.makedirs(final_sample_path)
    splitfolders.ratio(
        input=temp_sample_path,
        output=final_sample_path,
        seed=44,
        ratio=ratio_t_t_v,  # we set the ratio / let users do it
        group_prefix=None,
        move=True)
    shutil.rmtree(temp_sample_path)


def label_maps(
    label_groups: list[dict[str:str | int]],
    group_names: list[str],
    metadata_path: str,
    raw_path: str = 'Raw',
    temp_sample_path: str = 'Temp_Sample',
    sample_path: str = 'Training',
    ratio_t_t_v: tuple[float, float, float] = (.8, .1, .1),
    npy_size: int = 64,
    extract_stride: int = 32,
    atom_grid_radius: float = 1.5,
    n_workers: int = 4,
):
    """
    Generates and manages datasets for training models.

    Parameters:
    - label_groups: List of label groups.
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
        assert (len(label_groups) == len(group_names))
    except AssertionError:
        raise ValueError(
            '!!! Label Groups and Group Names Should Have the Same Length !!!')

    # create dirs
    if not os.path.exists(temp_sample_path):
        os.makedirs(temp_sample_path)
    if not os.path.exists(sample_path):
        os.makedirs(sample_path)

    # read csv
    csv_info, path_info = read_csv_info(metadata_path, raw_path)
    emdb_ids, _, _ = csv_info
    _, model_paths, normalized_map_paths = path_info
    training_set_name = os.path.splitext(os.path.basename(metadata_path))[0]

    # configure logger
    logger = logging.getLogger('Dataset_Generation_Logger')
    logger.setLevel(logging.DEBUG)
    std_out_hdlr = logging.StreamHandler()
    std_out_hdlr.setLevel(logging.INFO)
    log_file_path = os.path.join(sample_path,
                                 training_set_name + '_generate_dataset.log')
    file_hdlr = logging.FileHandler(log_file_path)
    file_hdlr.setLevel(logging.DEBUG)
    file_hdlr.setFormatter(
        logging.Formatter('%(asctime)s %(levelname)s: %(message)s',
                          datefmt='%m/%d/%Y %I:%M:%S %p'))
    logger.addHandler(std_out_hdlr)
    logger.addHandler(file_hdlr)

    logger.info(calculate_title_padding('Generating dataset'))
    # log the label groups and their respective labels
    msg = 'Label Groups:\n'
    for idx, name in enumerate(group_names):
        msg += f'    Group {name}:\n'
        for label in label_groups[idx]:
            msg += f'       Label: {label}\n'
    logger.debug(msg)

    # num of label in each group for all models
    num_of_label_in_each_group_for_all_models = np.array(
        [np.zeros(30, dtype=np.int64) for _ in range(len(group_names))])

    logger.info('Start Generating Label Files from Maps and Models')

    futures = []
    try:
        with ProcessPoolExecutor(max_workers=n_workers) as executor:
            futures = [
                executor.submit(data_to_npy, label_groups, group_names,
                                normalized_map_paths[idx], model_paths[idx],
                                temp_sample_path, emdb_ids[idx], npy_size,
                                extract_stride, atom_grid_radius)
                for idx in range(len(emdb_ids))
            ]

            # Process the results as they complete
            with logging_redirect_tqdm([logger]):
                i = 0
                total_num_npy = 0
                for future in tqdm(as_completed(futures),
                                   total=len(futures),
                                   desc='Labeling Maps'):
                    try:
                        num_labels, sample_num = future.result(timeout=60 * 10)
                    except Exception as e:
                        logger.warning(
                            f'Generating Label Files Failed for EMDB-{emdb_ids[i]}: {e}'
                        )
                    else:
                        logger.info(
                            f'Finished Generating Label Files from EMDB-{emdb_ids[i]}'
                        )
                        num_of_label_in_each_group_for_all_models = [num_of_label_in_each_group_for_all_models[idx]+num_labels[idx]\
                                                                for idx in range(len(label_groups))]
                        total_num_npy += sample_num
                    finally:
                        i += 1
    except BrokenExecutor as e:
        logger.error(f'Error Generating Label Files: {e}')
        logger.error(
            '!!! Please Check the Input Map/Model Paths and Try Again !!!')
        logger.error(calculate_title_padding('Dataset Generation Failed'))
        return
    logger.info('Successfully Generated All Label Files')

    # 3.3 Split data into training and validation dataset
    final_sample_path = os.path.join(sample_path, training_set_name)
    logger.info('')
    logger.info(
        'Start Splitting Data into Training, Testing, and Validation Sets')
    os.makedirs(final_sample_path, exist_ok=True)  # 创建目录（如果不存在）
    shutil.rmtree(final_sample_path)               # 删除旧目录
    os.makedirs(final_sample_path)                   # 重新创建新目录

    # register to move log file to final sample path
    atexit.register(move_log_file, log_file_path, final_sample_path)

    # Stats
    msg = 'Statistical results:\n'
    msg += f"Dataset Size (Number of .npy Files): {total_num_npy}\n"
    num_of_label_in_each_group_for_all_models = [np.trim_zeros(sub_array, 'b') \
                                                 for sub_array in num_of_label_in_each_group_for_all_models]
    msg += "Number of Labels in Each Group:\n"
    ratio_of_label = {key: [] for key in group_names}
    for group_idx in range(len(label_groups)):
        group_name = group_names[group_idx]
        msg += f'    Group {group_name}:\n'
        sum_label_per_group = 0
        group = num_of_label_in_each_group_for_all_models[group_idx]
        if len(group) != 0:
            for label in range(len(group)):
                label_num = group[label]
                msg += f'        Label-{label}: {label_num}\n'
                sum_label_per_group += label_num
                ratio_of_label[group_name].append(int(group[0] // label_num))
                if label == len(group) - 1:
                    msg += f'        Total: {sum_label_per_group}\n'
        else:
            msg += '     The group is empty.\n'
            continue
    print('\n' + msg)
    stats_path = os.path.join(final_sample_path, 'statistics.txt')
    with open(stats_path, "w") as file:
        file.write(msg)
    logger.info(f'Statistics Results Written into "{stats_path}"')

    try:
        split_folders(temp_sample_path, final_sample_path, ratio_t_t_v)
        logger.info('Successfully Splitted Data')
    except Exception as e:
        logger.error(f'Splitting Failed. Error: {e}')

    # 3.4 Calculate weight, create weight file and save it (ratio of labels)
    weight_path = os.path.join(final_sample_path,
                               'class_weight_for_training.txt')
    with open(weight_path, "w") as file:
        json.dump(ratio_of_label, file)
    logger.info(f'Weights Written into "{weight_path}"')

    logger.info(calculate_title_padding('Dataset generation completed'))

    return final_sample_path  # this is the folder with both files. Alternatively, return [stats_path, weights_path]


def main():
    # from config file read default values
    generate_dataset_config = ConfigParser(default_section='generate_dataset')
    # generate_dataset_config.read('CryoDataBotConfig.ini')
    # ratio_t_t_v = (generate_dataset_config.getfloat('user_settings', 'ratio_training'),
    #                generate_dataset_config.getfloat('user_settings', 'ratio_testing'),
    #                generate_dataset_config.getfloat('user_settings', 'ratio_validation'),
    #                )
    # npy_size = generate_dataset_config.getint('user_settings', 'npy_size')
    # extract_stride = generate_dataset_config.getint('user_settings', 'extract_stride')
    # atom_grid_radius = generate_dataset_config.getfloat('user_settings', 'atom_grid_radius')
    # n_workers = generate_dataset_config.getint('user_settings', 'n_workers')
    ratio_t_t_v = (0.8,0.1,0.1)
    npy_size = 64
    extract_stride = 32
    atom_grid_radius = 1.0
    n_workers = 4
    # csv_path = 'CryoDataBot_Data/Metadata/ribosome_res_1-4_001/ribosome_res_1-4_001_Final.csv'
    # csv_path = "C:/Users/noelu/CryoDataBot/download_file_001/download_file_001_Final.csv"

    csv_path = '/home/qiboxu/Database/U_NET/EMDB_PDB_for_U_Net/Filtered_Dateset/cryoID2_metadata/cryoID2_metadata_Final-VOF-filter.csv'

    group_names = ['secondary_strctures', 'residue_types', 'key_atoms']
    from helper.atom_in_models import atoms_sugar_ring, residues_RNA
    label_groups = [
        [{
            'secondary_type': 'Helix',
            'residue_type': '',
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 1
        }, {
            'secondary_type': 'Sheet',
            'residue_type': '',
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 2
        }, {
            'secondary_type': 'Loop',
            'residue_type': '',
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 3
        }, {
            'secondary_type': '',
            'residue_type': ','.join(residues_RNA),
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 4
        }],
        [{
            'secondary_type': '',
            'residue_type': residues_protein[0],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 1
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[1],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 2
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[2],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 3
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[3],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 4
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[4],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 5
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[5],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 6
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[6],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 7
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[7],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 8
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[8],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 9
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[9],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 10
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[10],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 11
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[11],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 12
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[12],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 13
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[13],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 14
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[14],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 15
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[15],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 16
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[16],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 17
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[17],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 18
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[18],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 19
        }, {
            'secondary_type': '',
            'residue_type': residues_protein[19],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 20
        }, {
            'secondary_type': '',
            'residue_type': residues_RNA[0],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 21
        }, {
            'secondary_type': '',
            'residue_type': residues_RNA[1],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 22
        }, {
            'secondary_type': '',
            'residue_type': residues_RNA[2],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 23
        }, {
            'secondary_type': '',
            'residue_type': residues_RNA[3],
            'atom_type': '',
            'element_type': '',
            'metal_type': '',
            'label': 24
        }],
        [
            {
                'secondary_type': '',
                'residue_type': '',
                'atom_type': 'CA',
                'element_type': '',
                'metal_type': '',
                'label': 1
            },
            {
                'secondary_type': '',
                'residue_type': '',
                'atom_type': 'P',
                'element_type': '',
                'metal_type': '',
                'label': 2
            },
            {
                'secondary_type': '',
                'residue_type': '',
                'atom_type': ','.join(atoms_sugar_ring),
                'element_type': '',
                'metal_type': '',
                'label': 3
            },
        ],
    ]
    raw_path = '/home/qiboxu/Database/U_NET/EMDB_PDB_for_U_Net/Filtered_Dateset/Raw'
    temp_path = '/home/qiboxu/Database/U_NET/EMDB_PDB_for_U_Net/Filtered_Dateset/Temp'
    sample_path = '/home/qiboxu/Database/U_NET/EMDB_PDB_for_U_Net/Filtered_Dateset/Training'

    label_maps(
        label_groups=label_groups,
        group_names=group_names,
        metadata_path=csv_path,
        raw_path=raw_path,
        temp_sample_path=temp_path,
        sample_path=sample_path,
        ratio_t_t_v=ratio_t_t_v,
        npy_size=npy_size,
        extract_stride=extract_stride,
        atom_grid_radius=atom_grid_radius,
        n_workers=n_workers,
    )


if __name__ == "__main__":
    main()
