import os
from configparser import ConfigParser

import requests

from atom_in_models import residues_protein
from downloading_and_preprocessing import (download_one_map,
                                           downloading_and_preprocessing,
                                           map_normalizing, map_output)
from fetch_sample_info import search_emdb
from generate_dataset import data_to_npy, label_maps
from redundancy_filter import filter_csv


def main(
        search_query: str,
        label_groups: list[dict[str: str|int]],
        group_names: list[str],
        file_name: str=None,
        cryo_data_bot_data_path: str='CryoDataBot_Data',
        metadata_path: str='Metadata',
        raw_path: str='Raw',
        sample_path: str='Sample',
        temp_path: str='Temp'
        ) -> None:   
    # create directories if not exist
    os.makedirs(cryo_data_bot_data_path, exist_ok=True)
    metadata_path = os.path.join(cryo_data_bot_data_path, metadata_path)
    os.makedirs(metadata_path, exist_ok=True)
    raw_path = os.path.join(cryo_data_bot_data_path, raw_path)
    os.makedirs(raw_path, exist_ok=True)
    sample_path = os.path.join(cryo_data_bot_data_path, sample_path)
    os.makedirs(sample_path, exist_ok=True)
    temp_path = os.path.join(cryo_data_bot_data_path, temp_path)
    os.makedirs(temp_path, exist_ok=True)

    # download EMDB csv file
    # from config file read default values
    fetch_sample_info_config = ConfigParser(default_section='fetch_sample_info')
    fetch_sample_info_config.read('CryoDataBotConfig.ini')
    fetch_qscore = fetch_sample_info_config.getboolean('user_settings', 'fetch_qscore')
    fetch_classification = fetch_sample_info_config.getboolean('user_settings', 'fetch_classification')
    rows = fetch_sample_info_config.getint('user_settings', 'rows')
    csv_path = search_emdb(query=search_query,
                           file_name=file_name,
                           save_path=metadata_path,
                           fetch_qscore=fetch_qscore,
                           fetch_classification=fetch_classification, 
                           rows=rows,
                           )

    # filter csv file
    # from config file read default values
    redundancy_filter_config = ConfigParser(default_section='redundancy_filter')
    redundancy_filter_config.read('CryoDataBotConfig.ini')
    q_threshold = redundancy_filter_config.getfloat('user_settings', 'q_threshold')
    uni_threshold = redundancy_filter_config.getfloat('user_settings', 'uni_threshold')
    csv_path = filter_csv(input_csv=csv_path, 
                          q_threshold=q_threshold, 
                          uni_threshold=uni_threshold, 
                          )

    # download and preprocess raw data
    # from config file read default values
    downloading_and_preprocessing_config = ConfigParser(default_section='downloading_and_preprocessing')
    downloading_and_preprocessing_config.read('CryoDataBotConfig.ini')
    overwrite = downloading_and_preprocessing_config.getboolean('user_settings', 'overwrite')
    give_map = downloading_and_preprocessing_config.getboolean('user_settings', 'give_map')
    protein_tag_dist = downloading_and_preprocessing_config.getint('user_settings', 'protein_tag_dist')
    map_threashold = downloading_and_preprocessing_config.getfloat('user_settings', 'map_threashold')
    vof_threashold = downloading_and_preprocessing_config.getfloat('user_settings', 'vof_threashold')
    dice_threashold = downloading_and_preprocessing_config.getfloat('user_settings', 'dice_threashold')
    downloading_and_preprocessing(matadata_path=csv_path, 
                                  raw_dir=raw_path, 
                                  overwrite=overwrite,
                                  give_map=give_map,
                                  protein_tag_dist=protein_tag_dist,
                                  map_threashold=map_threashold,
                                  vof_threashold=vof_threashold,
                                  dice_threashold=dice_threashold,
                                  )

    # label maps and split dataset
    # from config file read default values
    generate_dataset_config = ConfigParser(default_section='generate_dataset')
    generate_dataset_config.read('CryoDataBotConfig.ini')
    ratio_t_t_v = (generate_dataset_config.getfloat('user_settings', 'ratio_training'),
                   generate_dataset_config.getfloat('user_settings', 'ratio_testing'),
                   generate_dataset_config.getfloat('user_settings', 'ratio_validation'),
                   )
    npy_size = generate_dataset_config.getint('user_settings', 'npy_size')
    extract_stride = generate_dataset_config.getint('user_settings', 'extract_stride')
    atom_grid_radius = generate_dataset_config.getfloat('user_settings', 'atom_grid_radius')
    n_workers = generate_dataset_config.getint('user_settings', 'n_workers')
    label_maps(label_groups=label_groups,
               group_names=group_names,
               metadata_path=csv_path,
               raw_path=raw_path,
               temp_sample_path=temp_path, 
               sample_path=sample_path,
               ratio_t_t_v=ratio_t_t_v,
               npy_size=npy_size,
               extract_stride=extract_stride,
               atom_grid_radius=atom_grid_radius,
               n_workers=n_workers,
               )
    
    
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
    data_to_npy(normalized_map_path, model_path, label_groups, None, group_names, emdb_id, generate_test=True)


if __name__ == '__main__':
    label_groups = [[{'secondary_type': '', 'residue_type': ','.join(residues_protein), 'atom_type': 'CA', 'element_type': '', 'metal_type': '', 'label': 1},\
                   {'secondary_type': '', 'residue_type': ','.join(residues_protein), 'atom_type': 'C', 'element_type': '', 'metal_type': '', 'label': 2},\
                   {'secondary_type': '', 'residue_type': ','.join(residues_protein), 'atom_type': 'N', 'element_type': '', 'metal_type': '', 'label': 3}]]
    group_names = ['Back_Bone']
    query = "ribosome AND resolution:[1 TO 4}"
    main(query, label_groups, group_names)
    
    # run the following to generate test map
    # generate_test_label_maps(60537,'CryoDataBot_Data/Test_Maps', label_groups, group_names)
