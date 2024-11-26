import os
from collections import namedtuple
from configparser import ConfigParser
import json

from backend_core import *
from cmd_parser import parse_cmd


def main()->None:
    parser = parse_cmd()
    args = parser.parse_args()

    if args.mode == 'functions' or args.mode == 'f':
        run_funcs(args.file, args.run)
    elif args.mode == 'default' or args.mode == 'd':
        pass


def run_funcs(file_path: str,
              run_what: str,
              ):
    # required arguments for each function
    pipeline_req = ['query', 'file_name']
    fetch_req = ['query', 'file_name']
    filter_req = ['csv_path']
    preprocess_req = ['csv_path']
    label_req = ['csv_path', 'label_groups', 'group_names']
    test_req = ['emdb_id', 'label_groups', 'group_names']
    setting = f'{run_what}_inputs'

    # path settings
    path_info = create_path()
    metadata_path = path_info.metadata_path
    raw_path = path_info.raw_path
    sample_path = path_info.sample_path
    temp_path = path_info.temp_path

    if run_what == 'pipeline':
        params = extract_params(file_path,
                                setting,
                                *pipeline_req)
        run_pipeline(search_query=params['query'],
                     file_name=params['file_name'],
                     label_groups=params['label_groups'],
                     group_names=params['group_names'],
                     path_info=path_info,
                     )
    elif run_what == 'fetch':
        params = extract_params(file_path,
                                setting,
                                *fetch_req)
        fetch_sample_info_config = ConfigParser(default_section='directories')
        fetch_sample_info_config.read(os.path.join('backend_helpers','CryoDataBotConfig.ini'))
        fetch_qscore = fetch_sample_info_config.getboolean('user_settings', 'fetch_qscore')
        fetch_classification = fetch_sample_info_config.getboolean('user_settings', 'fetch_classification')
        rows = fetch_sample_info_config.getint('user_settings', 'rows')
        search_emdb(query=params['query'],
                    file_name=params['file_name'],
                    save_path=metadata_path,
                    fetch_qscore=fetch_qscore,
                    fetch_classification=fetch_classification, 
                    rows=rows,
                    )
    elif run_what == 'filter':
        params = extract_params(file_path,
                                setting, 
                                *filter_req)
        redundancy_filter_config = ConfigParser(default_section='redundancy_filter')
        redundancy_filter_config.read(os.path.join('backend_helpers','CryoDataBotConfig.ini'))
        q_threshold = redundancy_filter_config.getfloat('user_settings', 'q_threshold')
        uni_threshold = redundancy_filter_config.getfloat('user_settings', 'uni_threshold')
        filter_csv(input_csv=params['csv_path'], 
                   q_threshold=q_threshold, 
                   uni_threshold=uni_threshold, 
                   )
    elif run_what == 'preprocess':
        params = extract_params(file_path,
                                setting, 
                                *preprocess_req)
        downloading_and_preprocessing_config = ConfigParser(default_section='downloading_and_preprocessing')
        downloading_and_preprocessing_config.read(os.path.join('backend_helpers','CryoDataBotConfig.ini'))
        overwrite = downloading_and_preprocessing_config.getboolean('user_settings', 'overwrite')
        give_map = downloading_and_preprocessing_config.getboolean('user_settings', 'give_map')
        protein_tag_dist = downloading_and_preprocessing_config.getint('user_settings', 'protein_tag_dist')
        map_threashold = downloading_and_preprocessing_config.getfloat('user_settings', 'map_threashold')
        vof_threashold = downloading_and_preprocessing_config.getfloat('user_settings', 'vof_threashold')
        dice_threashold = downloading_and_preprocessing_config.getfloat('user_settings', 'dice_threashold')
        downloading_and_preprocessing(matadata_path=params['csv_path'], 
                                    raw_dir=raw_path, 
                                    overwrite=overwrite,
                                    give_map=give_map,
                                    protein_tag_dist=protein_tag_dist,
                                    map_threashold=map_threashold,
                                    vof_threashold=vof_threashold,
                                    dice_threashold=dice_threashold,
                                    )
    elif run_what == 'label':
        params = extract_params(file_path,
                                setting, 
                                *label_req)
        generate_dataset_config = ConfigParser(default_section='generate_dataset')
        generate_dataset_config.read(os.path.join('backend_helpers','CryoDataBotConfig.ini'))
        ratio_t_t_v = (generate_dataset_config.getfloat('user_settings', 'ratio_training'),
                    generate_dataset_config.getfloat('user_settings', 'ratio_testing'),
                    generate_dataset_config.getfloat('user_settings', 'ratio_validation'),
                    )
        npy_size = generate_dataset_config.getint('user_settings', 'npy_size')
        extract_stride = generate_dataset_config.getint('user_settings', 'extract_stride')
        atom_grid_radius = generate_dataset_config.getfloat('user_settings', 'atom_grid_radius')
        n_workers = generate_dataset_config.getint('user_settings', 'n_workers')
        label_maps(label_groups=params['label_groups'],
                group_names=params['group_names'],
                metadata_path=params['csv_path'],
                raw_path=raw_path,
                temp_sample_path=temp_path, 
                sample_path=sample_path,
                ratio_t_t_v=ratio_t_t_v,
                npy_size=npy_size,
                extract_stride=extract_stride,
                atom_grid_radius=atom_grid_radius,
                n_workers=n_workers,
                )
    elif run_what == 'test':
        params = extract_params(file_path,
                                setting, 
                                *test_req)


def extract_params(file_path: str,
                   setting: str,
                   *args,
                   )->dict:
    params = {}
    with open(file_path, 'r') as f:
        input = json.loads(f)
        for arg in args:
            try:
                params[arg] = input[setting][arg]
            except KeyError:
                print(f'Error: Required Argument {arg} Not Found in "{file_path}"')

    return params



def create_path()->namedtuple:
    # read path info from config file
    dir_config = ConfigParser(default_section='directories')
    dir_config.read(os.path.join('backend_helpers','CryoDataBotConfig.ini'))
    cryo_data_bot_data_path = dir_config.get('directories', 'cryo_data_bot_data_path')
    metadata_path = dir_config.get('directories','metadata_path')
    raw_path = dir_config.get('directories', 'raw_path')
    sample_path = dir_config.get('directories','sample_path')
    temp_path = dir_config.get('directories', 'temp_path')
    
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

    path_info = namedtuple('path_info', ['metadata_path', 'raw_path','sample_path', 'temp_path'])
    path_info.metadata_path = metadata_path
    path_info.raw_path = raw_path
    path_info.sample_path = sample_path
    path_info.temp_path = temp_path

    return path_info


