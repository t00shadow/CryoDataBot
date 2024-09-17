import os
import shutil
import mrcfile
import numpy as np
import pandas as pd
import cupy as cp
import urllib.request
import gzip
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm
import logging
import os
from cupyx.scipy.ndimage import zoom, binary_dilation
import gemmi


# configure logger
raw_data_dir = 'Raw'
logger = logging.getLogger(__name__)
logging.basicConfig(filename=raw_data_dir+'/download_and_preprocessing.log', encoding='utf-8', level=logging.INFO,\
                format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def download_and_preprocessing(metadata_path, raw_dir, overwrite = False):
    # Read map list and generate raw_map and model downloading paths
    csv_info, path_info = read_csv_info(metadata_path, raw_dir)

    # Download map and model files
    logger.info('-'*5+f'Downloading map/pdb files from {metadata_path}'+'-'*5)
    print('-'*5+f'Downloading map/pdb files from {metadata_path}'+'-'*5)
    fetch_map_model(csv_info, path_info, overwrite)
    print('-'*5+f'Downloading completed'+'-'*5)
    logger.info('-'*5+f'Downloading completed'+'-'*5)

    # Resample and normalize map files
    preprocess_maps(path_info)


def read_csv_info(csv_path, raw_dir):
    """
    arg(s):
        csv_path: path to .csv file
    return:
        csv_info:
        path_info: raw_map and model downloading paths
    """
    df = pd.read_csv(csv_path)
    emdbs, pdbs = df["emdb_id"], df["fitted_pdbs"]
    resolutions = df["resolution"].astype(str)
    emdb_ids = [emdb.split("-")[1] for emdb in emdbs]
    folders = [
        f"{emdb}_re_{resolution}"
        for emdb, resolution in zip(emdbs, resolutions)
    ]
    raw_maps = [f"emd_{emdb_id}.map" for emdb_id in emdb_ids]
    models = [f"{pdb}.cif" for pdb in pdbs]

    raw_map_paths = [
        f"{raw_dir}/{folder}/{raw_map}"
        for folder, raw_map in zip(folders, raw_maps)
    ]
    model_paths = [
        f"{raw_dir}/{folder}/{model}"
        for folder, model in zip(folders, models)
    ]
    csv_info = [emdbs, pdbs, resolutions, emdb_ids]
    path_info = [raw_map_paths, model_paths]
    return csv_info, path_info


def download_one_map(emdb, pdb, emdb_id, raw_map_path, model_path, overwrite = False):
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
            logger.warning(f"Error downloading EMD_{emdb_id} map file: {e}")
        else:
            logger.info(f"EMD_{emdb_id} file is downloaded")

    if not os.path.exists(model_path) or overwrite:
        try:
            urllib.request.urlretrieve(pdb_fetch_link, model_path)
        except Exception as e:
            logger.warning(f"Error downloading PDB-{pdb} model file: {e}")
        else:
            logger.info(f"PDB-{pdb} file is downloaded")

    return


def fetch_map_model(csv_info, path_info, overwrite = False):
    emdbs, pdbs, _, emdb_ids = csv_info
    raw_map_paths, model_paths = path_info
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(download_one_map, emdb, pdb, emdb_id, raw_map_path, model_path, overwrite)\
                   for emdb, pdb, emdb_id, raw_map_path, model_path in zip(emdbs, pdbs, emdb_ids, raw_map_paths, model_paths)]
        with logging_redirect_tqdm():
            for _ in tqdm(as_completed(futures), total=len(emdbs), desc="Downloading map/pdb files"):
                pass


def map_normalizing(map_path):
    with mrcfile.mmap(map_path) as mrc:
        # Load map data
        map_data = cp.array(mrc.data, dtype=np.float32)
        map_origin = np.array([mrc.header.nxstart, mrc.header.nystart, mrc.header.nzstart], dtype=np.int8)
        map_orientation = np.array([mrc.header.mapc, mrc.header.mapr, mrc.header.maps], dtype=np.float32)

        # Resample map to 1.0A*1.0A*1.0A grid size
        zoom_factors = [mrc.voxel_size.z, mrc.voxel_size.y, mrc.voxel_size.x]
        map_data = cp.asnumpy(zoom(map_data, zoom_factors))

        # Normalize map values to the range (0.0, 1.0)
        data_99_9 = np.percentile(map_data, 99.9)
        if data_99_9 == 0.:
            #print('data_99_9 == 0!!')
            raise ValueError('Empty map (99.9th percentile of map data is zero)')
        map_data /= data_99_9
        map_data = np.clip(map_data, 0., 1.)

        if mrc.header.nzstart != 0 or mrc.header.nystart != 0 or mrc.header.nxstart != 0:
            #print('The start of axis is not 0!!')
            raise ValueError('The start of axis is not zero.')

    return map_data, map_origin, map_orientation


