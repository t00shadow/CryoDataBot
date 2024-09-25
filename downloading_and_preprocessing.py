import gzip
import logging
import os
import shutil
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

import cupy as cp
import gemmi
import mrcfile
import numpy as np
from cupyx.scipy.ndimage import binary_dilation, zoom
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

from helper_funcs import calculate_title_padding, csv_col_reader, read_csv_info 


# main function
def download_and_preprocessing(metadata_path, raw_dir: str = 'Raw', overwrite = False):
    """
    Reads metadata, downloads map and model files, and preprocesses the map files.

    Parameters:
    metadata_path (str): The path to the metadata file.
    raw_dir (str): The directory where raw map and model files will be saved.
    overwrite (bool): If True, existing files and directories will be overwritten.

    Steps:
    1. Read map list and generate raw map and model downloading paths.
       - Uses read_csv_info(metadata_path, raw_dir) to get csv_info and path_info.

    2. Download map and model files.
       - Logs and prints the start of the downloading process.
       - Uses fetch_map_model(csv_info, path_info, overwrite) to download the files.
       - Logs and prints the completion of the downloading process.

    3. Resample and normalize map files.
       - Uses preprocess_maps(path_info) to preprocess the downloaded map files.
    """ 
    # configure logger
    # get logger
    logger = logging.getLogger('Download_and_Preprocessing_Logger')
    logger.setLevel(logging.INFO)  
    std_out_hdlr = logging.StreamHandler()
    std_out_hdlr.setLevel(logging.INFO)
    log_file_path = os.path.join(dir:=os.path.dirname(metadata_path), dir.split('/')[-1]+\
                                 '_download_and_preprocessing.log')
    file_hdlr = logging.FileHandler(log_file_path)
    file_hdlr.setLevel(logging.INFO)
    #std_out_hdlr.setFormatter(logging.Formatter(''))
    file_hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'))
    logger.addHandler(std_out_hdlr)
    logger.addHandler(file_hdlr)

    # Step1: create map and model paths for downloading and preprocessing from csv info
    # read additional recl column using read_csv_info func
    read_csv_info_with_recl = csv_col_reader('recommended_contour_level')(read_csv_info)
    csv_info, path_info = read_csv_info_with_recl(metadata_path, raw_dir)

    # # Step2: download maps and models using multithreasing
    # logger.info(calculate_title_padding('Downloading Map & PDB Files'))
    # logger.info(f'MetaData Path: {metadata_path}')
    # fetch_map_model(csv_info, path_info, overwrite)
    # logger.info(calculate_title_padding('Downloading Completed'))
    # logger.info('')

    # Step3: preprocess maps using multithreasing (Resample and normalize map files)
    logger.info(calculate_title_padding('Preprocessing Maps'))
    preprocess_maps(csv_info, path_info)
    logger.info(calculate_title_padding('Preprocessing Completed'))
    logger.info('')


# Step2: download maps and models using multithreasing
def fetch_map_model(csv_info, path_info, overwrite=False):
    """
    Downloads map and model files concurrently using a thread pool.

    Parameters:
    csv_info (tuple): A tuple containing lists of EMDB identifiers, PDB identifiers, 
                      and EMDB IDs extracted from the metadata CSV.
    path_info (tuple): A tuple containing lists of raw map paths and model paths.
    overwrite (bool): If True, existing files and directories will be overwritten.

    Steps:
    1. Extracts EMDB identifiers, PDB identifiers, and EMDB IDs from csv_info.
    2. Extracts raw map paths and model paths from path_info.
    3. Uses ThreadPoolExecutor to download map and model files concurrently.
       - Submits download_one_map function for each map and model file.
    4. Uses tqdm to display a progress bar for the download tasks.
    """
    logger = logging.getLogger('Download_and_Preprocessing_Logger')
    emdbs, pdbs, _, emdb_ids, _ = csv_info
    raw_map_paths, model_paths, _ = path_info
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(download_one_map, emdb, pdb, emdb_id, raw_map_path, model_path, overwrite)\
                   for emdb, pdb, emdb_id, raw_map_path, model_path in zip(emdbs, pdbs, emdb_ids, raw_map_paths, model_paths)]
        with logging_redirect_tqdm([logger]):
            for _ in tqdm(as_completed(futures), total=len(emdbs), desc="Downloading map/pdb files"):
                pass


