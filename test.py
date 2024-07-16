import json
import os
import shutil

import numpy as np
import pandas as pd

from Utils_search_EMDB import search_emdb, get_emdb_validation_data, get_average_qscores, write_qscores_to_csv, append_qscores_to_csv
from Utils_preprocess import read_csv_info, fetch_map_model, normalize_raw_map
from Utils_generate_dataset import data_to_npy


output_dir = "path_of_output_dataset"

query = 'ribosome AND sample_type:"complex" AND resolution:[5 TO 10}'
csv_path = "./"
fetch_bool = True


search_emdb(query, save_directory=csv_path, fetch_classification=fetch_bool)
