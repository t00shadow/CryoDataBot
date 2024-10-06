import os

from atom_in_models import residues_protein
from downloading_and_preprocessing import download_and_preprocessing
from fetch_sample_info import search_emdb
from generate_dataset import label_maps
from redundancy_filter import refine_csv


def main(
        search_query: str,
        label_groups,
        group_names: list[str],
        cryo_data_bot_path: str='CryoDataBot',
        metadata_path: str='Metadata',
        raw_path: str='Raw',
) -> None:   
    # create directories if not exist
    os.makedirs(cryo_data_bot_path, exist_ok=True)
    metadata_path = os.path.join(cryo_data_bot_path, metadata_path)
    os.makedirs(metadata_path, exist_ok=True)
    raw_path = os.path.join(cryo_data_bot_path, raw_path)
    os.makedirs(raw_path, exist_ok=True)
    sample_path = os.path.join(cryo_data_bot_path, 'Sample')
    temp_path = os.path.join(cryo_data_bot_path, 'Temp')

    # download EMDB csv file
    csv_path = search_emdb(search_query, metadata_path, rows=10, fetch_classification=True)

    # refine csv file
    csv_path = refine_csv(input_csv=csv_path, q_threshold=0.1, uni_threshold=0.5)

    # download and preprocess raw data
    download_and_preprocessing(csv_path, raw_path, overwrite=False)

    # label maps
    label_maps(label_groups,csv_path,raw_path,group_names, 
               temp_sample_path=temp_path, sample_path=sample_path)


if __name__ == '__main__':
    label_group = [[{'secondary_type': '', 'residue_type': ','.join(residues_protein), 'atom_type': 'CA', 'element_type': '', 'metal_type': '', 'label': 1},\
                   {'secondary_type': '', 'residue_type': ','.join(residues_protein), 'atom_type': 'C', 'element_type': '', 'metal_type': '', 'label': 2},\
                   {'secondary_type': '', 'residue_type': ','.join(residues_protein), 'atom_type': 'N', 'element_type': '', 'metal_type': '', 'label': 3}]]
    group_names = ['Back_Bone']
    query = "ribosome AND resolution:[1 TO 4}"
    main(query, label_group, group_names)
                            