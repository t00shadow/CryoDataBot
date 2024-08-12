import numpy as np
# import multiprocessing as mp
import mrcfile
from tqdm import tqdm
# from scipy.spatial import KDTree
import os
from Bio import PDB
# import shutil
from scipy.ndimage import zoom
from datetime import datetime

now = datetime.now()  # current date and time
text = now.strftime("%Y-%m-%d_%H-%M-%S")

# SavePath = r'D:/Database/U_NET/EMDB_PDB_for_U_Net/Filtered_Dateset/Raw'

def map_normalizing(map_path):
    with mrcfile.mmap(map_path) as mrc:
        # Load map data
        map_data = np.array(mrc.data, dtype=np.float32)

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

    return map_data


class MRC_FILE(object):
    def __init__(self):
        self.xdim, self.ydim, self.zdim = 0, 0, 0
        self.angstromX, self.angstromY, self.angstromZ = 0, 0, 0
        self.origin = 0
        self.orientation = 0

    def read_mrc(self, mrc_file_path):
        with mrcfile.open(mrc_file_path) as mrc:
            self.angstromX, self.angstromY, self.angstromZ = float(mrc.header.cella.x.item()), float(mrc.header.cella.y.item()), float(mrc.header.cella.z.item())  # cell dimensions
            self.xdim, self.ydim, self.zdim = int(mrc.header.nx.item()), int(mrc.header.ny.item()), int(mrc.header.nz.item()) #Determine Shape of Array
            self.orientation = [mrc.header.mapc.item(), mrc.header.mapr.item(), mrc.header.maps.item()] #Determine Orientation of Array
            self.origin = [mrc.header.nxstart.item(), mrc.header.nystart.item(), mrc.header.nzstart.item()]
            self.original_density = np.array(mrc.data)
            mrc.close()

        print("=== MRC File Read ===")
        print(f"EM_map Shape: {self.original_density.shape}")
        print(f"Cell Dimensions (angstroms): {self.angstromX, self.angstromY, self.angstromZ}")
        print(f"Array Dimensions: {self.xdim, self.ydim, self.zdim}")
        print(f"Orientation (MAPC, MAPR, MAPS): {self.orientation}")
        print(f"Origin: {self.origin}")
        print("=======================")

        return self.original_density

def map_model_corr(map_F, model_path: str):
    print("Start")
    pdb = model_path
    name = pdb[:3]
    p = PDB.PDBParser()
    s = p.get_structure(name, pdb)
    coord = np.concatenate([atom.get_coord() for atom in s.get_atoms()])
    coord = np.round(coord).astype(int)

    coord = np.array(coord).reshape(-1, 3)
    sample_tag = np.zeros(np.shape(map_F), dtype=np.int8)        
    # for x, y, z in tqdm(coord):
    #     sample_tag[max(0, x-1):min(map_F.shape[0], x+2), 
    #                 max(0, y-1):min(map_F.shape[1], y+2), 
    #                 max(0, z-1):min(map_F.shape[2], z+2)] = 1
    
    for i in tqdm(range(len(coord))):
        z, y, x = coord[i]
        x = int(x)
        y = int(y)
        z = int(z)
        sample_tag[x, y, z] = 1
        for j in range(-1, 1):
            for k in range(-1, 1):
                for l in range(-1, 1):
                    sample_tag[x+j, y+k, z+l] = 1
                
    #round every nonzero value in array to 1
    actual = map_F
    actual[actual > 0.15] = 1
    actual[actual <= 0.15] = 0
    print(sum(actual.flatten()))
    print(sum(sample_tag.flatten()))

    val = np.dot(sample_tag.flatten(),actual.flatten())
    corr = np.sum(val)/((np.sum(sample_tag)+np.sum(actual))/2)
    
    print("END")
    
    print(f"Correlation: {corr}")   

    return(actual,corr,sample_tag)

#function that plots a 3d array
#with multiprocessing








def check(map_paths, model_paths):
    corrs = []
    # map_A = map_normalizing(map_path)
    for map_path, model_path in zip(map_paths, model_paths):
        actual, corr, sampl = map_model_corr(map_path, model_path)
        corrs.append(corr)
    # with mrcfile.new(os.path.join(SavePath, f'testing{text}.mrc')) as mrc:
    #     mrc.set_data(sampl)
    # with mrcfile.new(os.path.join(SavePath,f'actual{text}.mrc')) as mrc:
    #     mrc.set_data(actual)

    return corrs




from backup.Utils_preprocess import read_csv_info

kept_path = "~/Database/U_NET/EMDB_PDB_for_U_Net/Filtered_Dateset/Raw/final-20240212.csv"

csv_info, path_info = read_csv_info(kept_path)
raw_map_paths, model_paths = path_info
map_paths = [f"{raw_map_path.split('.map')[0]}_normalized.mrc" for raw_map_path in raw_map_paths]

corrs = check(map_paths, model_paths)
print(corrs)



# pdb_s = r'C:\Users\micha\Downloads\2b4c.pdb'
# model = r'C:\Users\micha\Downloads\emd_0128 (1).map\emd_0128.mrc'
#pdb_s = r'C:\Users\micha\Downloads\pdb6h25\pdb6h25.pdb'