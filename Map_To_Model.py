import numpy as np
import mrcfile
from tqdm import tqdm
import os
from scipy.ndimage import zoom
from datetime import datetime
import gemmi
import threading
import queue



#Paths
#VOF = 19.7281% Dice = 32.9548%
SAVE_PATH = r'C:\Users\micha\OneDrive\Desktop\QIBO\CRYOEM_Data'
CIF_PATH = r"C:\Users\micha\Downloads\emd_0128 (4).map\6h25 (1).cif"
MAP_PATH = r"C:\Users\micha\Downloads\emd_0128 (4).map\emd_0128.map"

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


def write_updates(file_path: str, message_queue):
    """
    Write updates to a file.

    Args:
        file_path (str): The path to the file.
        message_queue: The message queue to get messages from.

    Returns:
        None
    """
    with open(file_path, 'a') as file:
        while True:
            message = message_queue.get()  # Get message from the queue
            if message == "STOP":
                break
            file.write(message + '\n')
            message_queue.task_done()
            

def main_map_model_corr(map_path: str, cif_path: str, GIVE_MAP: bool=True, PROTEIN_TAG_DIST: float=2, MAP_THRESHOLD: float=0.01):
    """
    Main function for mapping a model to a cryo-EM density map with correlation analysis.
    Args:
        map_path (str): The file path of the cryo-EM density map.
        cif_path (str): The file path of the model in CIF format.
        GIVE_MAP (bool, optional): Flag to indicate whether to save the density maps created for fitting. Defaults to True.
        PROTEIN_TAG_DIST (float, optional): The distance threshold for identifying protein tags. Defaults to 2.
        MAP_THRESHOLD (float, optional): The cutoff threshold for normalized densities. Defaults to 0.01.
    """
    now = datetime.now() # current date and time
    text = now.strftime("%m-%d-%Y_%H%M%S")
    
    #Create a Queue to store the Log Text
    out_text = queue.Queue()
    MAP_ID = os.path.basename(map_path).split(".")[0]
    NEW_SAVE_FOLDER = os.path.join(SAVE_PATH,f'{MAP_ID}__{text}')
    os.makedirs(NEW_SAVE_FOLDER, exist_ok=True)    
    out_text_path = os.path.join(NEW_SAVE_FOLDER,"LogFile.txt")
   
    
    writer_thread = threading.Thread(target=write_updates, args=(out_text_path, out_text))
    writer_thread.start()
    
    map_model_corr(map_path, cif_path, out_text, NEW_SAVE_FOLDER, GIVE_MAP, PROTEIN_TAG_DIST, MAP_THRESHOLD)
    
    out_text.put("STOP")
    out_text.join()
    writer_thread.join()

    return

