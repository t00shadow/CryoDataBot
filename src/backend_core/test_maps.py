import os
from configparser import ConfigParser

import cupy as cp
import requests

from .download_preprocess_maps import (download_one_map, map_normalizing,
                                       map_output)
from .generate_dataset import data_to_npy


def generate_test_label_maps(emdb_id: str|int,
                             test_path: str,
                             label_groups: list[dict[str: str|int]],
                             group_names: list[str]
                             ):
    # generate test dir
    os.makedirs(test_path, exist_ok=True)

    # get pdb_id
    print('Fetching Fitted PDB_ID...')
    emdb_id = str(emdb_id)
    url = f'https://www.ebi.ac.uk/emdb/api/entry/fitted/{emdb_id}'
    try:
        file = requests.get(url).json()
    except Exception as e:
        print(f'Error Getting Fitted PDB: {e}')
        exit(1)
    try:
        pdb_id = file['crossreferences']['pdb_list']['pdb_reference'][0]['pdb_id']
    except Exception as e:
        print('No Fitted PDB Found')
        exit(1)
    print('Fitted PDB_ID Fetched')

    # directories
    folder_name = 'EMD-' + emdb_id
    raw_map_path = os.path.join(test_path, folder_name, f"emd_{emdb_id}.map")
    model_path = os.path.join(test_path, folder_name, f"{pdb_id}.cif")
    normalized_map_path = os.path.join(test_path, folder_name,
            f"{os.path.splitext(os.path.basename(raw_map_path))[0]}_normalized.mrc")

    # download map and model file
    if os.path.exists(raw_map_path) and os.path.exists(model_path):
        print('Map and Model Already Downloaded')
    else:
        print('Downloading Map and Model...')
        try:
            download_one_map(emdb_id, pdb_id, raw_map_path, model_path, test_download=True)
        except Exception as e:
            print(f'Error Downloading Map and Model: {e}')
            exit(1)
        print('Download Completed')

    # fetch recommended_contour_level
    recl_file_path = os.path.join(test_path, folder_name, 'recl.txt')
    if os.path.exists(recl_file_path):
        print('Reading recommended_contour_level from File...')
        with open(recl_file_path, 'r') as recl_file:
            recl = float(recl_file.read().strip())
        print('Read recommended_contour_level from File')
    else:
        print('Fetching recommended_contour_level...')
        url = f"https://www.ebi.ac.uk/emdb/api/analysis/{emdb_id}"
        try:
            file = requests.get(url).json()
        except Exception as e:
            print(f'Error Fetching recommended_contour_level: {e}')
            exit(1)
        try:
            recl = file[emdb_id]["recommended_contour_level"]["recl"]
        except Exception as e:
            print('No recommended_contour_level Found')
            exit(1)
        else:
            print('Fetched recommended_contour_level')
            with open(recl_file_path, 'w') as recl_file:
                recl_file.write(str(recl))

    # normalize the map
    print('Normalizing Map...')
    map_F = map_normalizing(raw_map_path, recl)
    map_output(raw_map_path, cp.asnumpy(map_F), normalized_map_path, is_model=False)
    print(f'Normalized Map Saved as "{normalized_map_path}"')

    # delete previous test label maps
    test_map_folder = os.path.join(test_path, folder_name, 'Test_Maps')
    if os.path.exists(test_map_folder):
        os.remove(test_map_folder)

    # Generate test label map
    generate_dataset_config = ConfigParser(default_section='generate_dataset')
    config_path = os.path.join('src','backend_core','backend_helpers','CryoDataBotConfig.ini')
    generate_dataset_config.read(config_path)
    npy_size = generate_dataset_config.getint('user_settings', 'npy_size')
    extract_stride = generate_dataset_config.getint('user_settings', 'extract_stride')
    atom_grid_radius = generate_dataset_config.getfloat('user_settings', 'atom_grid_radius')
    data_to_npy(label_groups, 
                group_names, 
                normalized_map_path, 
                model_path,
                temp_sample_path=None,
                emdb_id=emdb_id, 
                generate_test=True,
                npy_size=npy_size,
                extract_stride=extract_stride,
                atom_grid_radius=atom_grid_radius)