# Step2.1: download the map and model of one entry
def download_one_map(emdb, pdb, emdb_id, raw_map_path, model_path, overwrite=False):
    """
    Downloads and extracts a map file from the Electron Microscopy Data Bank (EMDB) 
    and a model file from the Protein Data Bank (PDB).

    Parameters:
    emdb (str): The EMDB identifier.
    pdb (str): The PDB identifier.
    emdb_id (str): The specific EMDB ID for the map file.
    raw_map_path (str): The path where the raw map file will be saved.
    model_path (str): The path where the model file will be saved.
    overwrite (bool): If True, existing files and directories will be overwritten.

    Directory Handling:
    - Checks if the directory for raw_map_path exists.
    - If it exists and overwrite is True, deletes the directory and recreates it.
    - If it doesn't exist, creates the directory.

    URL Construction:
    - Constructs the download links for the EMDB map file and the PDB model file 
      using the provided emdb, pdb, and emdb_id.

    Map File Download and Extraction:
    - Appends .gz to raw_map_path.
    - If the map file doesn't exist or overwrite is True, downloads the map file.
    - Extracts the .gz file and removes the compressed file.

    Model File Download:
    - If the model file doesn't exist or overwrite is True, downloads the model file.

    Logging:
    - Logs warnings if there are errors during the download process.
    - Logs info messages when files are successfully downloaded.
    """
    logger = logging.getLogger('Download_and_Preprocessing_Logger')

    path = os.path.dirname(raw_map_path)
    if os.path.exists(path):
        if overwrite:
            shutil.rmtree(path)
            os.makedirs(path)
        pass
    else:
        os.makedirs(path)

    emdb_fetch_link = f"https://ftp.ebi.ac.uk/pub/databases/emdb/structures/{emdb}/map/emd_{emdb_id}.map.gz"
    pdb_fetch_link = f"http://files.rcsb.org/download/{pdb}.cif"

    raw_map_path = f"{raw_map_path}.gz"

    if not os.path.exists(raw_map_path) or overwrite:
        try:
            urllib.request.urlretrieve(emdb_fetch_link, raw_map_path)
            with gzip.open(raw_map_path, 'rb') as f_in:
                with open(raw_map_path.split('.gz')[0], 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
                    os.remove(raw_map_path)
        except Exception as e:
            logger.warning(f"Error Downloading EMD_{emdb_id} Map File: {e}")
        else:
            logger.info(f"emd_{emdb_id}.map is Downloaded")

    if not os.path.exists(model_path) or overwrite:
        try:
            urllib.request.urlretrieve(pdb_fetch_link, model_path)
        except Exception as e:
            logger.warning(f"Error Downloading PDB-{pdb} Model File: {e}")
        else:
            logger.info(f"{pdb}.cif is Downloaded")

    return


# Step3: preprocess maps using multithreasing
def preprocess_maps(csv_info, path_info, give_map: bool=True, protein_tag_dist: int=1, map_threashold: float=0.01):
    """
    Preprocesses multiple map files by normalizing them and calculating their fitness with models.

    Parameters:
    path_info (list): A list containing map paths and CIF paths.
    give_map (bool): If True, saves the normalized maps and binary maps.
    protein_tag_dist (int): Theoretical atomic radii for map to model fitness calculation.
    map_threashold (float): Normalized map density cutoff.

    Steps:
    1. Extracts map paths and CIF paths from path_info.
    2. Logs the start of the preprocessing process.
    3. Initializes an empty list to store results.
    4. Uses tqdm to display a progress bar for the preprocessing tasks.
       - Iterates through each map path and CIF path.
       - Calls preprocess_one_map for each map and CIF file.
       - Appends the result to the results list.
    5. Logs the completion of the preprocessing process.
    """
    logger = logging.getLogger('Download_and_Preprocessing_Logger')
    _, _, _, _, recls = csv_info
    raw_map_paths, model_paths, _ = path_info
    results = []
    with logging_redirect_tqdm([logger]):

        for raw_map_path, model_path, recl in tqdm(zip(raw_map_paths, model_paths, recls), total=len(raw_map_paths), desc='Preprocessing Maps'):
            result = preprocess_one_map(recl, raw_map_path, model_path, give_map, protein_tag_dist, map_threashold)
            results.append(result)


# Step3.1: preprocess the map of one entry
def preprocess_one_map(recl: float, raw_map_path: str, model_path: str, give_map: bool=True, protein_tag_dist: int=1, map_threashold: float=0.01):
    """
    Preprocesses a map file by normalizing it and calculating its fitness with a model.

    Parameters:
    raw_map_path (str): Path to the map file.
    model_path (str): Path to the CIF file.
    give_map (bool): If True, saves the normalized map and binary map.
    protein_tag_dist (int): Theoretical atomic radii for map to model fitness calculation.
    map_threashold (float): Normalized map density cutoff.

    Returns:
    tuple:
        vof (float): Volume overlap fraction (VOF) between the map and the model.
        dice (float): Dice coefficient between the map and the model.

    Steps:
    1. Extracts protein and map IDs from the file paths.
    2. Logs the preprocessing start information.
    3. Loads and normalizes the map file using map_normalizing.
       - Logs warnings and returns (0,0) if normalization fails.
    4. Logs the successful loading of voxel data.
    5. Calculates the map boundary.
    6. Logs the map to model fitness calculation parameters.
    7. Loads the CIF file using gemmi.read_structure.
       - Logs warnings and returns (0,0) if reading fails.
    8. Logs the successful loading of coordinate data.
    9. Extracts and adjusts atom coordinates from the CIF file.
    10. Logs the number of atoms in the CIF file.
    11. Checks if any atom coordinates are out of bounds.
        - Logs warnings and returns (0,0) if coordinates exceed map boundaries.
    12. Creates a binary map for the protein coordinates.
        - Rounds the coordinates to integers.
        - Performs binary dilation to create spheres around atoms.
    13. Applies the map threshold.
    14. Calculates the overlap between the protein and the map.
    15. Calculates the volume overlap fraction (VOF) and Dice coefficient.
        - Logs warnings and returns (0,0) if calculation fails.
    16. Logs the calculation completion information.
    17. Saves the normalized map and binary map if give_map is True.
    18. Returns the VOF and Dice coefficient.
    """
    logger = logging.getLogger('Download_and_Preprocessing_Logger')

    pdb = os.path.basename(model_path).split(".")[0]
    emdb_id = os.path.basename(raw_map_path).split(".")[0]
    save_path = os.path.dirname(raw_map_path)

    logger.info(f'Preprocessing Map: FITTED_PDB: {pdb} EMDB_ID: EMD-{emdb_id}')

    # TBD20240925: check if the origin is [0, 0, 0] first - if is not then just skip all of the rest steps and remove the entry in the csv
    with mrcfile.mmap(raw_map_path) as mrc:
        if mrc.header.nzstart != 0 or mrc.header.nystart != 0 or mrc.header.nxstart != 0:
            raise ValueError('The start of axis is not zero.')

    # if the origin is [0, 0, 0], then the following steps
    # Load the map
    try:
        map_F = map_normalizing(raw_map_path, recl)
        # map_F, origin_info, _ = map_normalizing(raw_map_path, recl)

        if give_map:
            map_path = f"{raw_map_path.split('.map')[0]}_normalized.mrc"
            map_output(raw_map_path, map_F, map_path, is_model=False)
            logger.info(f'  Normalized Map Saved as "{map_path}"')
    except FileNotFoundError as e:
        logger.warning(f'  Error Loading Map: {e}')
        logger.warning('  !!! Preprocessing Failed !!!')
        logger.info('')
        return (0, 0)
    except ValueError as e:
        logger.warning(f'  Error Normalizing Map: {e}')
        logger.warning('  !!! Preprocessing Failed !!!')
        logger.info('')
        return (0, 0)
    else:
        logger.info('  Successfully Loaded Voxel Data.')
    map_boundary = np.shape(map_F)

    logger.info(f'  Calculating Map to Model Fitness with Theoretical Atomic Radii as "{protein_tag_dist}" and Normalized Map Density Cutoff as "{map_threashold}"')
    # Load the CIF file
    try:
        protein = gemmi.read_structure(model_path)
    except Exception as e:
        logger.warning(f'  Error Reading CIF File: {e}')
        logger.warning('  !!! Preprocessing Failed !!!')
        logger.info('')
        return (0, 0)
    else:
        logger.info('  Successfully Loaded Coordinate Data')
    protein_coords = np.array(atom_coord_cif(protein)).reshape(-1, 3)

    # # Adjust atom coordinates if origin is not (0,0,0)
    # protein_coords -= origin_info
    logger.info(f'  Number of Atoms in CIF: {len(protein_coords)}')

    # Check if any atom coordinates are out of bounds
    try:
        if np.any(np.any(protein_coords > map_boundary, axis=1)):
            raise ValueError('Out of bounds - atom coordinates exceed map boundaries')
    except ValueError as e:
        logger.warning(f'  Bound Error: {e}')
        logger.warning('  !!! Preprocessing Failed !!!')
        logger.info('')
        return (0, 0)

    try:
        # Create a binary map for the protein coordinates
        protein_tag = cp.zeros(map_boundary, dtype=np.int8)

        # Round the coordinates to integers
        protein_coords = np.round(protein_coords).astype(int)
        protein_tag[protein_coords[:, 0], protein_coords[:, 1], protein_coords[:, 2]] = 1

        # Perform binary dilation to create spheres around atoms
        structure = cp.ones((protein_tag_dist*2+1,) * 3, dtype=np.int8)
        protein_tag = cp.asnumpy(binary_dilation(protein_tag, structure=structure).astype(np.int8))

        # Apply the map threshold
        map_F = np.where(map_F > map_threashold, 1, 0)

        # Calculate overlap between the protein and the map
        overlap = np.logical_and(protein_tag, map_F)
        overlap_count = np.sum(overlap)

        # Calculate the volume overlap fraction (VOF)
        total_voxels_union = np.sum(np.logical_or(protein_tag, map_F))
        vof = overlap_count / total_voxels_union

        # Calculate Dice coefficient
        dice = 2 * overlap_count / (np.sum(protein_tag) + np.sum(map_F))
    except Exception as e:
            logger.warning(f'  Error Calculating Map to Model Fitness: {e}\n  !!! Preprocessing Failed !!!')
            return (0, 0)
    else:
        logger.info(f'  Calculation Completed: Volume Overlap Fraction (VOF): {(vof*100):.4f}%, Dice Coefficient: {(dice*100):.4f}%')

    # if give_map:
    #     with mrcfile.new(os.path.join(save_path, f'CIF_{pdb}.mrc'), overwrite=True) as mrc:
    #         mrc.set_data(protein_tag)
    #     logger.info(f'  Binary Map of {emdb_id} Saved as "BINARY_{emdb_id}.mrc"\n')


# Step3.1.1: normalize one map - make the grid size 1A and make the density range [0,1]
def map_normalizing(raw_map_path, recl=0.0):
    """
    Normalizes a map file by resampling and scaling its values.

    Parameters:
    raw_map_path (str): Path to the map file.

    Returns:
    tuple: 
        map_data (ndarray): The normalized map data.
        map_origin (ndarray): The origin of the map.
        map_orientation (ndarray): The orientation of the map.

    Steps:
    1. Loads the map data using mrcfile.mmap.
    2. Extracts the map origin and orientation from the header.
    3. Resamples the map to a 1.0A*1.0A*1.0A grid size using zoom factors.
    4. Normalizes the map values to the range (0.0, 1.0).
       - Uses the 99.9th percentile of the map data for normalization.
       - Raises a ValueError if the 99.9th percentile is zero.
    5. Checks if the start of the axis is zero and raises a ValueError if not.
    """
    if recl == '':
        recl = 0.0
    with mrcfile.mmap(raw_map_path) as mrc:
        # Load map data
        map_data = cp.array(mrc.data, dtype=np.float32)
        # map_origin = np.array([mrc.header.nxstart, mrc.header.nystart, mrc.header.nzstart], dtype=np.int8)
        # map_orientation = np.array([mrc.header.mapc, mrc.header.mapr, mrc.header.maps], dtype=np.float32)

        # Resample map to 1.0A*1.0A*1.0A grid size
        zoom_factors = [mrc.voxel_size.z, mrc.voxel_size.y, mrc.voxel_size.x]
        map_data = cp.asnumpy(zoom(map_data, zoom_factors))

        # remove noisy values that are too small
        count_good = np.sum(map_data > max(0, recl))
        count_total = map_data.size

        if recl>0.0:
            # set some small values less than 0 to make the recommended contour level 15th percentile among positive values
            bottom_value_percentile = (1-(count_good/0.85)/count_total)*100
            if bottom_value_percentile > 100:
                value_bottom = 0
            else:
                value_bottom = np.percentile(map_data, bottom_value_percentile)
        else:
            # set 30% lowest positive values less than 0
            bottom_value_percentile = (1-(count_good*0.7)/count_total)*100
            value_bottom = np.percentile(map_data, bottom_value_percentile)
        map_data -= max(value_bottom, 0)

        # Normalize map values to the range (0.0, 1.0)
        data_99_9 = np.percentile(map_data, 99.9)
        if data_99_9 == 0.:
            raise ValueError('Empty map (99.9th percentile of map data is zero)')
        map_data /= data_99_9
        map_data = np.clip(map_data, 0., 1.)

    return map_data
    # return map_data, map_origin, map_orientation


# Step3.1.2: generate .mrc file
def map_output(input_map, map_data, output_map, is_model=False):
    if os.path.exists(output_map):
        os.remove(output_map)

    shutil.copyfile(input_map, output_map)
    with mrcfile.open(output_map, mode='r+') as mrc:
        if is_model:
            map_data = map_data.astype(np.int8)
        else:
            map_data = map_data.astype(np.float32)

        mrc.set_data(map_data)
        mrc.header.mz = map_data.shape[0]
        mrc.header.ispg = 1  #401
        #mrc.print_header()


def atom_coord_cif(structure):
    """
    Extracts and rounds the atomic coordinates from a given structure.

    Parameters:
    structure (Bio.PDB.Structure.Structure): The structure containing models, chains, residues, and atoms.

    Returns:
    list: A list of tuples containing the rounded atomic coordinates (z, y, x).

    Steps:
    1. Initializes an empty list to store coordinates.
    2. Iterates through each model in the structure.
    3. Iterates through each chain in the model.
    4. Iterates through each residue in the chain.
    5. Iterates through each atom in the residue.
    6. Rounds the atomic coordinates (z, y, x) and appends them to the list.
    7. Returns the list of rounded atomic coordinates.
    """
    coords = []
    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    coords.append((int(round(atom.pos.z)), int(round(atom.pos.y)), int(round(atom.pos.x))))
    return coords


if __name__ == '__main__':
    matadata_path = '/home/qiboxu/Database/CryoDataBot_Data/Metadata/ribosome_res_3-4_20240924_001/ribosome_res_3-4_20240924_001.csv'
    raw_dir = '/home/qiboxu/Database/CryoDataBot_Data/Raw'
    download_and_preprocessing(matadata_path, raw_dir, overwrite=False)