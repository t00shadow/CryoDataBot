import json
import os
import shutil

import numpy as np
# import pandas as pd

from backup.Utils_search_EMDB import search_emdb, refine_csv
from Utils_preprocess import read_csv_info, fetch_map_model, normalize_raw_map
from Utils_generate_dataset import data_to_npy, splitfolders


output_dir = "path_of_output_dataset"

query = 'ribosome AND resolution:[5 TO 10}'
csv_download_path = "./"
fetch_bool = False


# csv_path = search_emdb(query, save_path=csv_download_path, fetch_classification=fetch_bool)

csv_path = '/home/qiboxu/MyProject/CryoDataBot/download_file_01_review.csv'
kept_path, filtered_path = refine_csv(csv_path, csv_download_path, 100, .4)