import os

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
    csv_path = search_emdb(search_query, metadata_path, rows=20, fetch_classification=False)

    # filter csv file
    csv_path = filter_csv(input_csv=csv_path, q_threshold=0.1, uni_threshold=0.5)

    # download and preprocess raw data
    downloading_and_preprocessing(csv_path, raw_path, overwrite=True)

    # label maps and split dataset
    label_maps(label_groups,csv_path,raw_path,group_names, 
            temp_sample_path=temp_path, sample_path=sample_path)
    
    
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
    map_F, map_orientation = map_normalizing(raw_map_path, recl)
    mapc, mapr, maps = map_orientation
    if not (mapc == 1 and mapr == 2 and maps == 3):
        if mapc == 1 and mapr == 3 and maps == 2:
            map_F = map_F.swapaxes(1, 2)
        elif mapc == 2 and mapr == 1 and maps == 3:
            map_F = map_F.swapaxes(0, 1)
        elif mapc == 2 and mapr == 3 and maps == 1:
            map_F = map_F.swapaxes(1, 2)
            map_F = map_F.swapaxes(0, 1)
        elif mapc == 3 and mapr == 1 and maps == 2:
            map_F = map_F.swapaxes(0, 1)
            map_F = map_F.swapaxes(1, 2)
        elif mapc == 3 and mapr == 2 and maps == 1:
            map_F = map_F.swapaxes(0, 2)

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