def atom_coord_cif(structure):
    coords = []
    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    coords.append((int(round(atom.pos.z)), int(round(atom.pos.y)), int(round(atom.pos.x))))            # coords.append(atom.pos), # coords.append([atom.pos.x, atom.pos.y, atom.pos.z])
    return coords                                                                           # return np.array(coords)


def preprocess_one_map(map_path: str, cif_path: str, give_map: bool=False, protein_tag_dist: int=1, map_threashold: float=0.01):
    protein_id = os.path.basename(cif_path).split(".")[0]
    map_id = os.path.basename(map_path).split(".")[0]
    save_path = os.path.dirname(map_path)
    
    logging.info(f'Preprocessing Map:\n  FITTED_PDB: {protein_id} EMDB_ID: {map_id}')
    
    # Load the map
    try:
        map_F, origin_info, _ = map_normalizing(map_path)
    except ValueError as e:
        logging.warning(f'  Error Normalizing Map: {e}\n  Preprocessing Failed')
        return (0,0)
    else:
        logging.info(f'  Successfully Loaded Voxel Data.')
    map_boundary = np.shape(map_F)
    
    logger.info(f'  Calculating Map to Model Fitness with Theoretical Atomic Radii as "{protein_tag_dist}" and Normalized Map Density Cutoff as "{map_threashold}"')
    # Load the CIF file
    try:
        protein = gemmi.read_structure(cif_path)
    except Exception as e:
        logging.warning(f'  Error Reading CIF File: {e}\n  Preprocessing Failed')
        return (0,0)
    else:
        logging.info(f'  Successfully Loaded Coordinate Data')
    protein_coords = np.array(atom_coord_cif(protein)).reshape(-1, 3)
    
    # Adjust atom coordinates if origin is not (0,0,0)
    protein_coords -= origin_info
    
    logging.info(f'  Number of Atoms in CIF: {len(protein_coords)}')
    
    # Check if any atom coordinates are out of bounds
    try:
        if np.any(np.any(protein_coords > map_boundary, axis=1)):
            raise ValueError('  Out of bounds - atom coordinates exceed map boundaries')
    except ValueError as e:
        logging.warning(f'  Bound Error: {e}\n  Preprocessing Failed')
        return (0,0)
    
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
            logging.warning(f'  Error Calculating Map to Model Fitness: {e}\n  Preprocessing Failed')
            return (0,0)
    else:
        logging.info(f'  Calculation Completed:\n                           Volume overlap fraction (VOF): {(vof*100):.4f}% Dice Coefficient: {(dice*100):.4f}%')

    if give_map:
        with mrcfile.new(os.path.join(save_path, f'NORMALIZED_{map_id}.mrc'), overwrite=True) as mrc:
            mrc.set_data(map_F)
        logging.info(f'  Normalized Map Saved as "NORMALIZED_{map_id}.mrc"')
        with mrcfile.new(os.path.join(save_path, f'CIF_{protein_id}.mrc'), overwrite=True) as mrc:
            mrc.set_data(protein_tag)
        logging.info(f'  Binary Map of {map_id} Saved as "BINARY_{map_id}.mrc"')
    
    return (vof, dice)


def preprocess_maps(path_info: list, give_map: bool=False, protein_tag_dist: int=1, map_threashold: float=0.01):
    map_paths, cif_paths = path_info

    logging.info('-'*5+'Preprocessing Maps'+'-'*5)      
    results = []
    with logging_redirect_tqdm():
        for map_path, cif_path in tqdm(zip(map_paths, cif_paths), total=len(map_paths), desc='Preprocessing Maps'):
            result = preprocess_one_map(map_path, cif_path, give_map, protein_tag_dist, map_threashold)
            results.append(result)
    logging.info('-'*5+'Preprocessing Completed'+'-'*5)


if __name__ == '__main__':
    matadata_path = 'Metadata/ribosome_res_1-4/ribosome_res_1-4.csv'
    raw_dir = 'Raw'
    download_and_preprocessing(matadata_path, raw_dir, overwrite=True)