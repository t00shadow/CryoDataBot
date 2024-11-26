import os
from configparser import ConfigParser

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
        return None
    try:
        pdb_id = file['crossreferences']['pdb_list']['pdb_reference'][0]['pdb_id']
    except Exception as e:
        print('No Fitted PDB Found')
        return None
    print('Fitted PDB_ID Fetched')

    # directories
    folder_name = 'EMD-' + emdb_id
    raw_map_path = os.path.join(test_path, folder_name, f"emd_{emdb_id}.map")
    model_path = os.path.join(test_path, folder_name, f"{pdb_id}.cif")
    normalized_map_path = os.path.join(test_path, folder_name,
            f"{os.path.splitext(os.path.basename(raw_map_path))[0]}_normalized.mrc")

    # download map and model file
    print('Downloading Map and Model File...')
    download_one_map(emdb_id, pdb_id, raw_map_path, model_path, overwrite=True)
    print('Download Completed')

    # fetch recommended_contour_level
    print('Fetching recommended_contour_level...')
    url = f"https://www.ebi.ac.uk/emdb/api/analysis/{emdb_id}"
    try:
        file = requests.get(url).json()
    except Exception as e:
        print(f'Error Fetching recommended_contour_level: {e}')
        return None
    try:
        recl = file[emdb_id]["recommended_contour_level"]["recl"]
    except Exception as e:
        print('No recommended_contour_level Found')
        return None
    
    # normalize the map
    print('Normalizing Map...')
    map_F = map_normalizing(raw_map_path, recl)
    map_output(raw_map_path, map_F, normalized_map_path, is_model=False)
    print(f'Normalized Map Saved as "{normalized_map_path}"')

    # Generate test label map
    generate_dataset_config = ConfigParser(default_section='generate_dataset')
    generate_dataset_config.read(os.path.join('backend_helpers','CryoDataBotConfig.ini'))
    npy_size = generate_dataset_config.getint('user_settings', 'npy_size')
    extract_stride = generate_dataset_config.getint('user_settings', 'extract_stride')
    atom_grid_radius = generate_dataset_config.getfloat('user_settings', 'atom_grid_radius')

    data_to_npy(normalized_map_path, 
                model_path, 
                label_groups, 
                None, 
                group_names, 
                emdb_id, 
                generate_test=True,
                npy_size=npy_size,
                extract_stride=extract_stride,
                atom_grid_radius=atom_grid_radius)
    