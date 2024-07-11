import json
import os
import shutil
import splitfolders

import numpy as np
import pandas as pd
from B1_UTILS import download_map_model, map_normalizing, map_output
from B2_UTILS_data2npy import data_to_npy

# Step 1. Download map and model files and do preprocessing

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
def fetch_map_model(csv_info):
    emdbs, pdbs, resolutions, emdb_ids = csv_info
    for idx, _ in enumerate(emdb_ids):
        download_map_model(emdb=emdbs[idx],
                            pdb=pdbs[idx],
                            resolution=resolutions[idx],
                            directory=DATA_PATH)

# 1.3 Resampl and normalize map files
def normalized_raw_map(csv_info, path_info):
    """
    return:
        updated_path_info: raw_map, model, and normalized map paths
    """
    _, _, _, emdb_ids = csv_info
    raw_map_paths, _ = path_info
    map_paths = [
        f"{raw_map_path.split('.map')[0]}_normalized.mrc"
        for raw_map_path in raw_map_paths
    ]
    for idx, _ in enumerate(emdb_ids):
        if not os.path.exists(map_paths[idx]):
                map_data = map_normalizing(raw_map_paths[idx])
                map_output(raw_map_paths[idx],
                        map_data,
                        map_paths[idx],
                        is_model=False)
    updated_path_info = path_info.append(map_paths)
    return updated_path_info
                
# Step 2. Generate dataset (3d numpy arraies) from map and model files
def data_set_generation(csv_info,path_info):
    _, _, _, emdb_ids = csv_info
    _, model_paths, map_paths = path_info
    # idx of npy file
    sample_num = 0

    # num of tag in each part for all models
    num_of_tag_in_each_part_for_all_models = {}
    for part in MODEL_PARTS:
        num_of_tag_in_each_part_for_all_models[part] = 0

    num_entries = len(emdb_ids)
    for idx, emdb_id in enumerate(emdb_ids):
        # test for idx in [0,1]
        # for idx, emdb_id in enumerate(emdb_ids[0:1]):
        print(
            f"[{idx+1}/{num_entries}] Generating dataset from EMDB-{emdb_id}... "
        )
        sample_num, num_of_tag_in_each_part = data_to_npy(
            map_paths[idx], model_paths[idx], MODEL_PARTS,
            temp_sample_path, sample_num)
        # Add number of each tag in new sampled model
        for key, value_list in num_of_tag_in_each_part.items():
            num_of_tag_in_each_part_for_all_models[key] += value_list

    # Delete 0s in tag number list and calculate 1/ratio of tag number
    ratio_of_tag = {}
    for key, value_list in num_of_tag_in_each_part_for_all_models.items():
        value_list = np.trim_zeros(value_list)
        num_of_tag_in_each_part_for_all_models[key] = value_list
        if 0 in value_list:
            print(
                f'There is missing groups in part {key}, numbers of each class are {value_list}.'
            )
        ratio_of_tag[key] = [
            int(value_list[0] // value_x) for value_x in value_list
            if value_x != 0
        ]
    
    # Print statistical results
    print(f"The number of .npy file: {sample_num}")
    print("Num of each tag: ")
    for key, value in num_of_tag_in_each_part_for_all_models.items():
        print(f'{key}: {value}')
    print("\nRatio of tags: ")
    for key, value in ratio_of_tag.items():
        print(f'{key}: {value}')

    # split data
    split_data(output_dir)
    # Calculate weight, create weight file and save it (ratio of tags)
    weight_path = os.path.join(output_dir,
                                'class_weight_for_training.txt')
    with open(weight_path, "w") as file:
        json.dump(ratio_of_tag, file)

# Step 3. split data into training, testing, and validation dataset
def split_data(output_dir):
    sample_path = os.path.join(output_dir, 'training', 'testing', 'validation')
    os.makedirs(sample_path, exist_ok=True)
    splitfolders.ratio(input=temp_sample_path,
                        output=output_dir,
                        seed=44,
                        ratio=(.8, .1, .1),
                        group_prefix=None,
                        move=True)
    shutil.rmtree(temp_sample_path)

if __name__ == "__main__":
    output_dir = "PATH1" 
    csv_path = "PATH2"
    temp_sample_path = ''
    DATA_PATH = ""
    MODEL_PARTS = ['secondary_strctures', 'key_atoms', 'residue_types']    
    csv_info, path_info = read_csv_info(csv_path)
    fetch_map_model(csv_info)
    updated_path_info = normalized_raw_map(csv_info, path_info)
    data_set_generation(csv_info,updated_path_info)