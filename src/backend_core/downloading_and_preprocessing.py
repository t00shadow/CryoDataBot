import gzip
import logging
import os
import shutil
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from configparser import ConfigParser

import cupy as cp
import gemmi
import mrcfile
import numpy as np
import pandas as pd
from cupyx.scipy.ndimage import binary_dilation, zoom
from sqlalchemy import over
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from backend_helpers.helper_funcs import calculate_title_padding, csv_col_reader, read_csv_info
from backend_core.redundancy_filter import map_model_filter


# main function
def downloading_and_preprocessing(metadata_path, 
                                  raw_dir: str = 'Raw', 
                                  overwrite = False,
                                  give_map: bool=True, 
                                  protein_tag_dist: int=1, 
                                  map_threshold=0.01,
                                  vof_threashold: float=0.25, 
                                  dice_threashold: float=0.4,
                                  ):
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
    logger = logging.getLogger('Downloading_and_Preprocessing_Logger')
    logger.setLevel(logging.INFO)  
    std_out_hdlr = logging.StreamHandler()
    std_out_hdlr.setLevel(logging.INFO)
    log_file_path = metadata_path.replace('.csv', '_downloading_and_preprocessing.log')

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
    logger.info(calculate_title_padding('Downloading Map & PDB Files'))
    logger.info(f'MetaData Path: "{os.path.abspath(metadata_path)}"')
    fetch_map_model(csv_info, path_info, overwrite)
    logger.info(calculate_title_padding('Downloading Completed'))
    logger.info('')

    # Step3: preprocess maps using multithreasing (Resample and normalize map files)
    logger.info(calculate_title_padding('Preprocessing Maps'))
    preprocess_maps(csv_info, 
                    path_info, 
                    metadata_path, 
                    give_map, 
                    protein_tag_dist, 
                    map_threshold,
                    vof_threashold, 
                    dice_threashold
                    )
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
    logger = logging.getLogger('Downloading_and_Preprocessing_Logger')
    emdb_ids, pdbs, _, _ = csv_info
    raw_map_paths, model_paths, _ = path_info
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(download_one_map, emdb_id, pdb, raw_map_path, model_path, overwrite)\
                   for emdb_id, pdb, raw_map_path, model_path in zip(emdb_ids, pdbs, raw_map_paths, model_paths)]
        with logging_redirect_tqdm([logger]):
            for _ in tqdm(as_completed(futures), total=len(emdb_ids), desc="Downloading map/pdb files"):
                pass


# Step2.1: download the map and model of one entry
def download_one_map(emdb_id, pdb, raw_map_path, model_path, overwrite=False):
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
    logger = logging.getLogger('Downloading_and_Preprocessing_Logger')

    path = os.path.dirname(raw_map_path)
    if os.path.exists(path):
        if overwrite:
            shutil.rmtree(path)
            os.makedirs(path)
        pass
    else:
        os.makedirs(path)

    emdb_fetch_link = f"https://ftp.ebi.ac.uk/pub/databases/emdb/structures/EMD-{emdb_id}/map/emd_{emdb_id}.map.gz"
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
            logger.info(f"Downloaded: emd_{emdb_id}.map")

    if not os.path.exists(model_path) or overwrite:
        try:
            urllib.request.urlretrieve(pdb_fetch_link, model_path)
        except Exception as e:
            logger.warning(f"Error Downloading PDB-{pdb} Model File: {e}")
        else:
            logger.info(f"Downloaded: {pdb}.cif")


