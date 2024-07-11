import json
import os
import shutil

import numpy as np
import pandas as pd

from Utils_search_EMDB import search_emdb, search_rcsb
from Utils_preprocess import read_csv_info, fetch_map_model, normalize_raw_map
from Utils_generate_dataset import data_to_npy



csv_path = "path_of_downloaded_csv_file"
output_dir = "path_of_output_dataset"
query = "ribosome"
fetch_classification = False

def main(output_dir, csv_path):

    # Step 1. Read search queries for EMDB search, download the information and refine it
    # 1.1 Search EMDB and download the csv file
    path_list = search_emdb(query,csv_path)
    if fetch_classification:
        for i in range(len(path_list)):
            path = path_list[i]
            new_file_name = path[path.rfind('/') + 1:] - '.csv'
            search_rcsb(path,new_file_name+'_classified.csv')
    # 1.2 Refine entries in the csv file
    


    # Step 2. Download map and model files and do preprocessing
    # 2.1 Read map list and generate raw_map and model downloading paths
    csv_info, raw_map_paths, model_paths = read_csv_info(csv_path)

    # 2.2 Download map and model files
    fetch_map_model(csv_info)

    # 2.3 Resample and normalize map files
    map_paths = normalize_raw_map(csv_info, raw_map_paths)

    # Step 3. Generate a dataset (3d numpy arraies) from map and model files
    # 3.1 Read model files and create lables
    
    # 3.2 Generate a dataset
    if MAP2NPY:

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

        # split data into training and testing dataset
        import splitfolders
        # sample_path = os.path.join(output_dir, "TEST_with_blank", "train_val_data")
        # sample_path = os.path.join(output_dir, "TEST_with_all", "train_val_data")
        sample_path = os.path.join(output_dir, "TEST_20240520",
                                   "train_val_data")

        os.makedirs(sample_path, exist_ok=True)
        splitfolders.ratio(input=temp_sample_path,
                           output=sample_path,
                           seed=44,
                           ratio=(.8, .2),
                           group_prefix=None,
                           move=True)
        shutil.rmtree(temp_sample_path)

        # Calculate weight, create weight file and save it (ratio of tags)
        weight_path = os.path.join(sample_path,
                                   'class_weight_for_training.txt')
        with open(weight_path, "w") as file:
            json.dump(ratio_of_tag, file)


if __name__ == "__main__":
    main(output_dir, csv_path)
