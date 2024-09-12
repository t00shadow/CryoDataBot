import numpy as np
import mrcfile
from tqdm import tqdm
import os
from scipy.ndimage import zoom, binary_dilation
from datetime import datetime
import gemmi
import threading
import logging
import queue



#Paths
#VOF = 19.7281% Dice = 32.9548%
# SAVE_PATH = r'C:\Users\micha\OneDrive\Desktop\QIBO\CRYOEM_Data'
# CIF_PATH = r"C:\Users\micha\Downloads\emd_0128 (4).map\6h25 (1).cif"
# MAP_PATH = r"C:\Users\micha\Downloads\emd_0128 (4).map\emd_0128.map"



CIF_PATH = r"E:\OneDrive\Desktop\EMD-6780_re_3.35\5xxu.cif"
MAP_PATH = r"E:\OneDrive\Desktop\EMD-6780_re_3.35\emd_6780.map"
# SAVE_PATH = "/home/qiboxu/Database/U_NET/EMDB_PDB_for_U_Net/Filtered_Dateset/Raw/EMD-6780_re_3.35/save"

# #Additional TESTING PATHS (These were bad fits)
# #VOF = 6.483% Dice = 12.18%
# MAP_PATH = r"C:\Users\micha\Downloads\EMD-11457_re_3.0\EMD-10958_re_2.85\emd_10958.map"
# CIF_PATH = r"C:\Users\micha\Downloads\EMD-11457_re_3.0\EMD-10958_re_2.85\6yw5.cif"

#Things to Play With
PROTEIN_TAG_DIST = int(1) #Atom Tag Distance in Angstroms
MAP_THRESHOLD = 0.01 #Voxel Density Threshold to Consider PROTEIN/MAP Overlap


def map_normalizing(map_path):
    with mrcfile.mmap(map_path) as mrc:
        # Load map data
        map_data = np.array(mrc.data, dtype=np.float32)
        map_origin = np.array([mrc.header.nxstart, mrc.header.nystart, mrc.header.nzstart], dtype=np.int8)
        map_orientation = np.array([mrc.header.mapc, mrc.header.mapr, mrc.header.maps], dtype=np.float32)

        # Resample map to 1.0A*1.0A*1.0A grid size
        zoom_factors = [mrc.voxel_size.z, mrc.voxel_size.y, mrc.voxel_size.x]
        map_data = zoom(map_data, zoom_factors)

        # Normalize map values to the range (0.0, 1.0)
        data_99_9 = np.percentile(map_data, 99.9)
        if data_99_9 == 0.:
            print('data_99_9 == 0!!')
            raise ValueError('99.9th percentile of map data is zero')
        map_data /= data_99_9
        map_data = np.clip(map_data, 0., 1.)

        if mrc.header.nzstart != 0 or mrc.header.nystart != 0 or mrc.header.nxstart != 0:
            print('The start of axis is not 0!!')
            raise ValueError('The start of axis is not zero!')

    return map_data, map_origin, map_orientation

def atom_coord_cif(structure):
    """
    Returns the atomic coordinates from a PDB structure for specific residues and atoms.

    Args:
        structure (Structure): PDB structure.
        RESIDUE (list, optional): List of residue names to select. Defaults to None (all residues).
        ATOM (list, optional): List of atom names to select. Defaults to None (all atoms).

    Returns:
        list: List of atomic coordinates as tuples (z, y, x).
    """
    coords = []
    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    coords.append((int(round(atom.pos.z)), int(round(atom.pos.y)), int(round(atom.pos.x))))            # coords.append(atom.pos), # coords.append([atom.pos.x, atom.pos.y, atom.pos.z])
    return coords                                                                           # return np.array(coords)

