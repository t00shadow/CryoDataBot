import json
import os
import shutil

import numpy as np
# import pandas as pd

from Utils_search_EMDB import search_emdb, refine_csv
from Utils_preprocess import read_csv_info, fetch_map_model, normalize_raw_map
from Utils_generate_dataset import data_to_npy, splitfolders


temp_sample_path = "path_of_downloaded_temp_sample"  # we set a default path
csv_download_path = "directory_for_downloading_csv_file"  # we set a default path

output_dir = "path_of_output_dataset"  # user input for path of all datasets
query = "ribosome"  # user input for EMDB search
fetch_bool = False  # user input for RCSB search
MODEL_PARTS = ["a", "b", "c", ...]  # user input as datastes' name


def main(output_dir, csv_download_path):

    # Step 1. Read search queries for EMDB search, download the information and refine it
    # 1.1 Search EMDB and download the csv file
    csv_path = search_emdb(query, csv_download_path, fetch_classification=fetch_bool)

    # 1.2 Refine entries in the csv file
    refine_csv(csv_path, output_dir, threshold=100)

    # Step 2. Download map and model files and do preprocessing
    # 2.1 Read map list and generate raw_map and model downloading paths
    csv_info, raw_map_paths, model_paths = read_csv_info(csv_path)
    emdbs, pdbs, resolutions, emdb_ids = csv_info

    # 2.2 Download map and model files
    fetch_map_model(csv_info)

    # 2.3 Resample and normalize map files
    map_paths = normalize_raw_map(csv_info, raw_map_paths)


    # Step 3. Generate a dataset (3d numpy arraies) from map and model files
    # 3.1 Read map, model files and create lables
    # idx of npy file
    sample_num = 0

    # num of tag in each part for all models
    num_of_tag_in_each_part_for_all_models = {}
    for part in MODEL_PARTS:
        num_of_tag_in_each_part_for_all_models[part] = 0

    for idx, emdb_id in enumerate(emdb_ids):
        # test for idx in [0,1]
        # for idx, emdb_id in enumerate(emdb_ids[0:1]):
        print(
            f"[{idx+1}/{len(emdb_ids)}] Generating dataset from EMDB-{emdb_id}... "
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







    # 3.3 Split data into training and validation dataset
    sample_path = os.path.join(output_dir, "dataset")
    splitfolders(temp_sample_path, sample_path)

    # 3.4 Calculate weight, create weight file and save it (ratio of tags)
    weight_path = os.path.join(sample_path, 'class_weight_for_training.txt')
    with open(weight_path, "w") as file:
        json.dump(ratio_of_tag, file)


if __name__ == "__main__":
    main(output_dir, csv_path)
