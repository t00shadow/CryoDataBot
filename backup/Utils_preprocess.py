import os
import shutil
import mrcfile
import numpy as np
import pandas as pd
from scipy.ndimage import zoom
import urllib.request
import gzip


DATA_PATH = "~/Database/U_NET/EMDB_PDB_for_U_Net/Filtered_Dateset/Raw"  # user input


# 1.1 Read map list and generate raw_map and model downloading paths
def read_csv_info(csv_path):
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
        f"{DATA_PATH}/{folder}/{raw_map}"
        for folder, raw_map in zip(folders, raw_maps)
    ]
    model_paths = [
        f"{DATA_PATH}/{folder}/{model}"
        for folder, model in zip(folders, models)
    ]
    csv_info = [emdbs, pdbs, resolutions, emdb_ids]
    path_info = [raw_map_paths, model_paths]
    return csv_info, path_info


# 1.2 Download map and model files
def fetch_map_model(csv_info, raw_map_paths, model_paths):
    emdbs, pdbs, _, emdb_ids = csv_info
    for idx, emdb in enumerate(emdbs):
        pdb = pdbs[idx]
        emdb_id = emdb_ids[idx]
        raw_map_path = raw_map_paths[idx]
        model_path = model_paths[idx]

        directory1 = os.path.dirname(raw_map_path)
        os.makedirs(directory1, exist_ok=True)

        emdb_fetch_link = f"https://ftp.ebi.ac.uk/pub/databases/emdb/structures/{emdb}/map/emd_{emdb_id}.map.gz"
        pdb_fetch_link = f"http://files.rcsb.org/download/{pdb}.cif"

        raw_map_gz_path = f"{raw_map_path}.gz"

        if not os.path.exists(raw_map_path):
            urllib.request.urlretrieve(emdb_fetch_link, raw_map_gz_path)
            with gzip.open(raw_map_gz_path, 'rb') as f_in:
                with open(raw_map_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            os.remove(raw_map_gz_path)

        if not os.path.exists(model_path):
            urllib.request.urlretrieve(pdb_fetch_link, model_path)
            print(f"=> {emdb} and pdb-{pdb} files are downloaded.")

    # if os.path.exists(f"{directory1}/emd_{emdb_id}.map"):
    #     pass
    # else:
    #     subprocess.run(["wget", "-P", directory1, emdb_fetch_link])
    #     subprocess.run(["gzip", "-d", f"{directory1}/emd_{emdb_id}.map.gz"])
    # if os.path.exists(f"{directory1}/{pdb}.cif"):
    #     pass
    # else:
    #     subprocess.run(["wget", "-P", directory1, pdb_fetch_link])
    #     print(f"=> {emdb} and pdb-{pdb} files are downloaded.")


# 1.3 Resampl and normalize map files
def normalize_raw_map(raw_map_paths):
    """
    return:
        normalized map paths
    """
    map_paths = [
        f"{raw_map_path.split('.map')[0]}_normalized.mrc"
        for raw_map_path in raw_map_paths
        ]
    for idx, map_path in enumerate(map_paths):
        if not os.path.exists(map_path):
            map_data = map_normalizing(raw_map_paths[idx])
            map_output(raw_map_paths[idx], map_data, map_path, is_model=False)

    return map_paths


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


def map_output(input_map, map_data, output_map, is_model=False):
    if os.path.exists(output_map):
        os.remove(output_map)

    print(f"=> Writing new map to {output_map}")
    shutil.copyfile(input_map, output_map)
    with mrcfile.open(output_map, mode='r+') as mrc:
        if is_model:
            map_data = map_data.astype(np.int8)
        else:
            map_data = map_data.astype(np.float32)

        mrc.set_data(map_data)
        mrc.header.mz = map_data.shape[0]
        mrc.header.ispg = 1  #401
        mrc.print_header()
        print("=> New map written successfully.")
