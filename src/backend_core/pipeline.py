import os
from collections import namedtuple
from configparser import ConfigParser

from .download_preprocess_maps import downloading_and_preprocessing
from .fetch_sample_info import search_emdb
from .generate_dataset import label_maps
from .redundancy_filter import filter_csv


def run_pipeline(
        search_query: str,
        label_groups: list[dict[str: str|int]],
        group_names: list[str],
        path_info: namedtuple,
        file_name: str=None,
        ) -> None:   
    # set paths
    metadata_path = path_info.metadata_path
    raw_path = path_info.raw_path
    sample_path = path_info.sample_path
    temp_path = path_info.temp_path

    # download EMDB csv file
    # from config file read default values
    fetch_sample_info_config = ConfigParser(default_section='directories')
    fetch_sample_info_config.read(os.path.join('backend_helpers','CryoDataBotConfig.ini'))
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
    redundancy_filter_config.read(os.path.join('backend_helpers','CryoDataBotConfig.ini'))
    q_threshold = redundancy_filter_config.getfloat('user_settings', 'q_threshold')
    uni_threshold = redundancy_filter_config.getfloat('user_settings', 'uni_threshold')
    csv_path = filter_csv(input_csv=csv_path, 
                          q_threshold=q_threshold, 
                          uni_threshold=uni_threshold, 
                          )

    # download and preprocess raw data
    # from config file read default values
    downloading_and_preprocessing_config = ConfigParser(default_section='downloading_and_preprocessing')
    downloading_and_preprocessing_config.read(os.path.join('backend_helpers','CryoDataBotConfig.ini'))
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
    generate_dataset_config.read(os.path.join('backend_helpers','CryoDataBotConfig.ini'))
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