# Step3: preprocess maps using multithreasing
def preprocess_maps(csv_info, 
                    path_info, 
                    metadata_path, 
                    give_map: bool=True, 
                    protein_tag_dist: int=1, 
                    map_threashold: float=0.15,
                    vof_threashold: float=0.25, 
                    dice_threashold: float=0.4
                    ):
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
    logger = logging.getLogger('Downloading_and_Preprocessing_Logger')

    _, _, _, recls = csv_info
    raw_map_paths, model_paths, _ = path_info

    results = []
    failed: list[str] = []
    with logging_redirect_tqdm([logger]):
        for raw_map_path, model_path, recl in tqdm(zip(raw_map_paths, model_paths, recls), total=len(raw_map_paths), desc='Preprocessing Maps'):
            try:
                vof, dice = preprocess_one_map(recl, raw_map_path, model_path, give_map, protein_tag_dist, map_threashold)
                results.append(('EMD-'+os.path.basename(raw_map_path).split(".")[0].split('_')[1], vof, dice))
            except ValueError as e:
                logger.warning(f'  Error Preprocessing Map: {e}')
                logger.warning('  !!! Preprocessing Failed !!!')
                logger.info('')
                failed.append('EMD-'+os.path.basename(raw_map_path).split(".")[0].split('_')[1])
            except FileNotFoundError as e:
                logger.warning(f'  Error Preprocessing Map: {e}')
                logger.warning('  !!! Preprocessing Failed !!!')
                logger.info('')
                failed.append('EMD-'+os.path.basename(raw_map_path).split(".")[0].split('_')[1])
            except Exception as e:
                logger.warning(f'  Error Preprocessing Map: {e}')
                logger.warning('  !!! Preprocessing Failed !!!')
                logger.info('')
                failed.append('EMD-'+os.path.basename(raw_map_path).split(".")[0].split('_')[1])

    # read metadata file
    metadata_df = pd.read_csv(metadata_path)

    # Print out failed maps
    logger.info('')
    if failed:
        logger.info('Failed to Preprocess Maps:')
        length = len(failed)
        for idx in range(0, length, num:=10):
            logger.info(f'  {", ".join(failed[idx:idx + num])}')
    failed_df_path = os.path.join(os.path.dirname(metadata_path), 'Archive', 'preprocessing_failed.csv')
    os.makedirs(os.path.dirname(failed_df_path), exist_ok=True)
    failed_df = metadata_df[metadata_df['emdb_id'].isin(failed)]
    failed_df.to_csv(failed_df_path, index=False)
    print(f'Please Check Failed Entries at:\n"{os.path.abspath(failed_df_path)}"')
    logger.info('')

    # save VOF/Dice            
    result_df = pd.DataFrame(results, columns=['emdb_id', 'vof', 'dice_coefficient'])
    metadata_df = metadata_df.merge(result_df, on='emdb_id', how='left')

    # Remove failed entries from metadata file
    metadata_df = metadata_df[~metadata_df['emdb_id'].isin(failed)]

    # remove the entries with poor map_to_model fitness
    kept_df, removed_df = map_model_filter(metadata_df, vof_threashold, dice_threashold)

    # save filtered file
    kept_df.to_csv(metadata_path, index=False)
    poor_map_path = os.path.join(os.path.dirname(metadata_path), 'Archive', 'poor_map_model_fitness.csv')
    removed_df.to_csv(poor_map_path, index=False)
    logger.info(f'VOF/DICE Written & Failed Entries Removed')
    logger.info(f'New Meatadata File Written at: "{os.path.abspath(metadata_path)}"')
    logger.info(f'Poor Map Model Fitness File Written at: "{os.path.abspath(poor_map_path)}"')
    logger.info(f'Total Number of Poor Maps: {len(removed_df)}')


