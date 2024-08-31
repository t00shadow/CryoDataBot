import os
import shutil
import gemmi
import mrcfile
import numpy as np
import splitfolders
from MRC import MRC
import json
import logging

# for logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='generate_dataset.log', encoding='utf-8', level=logging.INFO,\
                    format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def data_to_npy(map_path: str,
                model_path: str,
                model_parts: list,
                sample_dir: str,
                sample_num: int = 0,
                npy_size: int = 64,
                generate_test: bool = False,
                classes: int = 24):
    """
    Read an MRC map file and a PDB model file, and create 3D numpy arraies with data from them.

    Args:
    - map_path (str): path to the MRC map file
    - model_path (str): path to the PDB model file
    - model_parts (list): list of dict representing parts and tag groups
    - sample_dir (str): path to a directory where the samples will be saved
    - sample_num (int): used to name the out put samples
    - npy_size (int = 64):

    """
    # Save map data and tagged data
    data = []
    part_names = []

    # Read the MRC map file and change the coordinates order to [z, y, x]
    mrc = MRC(map_path)
    map_data = mrc.swap_back_coordinates(mrc.dens, mrc.ordermode)
    map_size = [int(mrc.nz), int(mrc.ny), int(mrc.nx)]

    # Read the PDB model file
    structure = gemmi.read_structure(model_path)

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

    # Sample the selected parts of the model to create the numpy array, record the number of each tag in each part
    num_of_tag_in_each_part = {}  # Save number of each tag in each part

    # Creating tags
    helices, sheets = protein_2nd_structure_lists(structure)
    for part_name in range(len(model_parts)):
        secondary_type, residue_type, atom_type, element_type, metal_type, tag = model_parts[part_name]['secondary_type'].split(','), \
            model_parts[part_name]['residue_type'].split(','), model_parts[part_name]['atom_type'].split(','),\
            model_parts[part_name]['element_type'].split(','), model_parts[part_name]['metal_type'].split(','),\
                  model_parts[part_name]['tag']

        model_data = np.zeros(map_size, np.int8)  
        dis_array = np.array([])
        part_coords = None
        
        if residue_type == ['']:
            residue_type = None
        if atom_type == ['']:
            atom_type = None

        logger.info('Calculating and tagging atom coordinates.')
        try:
            if secondary_type == ['']:
                if element_type == [''] and metal_type == ['']:
                    part_coords = atom_coord_cif(structure, residue_type, atom_type)
                    model_data, dis_array = tag_npy(model_data, part_coords, tag, dis_array)
                elif element_type != [''] and metal_type == ['']:
                    part_coords = element_coord_cif(structure, residue_type, element_type)
                    model_data, dis_array = tag_npy(model_data, part_coords, tag, dis_array)
                elif element_type == [''] and metal_type != ['']:
                    for metal in metal_type:
                        part_coords = element_coord_cif(structure, residue_type, metal)
                        model_data, dis_array = tag_npy(model_data, part_coords, tag, dis_array, gemmi.Element(metal).vdw_r)
            else:   
                protein_2nd_structure_coords = atom_coord_cif_protein_secondary(
                        structure, helices, sheets, residue_type, atom_type)
                if 'Helix' in secondary_type:
                    model_data, dis_array = tag_npy(model_data, protein_2nd_structure_coords[0], tag, dis_array)
                if 'Sheet' in secondary_type:
                    model_data, dis_array = tag_npy(model_data, protein_2nd_structure_coords[1], tag, dis_array)
                if 'Loop' in secondary_type:
                    model_data, dis_array = tag_npy(model_data, protein_2nd_structure_coords[2], tag, dis_array)
            logger.info('Successfully calculated and tagged atom coordinates.')
        except Exception as e:
            logger.error(f'Calculation failed. Exception: {e}.')
        data.append(model_data)
        part_names.append(str(part_name+1))

        if generate_test is True:
            # Generate TEST.mrc for every value in one part
            logger.info('Generating test mrc(s).')
            try:
                for tag in range(1, classes + 1):
                    out_map = f"{map_path.split('.mrc')[0]}_EXAMPLE_{part_name}_{tag}.mrc"
                    print("=> Writing new map")
                    shutil.copy(map_path, out_map)
                    with mrcfile.open(out_map, mode='r+') as mrc:
                        TEST_data = np.zeros_like(model_data)
                        TEST_data = np.where(model_data == tag, model_data, 0)
                        mrc.set_data(TEST_data)
                        # mrc.header.mz = model_data.shape[0]
                    print("New map is writen.")
                    continue
                logger.info('Successfully generated test mrc(s).')
            except Exception as e:
                logger.error(f'Generation failed. Exception: {e}.')
            exit()

    # Create npy files from model_data of each part and map_data
    # Calcutate num of different tags
    data.append(map_data)
    part_names.append('map_sample')
    logger.info('Splitting tagged files into small cubes.')
    try:
        num_tags, sample_num = split_to_npy(data, sample_dir, start_coords,
                                        n_samples, npy_size, sample_num,
                                        part_names)
        logger.info('Splitting successful.')
    except Exception as e:
        logger.error(f'Splitting failed. Exception: {e}')
    
    for idx in range(len(part_names) - 1):
        num_of_tag_in_each_part[part_names[idx]] = num_tags[idx]

    return sample_num, num_of_tag_in_each_part


