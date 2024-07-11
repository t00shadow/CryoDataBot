import os
import shutil
import subprocess
import requests
import mrcfile
import numpy as np
import pandas as pd
from scipy.ndimage import zoom
import urllib.request
import gzip
import shutil


DATA_PATH = "dddd"


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
def fetch_map_model(csv_info, raw_map_paths, model_paths):
    emdbs, pdbs, _, emdb_ids = csv_info
    for idx, emdb in enumerate(emdbs):
        pdb = pdbs[idx]
        emdb_id = emdb_ids[idx]
        raw_map_path = raw_map_paths[idx]
        model_path = model_paths[idx]

        directory1 = os.path.dirname(raw_map_path)
        os.makedirs(directory1, exist_ok=True)

        emdb_fetch_link = f"https://ftp.ebi.ac.uk/pub/databases/emdb/structures/{emdb}/map/emd_{emdb_id}.map.gz"
        pdb_fetch_link = f"http://files.rcsb.org/download/{pdb}.cif"

        raw_map_gz_path = f"{raw_map_path}.gz"

        if not os.path.exists(raw_map_path):
            urllib.request.urlretrieve(emdb_fetch_link, raw_map_gz_path)
            with gzip.open(raw_map_gz_path, 'rb') as f_in:
                with open(raw_map_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            os.remove(raw_map_gz_path)

        if not os.path.exists(model_path):
            urllib.request.urlretrieve(pdb_fetch_link, model_path)
            print(f"=> {emdb} and pdb-{pdb} files are downloaded.")

    # if os.path.exists(f"{directory1}/emd_{emdb_id}.map"):
    #     pass
    # else:
    #     subprocess.run(["wget", "-P", directory1, emdb_fetch_link])
    #     subprocess.run(["gzip", "-d", f"{directory1}/emd_{emdb_id}.map.gz"])
    # if os.path.exists(f"{directory1}/{pdb}.cif"):
    #     pass
    # else:
    #     subprocess.run(["wget", "-P", directory1, pdb_fetch_link])
    #     print(f"=> {emdb} and pdb-{pdb} files are downloaded.")


# 1.3 Resampl and normalize map files
def normalize_raw_map(raw_map_paths):
    """
    return:
        normalized map paths
    """
    map_paths = [
        f"{raw_map_path.split('.map')[0]}_normalized.mrc"
        for raw_map_path in raw_map_paths
        ]
    for idx, map_path in enumerate(map_paths):
        if not os.path.exists(map_path):
            map_data = map_normalizing(raw_map_paths[idx])
            map_output(raw_map_paths[idx], map_data, map_path, is_model=False)

    return map_paths


def map_normalizing(map_path):
    with mrcfile.mmap(map_path) as mrc:
        # Load map data
        map_data = np.array(mrc.data, dtype=np.float32)

        # Resample map to 1.0A*1.0A*1.0A grid size
        zoom_factors = [mrc.voxel_size.z, mrc.voxel_size.y, mrc.voxel_size.x]
        map_data = zoom(map_data, zoom_factors)

        # Normalize map values to the range (0.0, 1.0)
        data_99_9 = np.percentile(map_data, 99.9)
        if data_99_9 == 0.:
            print('data_99_9 == 0!!')
            raise ValueError('99.9th percentile of map data is zero')
        map_data /= data_99_9
        map_data = np.clip(map_data, 0., 1.)

        if mrc.header.nzstart != 0 or mrc.header.nystart != 0 or mrc.header.nxstart != 0:
            print('The start of axis is not 0!!')
            raise ValueError('The start of axis is not zero!')

    return map_data


def map_output(input_map, map_data, output_map, is_model=False):
    if os.path.exists(output_map):
        os.remove(output_map)

    print(f"=> Writing new map to {output_map}")
    shutil.copyfile(input_map, output_map)
    with mrcfile.open(output_map, mode='r+') as mrc:
        if is_model:
            map_data = map_data.astype(np.int8)
        else:
            map_data = map_data.astype(np.float32)

        mrc.set_data(map_data)
        mrc.header.mz = map_data.shape[0]
        mrc.header.ispg = 1  #401
        mrc.print_header()
        print("=> New map written successfully.")


def search_emdb(query, file_names=None, fl='emdb_id,title,resolution,fitted_pdbs,xref_UNIPROTKB,xref_ALPHAFOLD', rows=None):
    """
    # Inputs:
    # query(required): a string list of search queries
    # Example: ['structure_determination_method:"singleParticle"', 'Human Albumin']
    # The query can also be composed by multiple search terms concatened by AND or OR terms
    # Example: ['sample_type:"virus" and resolution [* TO 3]']

    # file_names(optional): a string list of desired file names
    # Example: 'Ribosome'
    # Default: 'download_file_0'

    # fl(optional): list of fields to be shown in the csv file; each item is separated by ','
    # Example: 'emdb_id,resolution,fitted_pdbs'
    # Default: 'emdb_id,title,resolution,fitted_pdbs,xref_UNIPROTKB,xref_ALPHAFOLD'

    # rows(optional): a list of int (how many entries to include in each file)
    # Example: [1000, 500]
    # Default: 100

    # Output(s):
    # csv file(s) with the user provided file names
    """
    url = 'https://www.ebi.ac.uk/emdb/api/search/'
    if file_names is None:
        for i in range(len(query)):
            output = ''
            try:
                if rows is None:
                    payload = {'rows': 100, 'fl': fl}
                elif len(rows) == len(query):
                    payload = {'rows': rows[i], 'fl': fl}
                else:
                    print('The length of query, file_names, and rows must match!')
                    return
                r = requests.get(url+query[i], params=payload, headers={'accept': 'text/csv'})
                if r.status_code == 200:
                    output += r.text
                else:
                    print(f"Error fetching data query: {query[i]}. Unexpected error.")
            except requests.exceptions.RequestException as e:
                print(f"Error fetching data: {e}")

            file_name = f'download_file_{i}' + '.csv'
            with open(file_name, 'w') as out:
                out.write(output)
                count = output.count('\n')-1
                if rows is None:
                    if count< 100:
                        print(f"Number of entries is less than 100. Entries fetched: {count}.")
                else:
                    if count < rows[i]:
                        print(f"Number of entries is less than {rows[i]}. Entries fetched: {count}.")
                print(f'File wrote: {file_name}')
    elif len(query) == len(file_names):
        for i in range(len(query)):
            output = ''
            try:
                if rows is None:
                    payload = {'rows': 100, 'fl': fl}
                elif len(rows) == len(query):
                    payload = {'rows': rows[i], 'fl': fl}
                else:
                    print('Error: the length of query, file_names, and rows must match!')
                    return
                r = requests.get(url+query[i], params=payload, headers={'accept': 'text/csv'})
                if r.status_code == 200:
                    output += r.text
                else:
                    print(f"Error fetching data query: {query[i]}. Unexpected error.")
            except requests.exceptions.RequestException as e:
                print(f"Error fetching data: {e}")

            file_name = file_names[i] + '.csv'
            with open(file_name, 'w') as out:
                out.write(output)
                count = output.count('\n') - 1
                if rows is None:
                    if count < 100:
                        print(f"Number of entries is less than 100. Entries fetched: {count}.")
                else:
                    if count < rows[i]:
                        print(f"Number of entries is less than {rows[i]}. Entries fetched: {count}.")
                print(f'File wrote: {file_name}')
    else:
        print('Error: the length of query and file_names must match!')
    pass


def search_rcsb(file_path, save_path):
    """
    :param file_path: path to .csv file
    :param save_path: path to save directory
    :return: .csv file with classification and classification description for each entry
    """
    df = pd.read_csv(file_path)
    url = 'https://data.rcsb.org/rest/v1/core/entry/'
    classification = []
    classification_des = []
    for i in range(len(df['fitted_pdbs'])):
        pdb_id = df['fitted_pdbs'][i]
        r = requests.get(url + pdb_id)
        file = r.json()
        classification.append(file["struct_keywords"]["pdbx_keywords"])
        classification_des.append(file["struct_keywords"]["text"])
    df["RCSB_classification"] = classification
    df["RCSB_description"] = classification_des
    df.to_csv(save_path, index=False)