def map_model_corr(map_path: str, cif_path: str, out_text: queue, NEW_SAVE_FOLDER: str, GIVE_MAP: bool=True, PROTEIN_TAG_DIST: float=2, MAP_THRESHOLD: float=0.01):
    """
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
 
    
    #Sample Name    
    PROTEIN_ID = os.path.basename(cif_path).split(".")[0]
    MAP_ID = os.path.basename(map_path).split(".")[0]    
    
    out_text.put(
        f'RUNNING MAP TO MODEL CORRELATION\n================================\n'
        f'Started At:{datetime.now()}\n\n'
        f'FITTED_PDB: {PROTEIN_ID}\nEMDB_ID: {MAP_ID}\n\n'
        f'PARAMETERS:\n{PROTEIN_TAG_DIST=}\n{MAP_THRESHOLD=}\n{PROTEIN_TAG_DIST=}Angstroms\n\n'        
        )     
    
    #Primarily for Debugging, Want to Visualize Map to PDB overlap from generated files
    if GIVE_MAP:
        out_text.put(f'GENERATED MRC MAPS SAVED: {GIVE_MAP}\n\n')
    
    else:
        out_text.put(f'GENERATED MRC MAPS SAVED: {GIVE_MAP}\n\n')
    
    
    #Load the map
    map_F, origin_info, orientation_info = map_normalizing(map_path)
    out_text.put(f'Successfully Loaded Voxel Data from {MAP_ID}\n')
    MAP_BOUNDARY = np.shape(map_F)
    
    #Load the Cif File
    protein = gemmi.read_structure(CIF_PATH)
    out_text.put(f'Successfully Loaded Coordinate Data from "{PROTEIN_ID}.cif"')
    protein_coords = np.array(atom_coord_cif(protein)).reshape(-1, 3)
    
    #Check if the origin of the map is 0,0,0 if not adjust atom coordinates so they match the map
    if origin_info[0] != 0 or origin_info[1] != 0 or origin_info[2] != 0:
        out_text.put(f'The start of axis of {MAP_ID} is not 0!!\nAdjusting the coordinates of {PROTEIN_ID} to match the map...')
        protein_coords -= origin_info
    
    ########################################################################################
    #Dont know if this is necessary, but some maps are not in the standard orientation
    # if orientation_info[0] != 1 or orientation_info[1] != 2 or orientation_info[2] != 3:
    #     raise ValueError(f'The orientation of {MAP_ID} is not 1, 2, 3!!')
    
    
    out_text.put(f'Number of Atoms in CIF:{len(protein_coords)}\n')
    
    #Check if any of the coordinates are out of bounds with the bounds of the map as 338, 338, 338    
    for i in range(len(protein_coords)):
        if protein_coords[i][0] > MAP_BOUNDARY[0] or protein_coords[i][1] > MAP_BOUNDARY[1] or protein_coords[i][2] > MAP_BOUNDARY[2]:
            out_text.put("Out of bounds:",protein_coords[i])
            raise ValueError(f'For PDB:{PROTEIN_ID} the atom at position {protein_coords[i]} is out of bounds with the {MAP_ID} Boundary:{MAP_BOUNDARY}')
    
    
    #Create a binary map of the protein coordinates    
    protein_tag = np.zeros(MAP_BOUNDARY, dtype=np.int8)
    
    ATOM_RADIUS = range(-1*PROTEIN_TAG_DIST, PROTEIN_TAG_DIST)
    for i in tqdm(range(len(protein_coords))):
        x, y, z = protein_coords[i]
        protein_tag[x, y, z] = 1
        for j in ATOM_RADIUS:
            # if x+j > origin_info[0]+(MAP_BOUNDARY[0]/2) or x+j < origin_info[0]-(MAP_BOUNDARY[0]/2):
            #    raise ValueError(
                # f'For PDB:{PROTEIN_ID} the atom at position {protein_coords[i]} is out 
                # of bounds with the {MAP_ID} Boundary:{MAP_BOUNDARY}')
            #     continue
            for k in ATOM_RADIUS:
                # if y+k > origin_info[1]+(MAP_BOUNDARY[1]/2) or y+k < origin_info[1]-(MAP_BOUNDARY[1]/2):
                # raise ValueError(
                    # f'For PDB:{PROTEIN_ID} the atom at position {protein_coords[i]} is out
                    # of bounds with the {MAP_ID} Boundary:{MAP_BOUNDARY}')
                #     continue
                for l in ATOM_RADIUS:
                    # if z+l > origin_info[2]+(MAP_BOUNDARY[2]/2) or z+l < origin_info[2]-(MAP_BOUNDARY[2]/2)
                    # raise ValueError(
                    # f'For PDB:{PROTEIN_ID} the atom at position {protein_coords[i]} is out
                    # of bounds with the {MAP_ID} Boundary:{MAP_BOUNDARY}')
                #     continue
                    protein_tag[x+j, y+k, z+l] = 1

    
    if GIVE_MAP:
        with mrcfile.new(os.path.join(NEW_SAVE_FOLDER,f'NORMALIZED_{MAP_ID}.mrc')) as mrc:
            mrc.set_data(map_F)
            out_text.put(f'Normalized Map Saved as "NORMALIZED_{MAP_ID}.mrc"\n')
                    
    map_F[map_F > 0.05] = 1
    map_F[map_F <= 0.05] = 0
    
    # Calculate the overlap between the protein and the map
    overlap = np.logical_and(protein_tag, map_F)
    
    # Count the number of overlapping voxels
    overlap_count = np.sum(overlap)

    # Calculate the volume overlap fraction (VOF)
    total_voxels_union = np.sum(np.logical_or(protein_tag, map_F))
    vof = overlap_count / total_voxels_union
    
    #Calculate Volume fit Using Discrete Dice Method
    dice = 2 * overlap_count / (np.sum(protein_tag) + np.sum(map_F))
        
    out_text.put(f'Volume overlap fraction (VOF): {(vof*100):.4f}%')
    out_text.put(f'Dice Coefficient: {(dice*100):.4f}%\n')
    
    
    if GIVE_MAP:
        with mrcfile.new(os.path.join(NEW_SAVE_FOLDER, f'CIF_{PROTEIN_ID}.mrc')) as mrc:
            mrc.set_data(protein_tag)
        out_text.put(f'Binary Map of {MAP_ID} Saved as "BINARY_{MAP_ID}.mrc"\n')
        with mrcfile.new(os.path.join(NEW_SAVE_FOLDER,f'BINARY_{MAP_ID}.mrc')) as mrc:
            mrc.set_data(map_F)
        out_text.put(f'Estimated Volume Data of {PROTEIN_ID} Saved as "CIF_{PROTEIN_ID}.mrc"\n')
        
    out_text.put(f'Finished At:{datetime.now()}')
    return


if __name__ == '__main__':
    print("Starting Program")
    main_map_model_corr(MAP_PATH, CIF_PATH, GIVE_MAP=True, PROTEIN_TAG_DIST=PROTEIN_TAG_DIST, MAP_THRESHOLD=MAP_THRESHOLD)
    #Help With Saving Files

    print("Program Finished")
 