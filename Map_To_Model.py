import numpy as np
import mrcfile
from tqdm import tqdm
import os
from scipy.ndimage import zoom
from datetime import datetime
import gemmi

#Help With Saving Files
now = datetime.now() # current date and time
text = now.strftime("_%m%d%Y_%H%M%S")

#Paths
SAVE_PATH = r'C:\Users\micha\OneDrive\Desktop\QIBO\CRYOEM_Data'
CIF_PATH = r"C:\Users\micha\Downloads\emd_0128 (4).map\6h25 (1).cif"
MAP_PATH = r"C:\Users\micha\Downloads\emd_0128 (4).map\emd_0128.map"


#Things to Play With
PROTEIN_TAG_DIST = int(1) #Atom Tag Distance in Angstroms
MAP_THRESHOLD = 0.01 #Voxel Density Threshold to Consider PROTEIN/MAP Overlap

################
#DO NOT CHANGE
ATOM_RADIUS = range(-1*PROTEIN_TAG_DIST, PROTEIN_TAG_DIST) #Tuple of Boundaries for Atom Tagging in Angstroms
################

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
    return coords                                                                                       # return np.array(coords)


def main_map_model_corr(map_path: str, cif_path: str, GIVE_MAP: bool=True):
    #Sample Name    
    PROTEIN_ID = os.path.basename(cif_path).split(".")[0]
    MAP_ID = os.path.basename(map_path).split(".")[0]    
    
    if GIVE_MAP:
        NEW_SAVE_FOLDER = os.path.join(SAVE_PATH,f'{MAP_ID}{text}')
        os.makedirs(NEW_SAVE_FOLDER, exist_ok=True)
      
    #Load the map
    map_F, origin_info, orientation_info = map_normalizing(map_path)
    MAP_BOUNDARY = np.shape(map_F)
    protein = gemmi.read_structure(CIF_PATH)
    protein_coords = np.array(atom_coord_cif(protein)).reshape(-1, 3)
    
    if origin_info[0] != 0 or origin_info[1] != 0 or origin_info[2] != 0:
        print(f'The start of axis of {MAP_ID} is not 0!!\nAdjusting the coordinates of {PROTEIN_ID} to match the map...')
        protein_coords -= origin_info
    
    if orientation_info[0] != 1 or orientation_info[1] != 2 or orientation_info[2] != 3:
        raise ValueError(f'The orientation of {MAP_ID} is not 1, 2, 3!!')
    
    # np.reshape(protein_coords, (-1, 3))
    # print("Type:",type(protein_coords))
    # print("Shape:",np.shape(protein_coords))
    
    #Check if any of the coordinates are out of bounds with the bounds of the map as 338, 338, 338
    # MAP_BOUNDARY = [np.shape(map_F)[0], np.shape(map_F)[1], np.shape(map_F)[2]]
    
    for i in range(len(protein_coords)):
        if protein_coords[i][0] > MAP_BOUNDARY[0] or protein_coords[i][1] > MAP_BOUNDARY[1] or protein_coords[i][2] > MAP_BOUNDARY[2]:
            print("Out of bounds:",protein_coords[i])
            raise ValueError(f'For PDB:{PROTEIN_ID} the atom at position {protein_coords[i]} is out of bounds with the {MAP_ID} Boundary:{MAP_BOUNDARY}')
            
    
    # out_of_bounds = np.array(out_of_bounds).reshape(-1, 3)
    # print("Number of out of bounds coordinates:",len(out_of_bounds))
    # print("Out of bounds coordinates:",out_of_bounds)
    
    
    # print("Map shape:",np.shape(map_F))
    # print("Map origin:",origin_info)
    # print("Map orientation:",orientation_info)
    
    protein_tag = np.zeros(MAP_BOUNDARY, dtype=np.int8)
  
    
    for i in tqdm(range(len(protein_coords))):
        x, y, z = protein_coords[i]       
        protein_tag[x, y, z] = 1
        for j in ATOM_RADIUS:
            # if x+j > MAP_BOUNDARY[0]:
            #     continue
            for k in ATOM_RADIUS:
                # if y+k > MAP_BOUNDARY[1]:
                #     continue
                for l in ATOM_RADIUS:
                    # if z+l < 0 or z+l > MAP_BOUNDARY[2]:
                    #     continue
                    protein_tag[x+j, y+k, z+l] = 1

    if GIVE_MAP:
        with mrcfile.new(os.path.join(NEW_SAVE_FOLDER,f'NORMALIZED_{MAP_ID}.mrc')) as mrc:
            mrc.set_data(map_F)
                    
    map_F[map_F > 0.05] = 1
    map_F[map_F <= 0.05] = 0
    # print("True Voxels After Normalization and shi",np.sum(map_F))
    # print("Voxels in Protein Tag:",np.sum(protein_tag))
    overlap = np.logical_and(protein_tag, map_F)
    # Count the number of overlapping voxels
    overlap_count = np.sum(overlap)

    # Optionally, calculate the volume overlap fraction (VOF)
    total_voxels_union = np.sum(np.logical_or(protein_tag, map_F))
    vof = overlap_count / total_voxels_union
    
    print(f"Volume overlap fraction (VOF): {vof}")
    
    if GIVE_MAP:
        with mrcfile.new(os.path.join(NEW_SAVE_FOLDER, f'CIF_{PROTEIN_ID}.mrc')) as mrc:
            mrc.set_data(protein_tag)
        # print("Saved")
        with mrcfile.new(os.path.join(NEW_SAVE_FOLDER,f'BINARY_{MAP_ID}.mrc')) as mrc:
            mrc.set_data(map_F)
            
        np_to_xyz(protein_coords, PROTEIN_ID, NEW_SAVE_FOLDER)
    
    return 1


def np_to_xyz(coords: np.ndarray, sample_name: str, save_folder) -> str:
    """
    Convert np.array of Coordinates to XYZ format.

    Args:
        coords (np.ndarray): Nx3 array of atomic coordinates.

    Returns:
        str: XYZ format string.
    """
    xyz = []
    num_atoms = len(coords)
    for i in range(num_atoms):
        for j in range(num_atoms):
            for k in range(num_atoms):
                xyz.append((float(i), float(j), float(k)))
    
    xyz = np.array(xyz).reshape(-1, 3)
    
    
    
    with open(os.path.join(save_folder, f'{sample_name}.xyz'), 'w') as f:
        f.write(f'{sample_name} 0 {num_atoms}\n')        
        # Write atom coordinates
        for i in range(num_atoms):
            x, y, z = xyz[i]
            f.write(f"C    {x:>12.6f}    {y:>12.6f}    {z:>12.6f}\n")
        
        # Ending line
        f.write("*\n")   
                    

    return 