# Step3.1: preprocess the map of one entry
def preprocess_one_map(recl: float, raw_map_path: str, model_path: str, give_map: bool=True, protein_tag_dist: int=2, map_threshold=0.01):
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
    logger = logging.getLogger('Downloading_and_Preprocessing_Logger')

    pdb = os.path.basename(model_path).split(".")[0]
    emdb_id = os.path.basename(raw_map_path).split(".")[0].split('_')[1]
    #save_path = os.path.dirname(raw_map_path)

    logger.info(f'Preprocessing Map: FITTED_PDB: {pdb} EMDB_ID: EMD-{emdb_id}')

    # TBD20240925: check if the origin is [0, 0, 0] first - if is not then just skip all of the rest steps and remove the entry in the csv
    with mrcfile.mmap(raw_map_path) as mrc:
        if mrc.header.nzstart != 0 or mrc.header.nystart != 0 or mrc.header.nxstart != 0:
            raise ValueError('The start of axis is not zero.')

    # if the origin is [0, 0, 0], then the following steps
    # Load the map
    try:
        logger.info('  Normalizing Map')
        map_F = map_normalizing(raw_map_path, recl)
        
        if give_map:
            map_path = f"{raw_map_path.split('.map')[0]}_normalized.mrc"
            map_output(raw_map_path, cp.asnumpy(map_F), map_path, is_model=False)
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
        logger.info('  Successfully Normalized Map')
        map_boundary = np.shape(map_F)

    try:
        protein_tag = map_from_cif(model_path, map_boundary, protein_tag_dist)
    except Exception as e:
        logger.warning(f'  Error Reading CIF File: {e}')
        logger.warning('  !!! Preprocessing Failed !!!')
        logger.info('')
        return (0, 0)   

    try:
        

        # Apply the map threshold
        map_F = cp.where(map_F > 0.15, 1, 0)
        protein_tag = cp.array(protein_tag)
        vof, dice = planes_map(map_F, protein_tag)
        
        map_path = f"{model_path.split('.cif')[0]}_simulated.mrc"
        map_output(raw_map_path, cp.asnumpy(protein_tag), map_path, is_model=True)
            
    except Exception as e:
            logger.warning(f'  Error Calculating Map to Model Fitness: {e}')
            logger.warning('  !!! Preprocessing Failed !!!')
            logger.info('')
            return (0, 0)
    else:
        logger.info('  Map_to_Model Calculation Completed:')
        logger.info(f'  Volume Overlap Fraction (VOF): {(vof*100):.4f}%, Dice Coefficient: {(dice*100):.4f}%')

    # # test
    # if give_map:
    #     save_path = os.path.dirname(raw_map_path)
    #     with mrcfile.new(os.path.join(save_path, f'CIF_{pdb}.mrc'), overwrite=True) as mrc:
    #         mrc.set_data(protein_tag)
    #     with mrcfile.new(os.path.join(save_path, f'overlapped_part.mrc'), overwrite=True) as mrc:
    #         mrc.set_data(overlap.astype(np.int8))
    #     with mrcfile.new(os.path.join(save_path, f'map_F.mrc'), overwrite=True) as mrc:
    #         mrc.set_data(map_F.astype(np.int8))
    #     logger.info(f'  Binary Map of {emdb_id} Saved as "BINARY_{emdb_id}.mrc"\n')

    logger.info('')

    return vof, dice


def planes_map(map_F, protein_tag):

    def helper_diag_gof(map_diag, cifmap_diag,all_top_gof,all_top_dc):
        map_diag = cp.where(map_diag>=1,1,0)
        cifmap_diag = cp.where(cifmap_diag>=1,1,0)
        overlap_count = cp.sum(cp.logical_and(map_diag, cifmap_diag))
        overlap = cp.where((cp.logical_and(map_diag, cifmap_diag)>0),1,0)
        union = cp.where((cp.logical_or(map_diag, cifmap_diag)>0),1,0)
        top_gof = cp.sum(overlap)/cp.sum(union)
        top_dc = overlap_count/(cp.sum(map_diag) + cp.sum(cifmap_diag))
        all_top_gof.append(float(top_gof))
        all_top_dc.append(float(top_dc))
        return


    all_top_gof = []
    all_top_dc = []
    for i in range(3):
        map_fx = cp.sum(map_F,axis=i)
        cifmap_fx = cp.sum(protein_tag,axis=i)
        helper_diag_gof(map_fx, cifmap_fx, all_top_gof, all_top_dc)
       

    for i in range(3):
        map_diag = cp.zeros((map_F.shape[0],map_F.shape[1]))
        cifmap_diag = cp.zeros((protein_tag.shape[0],protein_tag.shape[1]))
        if i==0:
            for j in range(map_F.shape[1]):
                map_diag += map_F[:,j,:]

            for j in range(map_F.shape[1]):
                cifmap_diag += protein_tag[:,j,:]

            helper_diag_gof(map_diag,cifmap_diag, all_top_gof, all_top_dc)
                  
        elif i==1:
            for j in range(map_F.shape[1]):
                map_diag += map_F[:,:,j]

            for j in range(map_F.shape[1]):
                cifmap_diag += protein_tag[:,:,j]

            helper_diag_gof(map_diag,cifmap_diag, all_top_gof, all_top_dc)
            
            
        elif i==2:
            for j in range(map_F.shape[1]):
                map_diag += map_F[j,:,:]

            for j in range(map_F.shape[1]):
                cifmap_diag += protein_tag[j,:,:]

            helper_diag_gof(map_diag,cifmap_diag, all_top_gof, all_top_dc)
              
    
    all_top_gof = cp.array(all_top_gof)
    all_top_gof = (cp.array(all_top_gof[all_top_gof != all_top_gof.max()])).mean()
    all_top_dc = cp.mean(cp.array(all_top_dc))

    return all_top_gof, all_top_dc


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
    with mrcfile.mmap(raw_map_path, 'r+') as mrc:
        # Load map data
        map_data = cp.array(mrc.data, dtype=np.float32)
        map_origin = np.array([mrc.header.nxstart, mrc.header.nystart, mrc.header.nzstart], dtype=np.int8)
        map_orientation = np.array([mrc.header.mapc, mrc.header.mapr, mrc.header.maps], dtype=np.float32)

        # Resample map to 1.0A*1.0A*1.0A grid size
        zoom_factors = [mrc.voxel_size.z, mrc.voxel_size.y, mrc.voxel_size.x]
        map_data = zoom(map_data, zoom_factors)

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

        map_orientation = np.array([mrc.header.mapc-1, mrc.header.mapr-1, mrc.header.maps-1], dtype=np.int32)
        map_data = cp.transpose(map_data, map_orientation)

    return map_data
    