def compute_grid_params(box_min_list, box_max_list, axis_length_list,
                        grid_size): 
    """
    Computes the starting coordinate and number of grid samples along three axis for a given box.

    Args:
        box_min_list (List): Minimum coordinates of the box.
        box_max_list (List): Maximum coordinates of the box.
        axis_length_list (List): Lengths of the axes.
        grid_size (int): Size of the grid.

    Returns:
        List[int], List[int]: Starting coordinates and numbers of grid samples
        when sampling stride = 0.
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
                 sample_dir,
                 start_coords,
                 n_samples,
                 npy_size,
                 sample_num,
                 part_names,
                 extract_stride=32):
    """
    Extracts sub-volumes of size npy_size from the input data array, starting from the given start coordinates and generates npy files for each sub-volume.

    Parameters:
        data (list of ndarray): Input data arrays [tag_data1, tag_data2, ..., map_data]
        sample_dir (str): Directory to save the npy files
        start_coords (tuple): Tuple of start coordinates (z,y,x)
        n_samples (tuple): Tuple of number of samples to extract (z,y,x)
        npy_size (int): Size of the sub-volume to extract
        extract_stride (int): Stride length of the stepping sample
        sample_num (int): Number to use as suffix in the npy file names
        part_names (str): Name of the subdirectory to save the npy files

    Returns:
        None
    """
    num_tags = [0] * len(data)
    sample_start_z, sample_start_y, sample_start_x = start_coords
    for i in range(3):
        n_samples[i] = int(n_samples[i] * npy_size / extract_stride) - 1
    for part_name in part_names:
        os.makedirs(os.path.join(sample_dir, part_name), exist_ok=True)
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
                        sample_dir, part_names[idx],
                        f"model_{part_names[idx]}.{sample_num}.npy")
                    np.save(file_name, sample)

                    count = np.count_nonzero(sample)
                    num_tags[idx] += count

                # Save seperated files for map data
                sample = data[len(data) - 1][idx_z:idx_z + npy_size,
                         idx_y:idx_y + npy_size,
                         idx_x:idx_x + npy_size]
                file_name = os.path.join(sample_dir, part_names[len(data) - 1],
                                         f"map.{sample_num}.npy")
                np.save(file_name, sample)

                sample_num += 1

    return num_tags, sample_num


def tag_npy(model_data,
            part_coords,
            tag_id,
            dis_array=np.array([]),
            atom_grid_radius=1.5):
    """
    Add tags to 3D grid points surrounding given part coordinates.

    Args:
        model_data (ndarray): A 3D numpy array representing the 3D grid.
        part_coords (list of tuples): A list of tuples representing the part coordinates (z, y, x).
        tag_id (int): The tag value to apply to the tagged points.
        atom_grid_radius (int, optional): The radius of the grid to tag around the part coordinates. Defaults to 2.

    Returns:
        model_data (ndarray): The modified model data with the tagged points.
        dis_array (ndarray): The modified model data with the tagged points.
    """

    dis_array = np.full(model_data.shape, atom_grid_radius ** 2)

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

    for coord in np.array(part_coords):
        floor_coord = np.floor(coord).astype(int)
        for around in arounds:
            around_coord = floor_coord + around
            dist = np.sum((around_coord - coord) ** 2)
            if dist <= dis_array[around_coord[0], around_coord[1],
            around_coord[2]]:
                model_data[around_coord[0], around_coord[1],
                around_coord[2]] = tag_id
                dis_array[around_coord[0], around_coord[1],
                around_coord[2]] = dist

    return model_data, dis_array


def atom_coord_cif(structure, RESIDUE=None, ATOM=None):
    """
    Returns the atomic coordinates from a PDB structure for specific residues and atoms.

    Args:
        structure (Structure): PDB structure.
        RESIDUE (list, optional): List of residue names to select. Defaults to None (all residues).
        ATOM (list, optional): List of atom names to select. Defaults to None (all atoms).

    Returns:
        list: List of atomic coordinates as lists [z, y, x].
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
                    # coords.append(
                    #     (int(round(atom.pos.z)), int(round(atom.pos.y)),
                    #      int(round(atom.pos.x)))
                    # )
                    # coords.append(atom.pos),
                    coords.append([atom.pos.z, atom.pos.y, atom.pos.x])
    return coords

