import json
import os
import shutil

import numpy as np
import pandas as pd

from Utils_search_EMDB import search_emdb, search_rcsb
from Utils_preprocess import read_csv_info, fetch_map_model, normalize_raw_map
from Utils_generate_dataset import data_to_npy



csv_path = "path_of_downloaded_csv_file"
output_dir = "./"
query = "ribosome AND resolution: [1 TO 4}"
fetch_classification = False

def main(output_dir, csv_path):

    # Step 1. Read search queries for EMDB search, download the information and refine it
    # 1.1 Search EMDB and download the csv file
    path_list = search_emdb(query, csv_path)
    if fetch_classification:
        for i in range(len(path_list)):
            path = path_list[i]
            new_file_name = path[path.rfind('/') + 1:] - '.csv'
            search_rcsb(path, new_file_name+'_classified.csv')
    # 1.2 Refine entries in the csv file



if __name__ == "__main__":
    main(output_dir, csv_path)