# Step3.1.2: generate .mrc file
def map_output(input_map, map_data, output_map, is_model=False):
    if os.path.exists(output_map):
        os.remove(output_map)

    shutil.copyfile(input_map, output_map)
    with mrcfile.mmap(output_map, mode='r+') as mrc:
        if is_model:
            map_data = map_data.astype(np.int8)
        else:
            map_data = map_data.astype(np.float32)

        mrc.set_data(map_data)
        mrc.header.mz = map_data.shape[0]
        mrc.header.mapc, mrc.header.mapr, mrc.header.maps = 1, 2, 3
        mrc.header.ispg = 1  #401
        #mrc.print_header()


def map_from_cif(cif_path: str, MAP_BOUNDARY, PROTEIN_TAG_DIST):
        def atom_coord_cif(structure):
            """
            Extracts atomic coordinates (z, y, x) from a PDB/CIF structure file.
            
            Args:
                structure (Structure): Parsed structure file.

            Returns:
                cp.ndarray: Array of atomic coordinates on GPU.
            """
            coords = []
            for model in structure:
                for chain in model:
                    for residue in chain:
                        for atom in residue:
                            coords.append((int(round(atom.pos.z)), int(round(atom.pos.y)), int(round(atom.pos.x))))

            
            return cp.array(coords)
            
        protein_coords = atom_coord_cif(gemmi.read_structure(cif_path))    
        origin_info = cp.array([0,0,0])
        
        # Create binary map for protein coordinates
        MAP_BOUNDARY1 = ((int(MAP_BOUNDARY[0])),int((MAP_BOUNDARY[1])),int(MAP_BOUNDARY[2]))
        protein_tag = cp.zeros(shape=tuple(MAP_BOUNDARY1))
        protein_coords = np.round(protein_coords).astype(int)
        protein_tag[protein_coords[:, 0], protein_coords[:, 1], protein_coords[:, 2]] = 1

        # Binary dilation using GPU
        structure = cp.ones((PROTEIN_TAG_DIST * 2 + 1,) * 3, dtype=cp.int8)
        protein_tag = binary_dilation(protein_tag, structure=structure).astype(cp.int8)

        return protein_tag


if __name__ == '__main__':
    # from config file read default values
    downloading_and_preprocessing_config = ConfigParser(default_section='downloading_and_preprocessing')
    downloading_and_preprocessing_config.read('CryoDataBotConfig.ini')
    overwrite = downloading_and_preprocessing_config.getboolean('user_settings', 'overwrite')
    give_map = downloading_and_preprocessing_config.getboolean('user_settings', 'give_map')
    protein_tag_dist = downloading_and_preprocessing_config.getint('user_settings', 'protein_tag_dist')
    map_threashold = downloading_and_preprocessing_config.getfloat('user_settings', 'map_threashold')
    vof_threashold = downloading_and_preprocessing_config.getfloat('user_settings', 'vof_threashold')
    dice_threashold = downloading_and_preprocessing_config.getfloat('user_settings', 'dice_threashold')

    matadata_path = 'CryoDataBot_Data/Metadata/ribosome_res_1-4_001/ribosome_res_1-4_001_Final.csv'
    raw_dir = 'CryoDataBot_Data/Raw'
    downloading_and_preprocessing(matadata_path, 
                                  raw_dir, 
                                  overwrite,
                                  give_map,
                                  protein_tag_dist,
                                  map_threashold,
                                  vof_threashold,
                                  dice_threashold,
                                  )