def element_coord_cif(structure, RESIDUE=None, ATOM=None):
    """
    Returns the atomic coordinates from a PDB structure for specific residues and atoms.

    Args:
        structure (Structure): PDB structure.
        RESIDUE (list, optional): List of residue names to select. Defaults to None (all residues).
        ATOM (list, optional): List of atom names to select. Defaults to None (all atoms).

    Returns:
        list: List of atomic coordinates as lists [z, y, x].
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
                    # coords.append(
                    #     (int(round(atom.pos.z)), int(round(atom.pos.y)),
                    #      int(round(atom.pos.x)))
                    # )
                    # coords.append(atom.pos),
                    coords.append([atom.pos.z, atom.pos.y, atom.pos.x])
    return coords


def protein_2nd_structure_lists(structure):
    helices, sheets, = [], []
    # helices = [[hlx_chain1, start.res_id.seqid.num, end.res_id.seqid.num],
    #            [hlx_chain2, start.res_id.seqid.num, end.res_id.seqid.num],
    #            ... ]

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
    coords, coords_helices, coords_sheets = [], [], []
    chain_helices = [row[0] for row in helices]
    chain_sheets = [row[0] for row in sheets]
    chain_name = list(set(chain_helices + chain_sheets))

    coords = atom_coord_cif(structure, RESIDUE, ATOM)

    for model in structure:
        for chain in model:
            if chain_name is not None and chain.name not in chain_name:
                continue
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
    # coords_others1 = [x for x in coords_sheets if x not in coords]
    # coords_others2 = [x for x in coords_helices if x not in coords]
    # print(coords_others1, coords_others2)

    return [coords_helices, coords_sheets, coords_loops]


def split_folders(temp_sample_path, sample_path):
    os.makedirs(sample_path, exist_ok=True)
    splitfolders.ratio(input=temp_sample_path,
                       output=sample_path,
                       seed=44,
                       ratio=(.8, .2),  # we set the ratio / let users do it
                       group_prefix=None,
                       move=True)
    shutil.rmtree(temp_sample_path)


def tag_maps(model_parts,map_paths,model_paths,temp_sample_path,emdb_ids,output_dir):
    # Step 3. Generate a dataset (3d numpy arraies) from map and model files
    # 3.1 Read map, model files and create lables
    logger.info('-'*5+'Generating dataset'+'-'*5)
    logger.info(f'Model parts: {model_parts}')
    # idx of npy file
    sample_num = 0

    # num of tag in each part for all models
    num_of_tag_in_each_part_for_all_models = {}
    for part in range(len(model_parts)):
        num_of_tag_in_each_part_for_all_models[str(part+1)] = 0

    for idx, emdb_id in enumerate(emdb_ids):
        # test for idx in [0,1]
        # for idx, emdb_id in enumerate(emdb_ids[0:1]):
        print(
            f"[{idx+1}/{len(emdb_ids)}] Generating dataset from EMDB-{emdb_id}... "
        )
        logger.info(f'[{idx+1}/{len(emdb_ids)}] Generating tagged file(s) from EMDB-{emdb_id}.')
        try:
            sample_num, num_of_tag_in_each_part = data_to_npy(
                map_paths[idx], model_paths[idx], model_parts,
                temp_sample_path, sample_num)
            logger.info(f'Successfully generated tagged file(s) from EMDB-{emdb_id}.')
        except Exception as e:
            logger.error(f'Generating tagged file(s) failed. Exception: {e}.')
        # Add number of each tag in new sampled model
        num_of_tag_in_each_part_for_all_models = {key: num_of_tag_in_each_part[key] + num_of_tag_in_each_part_for_all_models[key]\
                                                   for key in num_of_tag_in_each_part}

    # Delete 0s in tag number list and calculate 1/ratio of tag number
    ratio_of_tag = {}
    sum_tags = sum(num_of_tag_in_each_part_for_all_models.values())
    for key, val in num_of_tag_in_each_part_for_all_models.items():
        if val == 0:
            print(
                f'There is missing groups in part {key}, numbers of each class are {val}.'
            )
        ratio_of_tag[key] = val/sum_tags

    '''for key, value_list in num_of_tag_in_each_part_for_all_models.items():
        value_list = np.trim_zeros(value_list)
        num_of_tag_in_each_part_for_all_models[key] = value_list
        if 0 in value_list:
            print(
                f'There is missing groups in part {key}, numbers of each class are {value_list}.'
            )
        ratio_of_tag[key] = [
            int(value_list[0] // value_x) for value_x in value_list
            if value_x != 0
        ]'''

    # Print statistical results
    print(f"The number of .npy file: {sample_num}")
    print("Num of each tag: ")
    for key, value in num_of_tag_in_each_part_for_all_models.items():
        print(f'{key}: {value}')
    logger.info(f'Num of each tag: {num_of_tag_in_each_part_for_all_models}.')
    print("\nRatio of tags: ")
    for key, value in ratio_of_tag.items():
        formatted_value = "{:.2%}".format(value)
        print(f'{key}: {formatted_value}')
    logger.info(f'Ratio of tags: {ratio_of_tag}.')

    # 3.3 Split data into training and validation dataset
    sample_path = os.path.join(output_dir, "dataset")
    split_folders(temp_sample_path, sample_path)

    # 3.4 Calculate weight, create weight file and save it (ratio of tags)
    weight_path = os.path.join(sample_path, 'class_weight_for_training.txt')
    with open(weight_path, "w") as file:
        json.dump(ratio_of_tag, file)
    logger.info('-'*5+'Dataset generation completed'+'-'*5)

def generate_test_mrcs(generate_test = False, classes = 24):
    sample_num, num_of_tag_in_each_part = data_to_npy(map_path, model_path,
                                                    model_parts, sample_dir,
                                                    generate_test, classes)
    print(sample_num)
    print(num_of_tag_in_each_part)


if __name__ == "__main__":
    '''
    raw_map_paths = ["path_to_save_downloaded_map_and_model/EMD-37007_re_3.3/emd_37007.map",\
                     "path_to_save_downloaded_map_and_model/EMD-3145_re_3.3/emd_3145.map",\
                        'path_to_save_downloaded_map_and_model/EMD-41587_re_2.92/emd_41587.map']
    model_paths = ["path_to_save_downloaded_map_and_model/EMD-37007_re_3.3/8kab.cif",\
                   "path_to_save_downloaded_map_and_model/EMD-3145_re_3.3/5an9.cif",\
                    'path_to_save_downloaded_map_and_model/EMD-41587_re_2.92/8ts1.cif']
    emdb_ids = [37007, 3145, 41587]
    map_paths = normalize_raw_map(raw_map_paths)

    # this is the only function that needs to be called
    tag_maps(model_parts,map_paths,model_paths,temp_sample_path,emdb_ids,output_dir)
    '''

    # for testing data_to_npy()
    #map_path = r'path_to_save_downloaded_map_and_model/EMD-3145_re_3.3/emd_3145_normalized.mrc'
    #model_path = r'path_to_save_downloaded_map_and_model/EMD-3145_re_3.3/5an9.cif'
    map_path = r'path_to_save_downloaded_map_and_model/EMD-41587_re_2.92/emd_41587_normalized.mrc'
    model_path = r'path_to_save_downloaded_map_and_model/EMD-41587_re_2.92/8ts1.cif'
    # different model_parts
    #model_parts = [{'secondary_type': 'Helix', 'residue_type': 'ALA', 'atom_type': 'CA', 'element_type': '', 'metal_type': '', 'tag': 1}]
    #model_parts = [{'secondary_type': 'Helix', 'residue_type': 'ALA', 'atom_type': 'N', 'element_type': '', 'metal_type': '', 'tag': 2}]
    #model_parts = [{'secondary_type': '', 'residue_type': 'ALA', 'atom_type': 'CA', 'element_type': '', 'metal_type': '', 'tag': 3}]
    #model_parts = [{'secondary_type': 'Loop', 'residue_type': '', 'atom_type': '', 'element_type': '', 'metal_type': '', 'tag': 4}]
    #model_parts = [{'secondary_type': 'Sheet', 'residue_type': '', 'atom_type': '', 'element_type': '', 'metal_type': '', 'tag': 5}]
    #model_parts = [{'secondary_type': 'Sheet,Helix', 'residue_type': 'ALA', 'atom_type': 'CA', 'element_type': '', 'metal_type': '', 'tag': 6}]
    #model_parts = [{'secondary_type': '', 'residue_type': 'A,C,G,U,DA,DC,DG,DT', 'atom_type': '', 'element_type': 'N', 'metal_type': '', 'tag': 7}]
    model_parts = [{'secondary_type': '', 'residue_type': '', 'atom_type': '', 'element_type': '', 'metal_type': 'Mg', 'tag': 8}]
    sample_dir = 'testing_data_to_npy'

    sample_num, num_of_tag_in_each_part = data_to_npy(map_path, model_path,
                                                      model_parts, sample_dir,
                                                      generate_test=True)
    print(sample_num)
    print(num_of_tag_in_each_part)