def map_model_helper(map_path: str, cif_path: str, GIVE_MAP: bool=False, PROTEIN_TAG_DIST: float=2, MAP_THRESHOLD: float=0.01):
    PROTEIN_ID = os.path.basename(cif_path).split(".")[0]
    MAP_ID = os.path.basename(map_path).split(".")[0]
    save_path = os.path.dirname(map_path)
    
    logging.info(f'FITTED_PDB: {PROTEIN_ID}\nEMDB_ID: {MAP_ID}\n\n')
    
    if GIVE_MAP:
        logging.info(f'GENERATED MRC MAPS SAVED: {GIVE_MAP}\n\n')
    
    # Load the map
    map_F, origin_info, orientation_info = map_normalizing(map_path)
    logging.info(f'Successfully Loaded Voxel Data from {MAP_ID}\n')
    MAP_BOUNDARY = np.shape(map_F)
    
    # Load the CIF file
    protein = gemmi.read_structure(cif_path)
    logging.info(f'Successfully Loaded Coordinate Data from "{PROTEIN_ID}.cif"')
    protein_coords = np.array(atom_coord_cif(protein)).reshape(-1, 3)
    
    # Adjust atom coordinates if origin is not (0,0,0)
    protein_coords -= origin_info
    
    logging.info(f'Number of Atoms in CIF: {len(protein_coords)}\n')
    
    # Check if any atom coordinates are out of bounds
    if np.any(np.any(protein_coords > MAP_BOUNDARY, axis=1)):
        logging.info(f'Out of bounds: Atom coordinates exceed map boundaries.\n')
        raise ValueError(f'For PDB:{PROTEIN_ID}, atom coordinates exceed the {MAP_ID} boundary {MAP_BOUNDARY}')
    
    # Create a binary map for the protein coordinates
    protein_tag = np.zeros(MAP_BOUNDARY, dtype=np.int8)
    
    # Round the coordinates to integers
    protein_coords = np.round(protein_coords).astype(int)
    protein_tag[protein_coords[:, 0], protein_coords[:, 1], protein_coords[:, 2]] = 1
    
    # Perform binary dilation to create spheres around atoms
    structure = np.ones((PROTEIN_TAG_DIST*2+1,) * 3, dtype=np.int8)
    protein_tag = binary_dilation(protein_tag, structure=structure).astype(np.int8)

    if GIVE_MAP:
        with mrcfile.new(os.path.join(save_path, f'NORMALIZED_{MAP_ID}.mrc', overwrite=True)) as mrc:
            mrc.set_data(map_F)
        logging.info(f'Normalized Map Saved as "NORMALIZED_{MAP_ID}.mrc"\n')

    # Apply the map threshold
    map_F = np.where(map_F > MAP_THRESHOLD, 1, 0)

    # Calculate overlap between the protein and the map
    overlap = np.logical_and(protein_tag, map_F)
    overlap_count = np.sum(overlap)
    
    # Calculate the volume overlap fraction (VOF)
    total_voxels_union = np.sum(np.logical_or(protein_tag, map_F))
    vof = overlap_count / total_voxels_union
    
    # Calculate Dice coefficient
    dice = 2 * overlap_count / (np.sum(protein_tag) + np.sum(map_F))
    
    logging.info(f'Volume overlap fraction (VOF): {(vof*100):.4f}%\n')
    logging.info(f'Dice Coefficient: {(dice*100):.4f}%\n')
    
    if GIVE_MAP:
        with mrcfile.new(os.path.join(save_path, f'CIF_{PROTEIN_ID}.mrc', overwrite=True)) as mrc:
            mrc.set_data(protein_tag)
        logging.info(f'Binary Map of {MAP_ID} Saved as "BINARY_{MAP_ID}.mrc"\n')
    
    return(vof, dice)

def map_model_corr(map_path: str, cif_path: str, GIVE_MAP: bool=False, PROTEIN_TAG_DIST: float=2, MAP_THRESHOLD: float=0.01):
    """)
    Calculates the map to model correlation by comparing a map file and a CIF file.
    Parameters:
    - map_path (str): The path to the map file.
    - cif_path (str): The path to the CIF file.
    - out_text (queue): The queue to store the output text.
    - NEW_SAVE_FOLDER (str): The path to the folder where the generated files will be saved.
    - GIVE_MAP (bool, optional): Whether to generate and save MRC maps. Defaults to True.
    - PROTEIN_TAG_DIST (float, optional): The distance in Angstroms to tag protein atoms in the map. Defaults to 2.
    - MAP_THRESHOLD (float, optional): The threshold value for the map. Defaults to 0.01.
    Returns:
    None
    """
    
    PROTEIN_ID = os.path.basename(cif_path).split(".")[0]
    MAP_ID = os.path.basename(map_path).split(".")[0]
    # save_path = os.path.dirname(map_path)
    save_path = r"E:\OneDrive\Desktop\EMD-6780_re_3.35"
    
    
    # configure logger
    logging.basicConfig(filename=os.path.join(save_path,'log.log'), encoding='utf-8', level=logging.INFO,\
                    format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('-'*5+f'Calculating Map to Model Fitness with Theoretical Atomic Radii as"{PROTEIN_TAG_DIST}"and Normalized Map Density Cutoff as"{MAP_THRESHOLD}".'+'-'*5)
    print('\n--------------------------------------------------------------------------------\nMap to Model Fitness Calculation\n--------------------------------------------------------------------------------')    
        
    logging.info(
        f'RUNNING MAP TO MODEL CORRELATION\n================================\n'
        f'Started At:{datetime.now()}\n\n'
        f'PARAMETERS:\nPROTEIN_TAG_DIST={PROTEIN_TAG_DIST}\nMAP_THRESHOLD={MAP_THRESHOLD}\n\n'        
        )     
    
    vof_list = []
    dice_list = []
    
    vof_list, dice_list = zip(map_model_helper(map_path, cif_path, GIVE_MAP, PROTEIN_TAG_DIST, MAP_THRESHOLD))

    
    logging.info('--------------------------------------------------------------------')







if __name__ == '__main__':
    print("Starting Program")
    map_model_corr(MAP_PATH, CIF_PATH, GIVE_MAP=True, PROTEIN_TAG_DIST=PROTEIN_TAG_DIST, MAP_THRESHOLD=MAP_THRESHOLD)
    #Help With Saving Files

    print("Program Finished")
 
