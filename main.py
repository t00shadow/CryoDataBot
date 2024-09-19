import os

from atom_in_models import residues_protein
from downloading_and_preprocessing import download_and_preprocessing
from fetch_sample_info import search_emdb
from generate_dataset import label_maps


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

    csv_path = search_emdb(search_query, metadata_path, rows=3)

    download_and_preprocessing(csv_path, raw_path, overwrite=True)

    label_maps(label_groups,csv_path,raw_path,group_names, 
               temp_sample_path=temp_path, sample_path=sample_path)


if __name__ == '__main__':
    label_group = [[{'secondary_type': '', 'residue_type': ','.join(residues_protein), 'atom_type': 'CA', 'element_type': '', 'metal_type': '', 'label': 1},\
                   {'secondary_type': '', 'residue_type': ','.join(residues_protein), 'atom_type': 'C', 'element_type': '', 'metal_type': '', 'label': 2},\
                   {'secondary_type': '', 'residue_type': ','.join(residues_protein), 'atom_type': 'N', 'element_type': '', 'metal_type': '', 'label': 3}],
                   [{'secondary_type': '', 'residue_type': 'A,DA', 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 1},\
                   {'secondary_type': '', 'residue_type': 'U,DT', 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 2},\
                   {'secondary_type': '', 'residue_type': 'C,DC', 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 3},\
                   {'secondary_type': '', 'residue_type': 'G,DG', 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 4}],
                   [{'secondary_type': '', 'residue_type': residues_protein[0], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 1},\
                    {'secondary_type': '', 'residue_type': residues_protein[1], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 2},\
                    {'secondary_type': '', 'residue_type': residues_protein[2], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 3},\
                    {'secondary_type': '', 'residue_type': residues_protein[3], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 4},\
                    {'secondary_type': '', 'residue_type': residues_protein[4], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 5},\
                    {'secondary_type': '', 'residue_type': residues_protein[5], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 6},\
                    {'secondary_type': '', 'residue_type': residues_protein[6], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 7},\
                    {'secondary_type': '', 'residue_type': residues_protein[7], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 8},\
                    {'secondary_type': '', 'residue_type': residues_protein[8], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 9},\
                    {'secondary_type': '', 'residue_type': residues_protein[9], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 10},\
                    {'secondary_type': '', 'residue_type': residues_protein[10], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 11},\
                    {'secondary_type': '', 'residue_type': residues_protein[11], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 12},\
                    {'secondary_type': '', 'residue_type': residues_protein[12], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 13},\
                    {'secondary_type': '', 'residue_type': residues_protein[13], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 14},\
                    {'secondary_type': '', 'residue_type': residues_protein[14], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 15},\
                    {'secondary_type': '', 'residue_type': residues_protein[15], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 16},\
                    {'secondary_type': '', 'residue_type': residues_protein[16], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 17},\
                    {'secondary_type': '', 'residue_type': residues_protein[17], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 18},\
                    {'secondary_type': '', 'residue_type': residues_protein[18], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 19},\
                    {'secondary_type': '', 'residue_type': residues_protein[19], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 20},\
                    ]]
    group_names = ['Protein_Back_Bone','Nucleotides','Protein_Residues']
    query = "ribosome AND resolution:[1 TO 4}"
    main(query, label_group, group_names)
                            