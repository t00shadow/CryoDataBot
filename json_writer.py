import json

pipeline_inputs = {
    'query':'ribosome AND resolution:[1 TO 4}',
    'file_name':'ribosome_res_1-4',
}

fetch_inputs = {
    'query':'ribosome AND resolution:[1 TO 4}',
    'file_name':'ribosome_res_1-4',
}

filter_inputs = {
    'csv_path':'CryoDataBot_Data/Metadata/ribosome_res_1-4_001/ribosome_res_1-4_001.csv'
}

preprocess_inputs = {
    'csv_path':'CryoDataBot_Data/Metadata/ribosome_res_1-4_001/ribosome_res_1-4_001_Final.csv',
}

group_names = ['secondary_strctures', 'residue_types', 'key_atoms']
from src.backend_core.backend_helpers.atom_in_models import atoms_sugar_ring, residues_RNA, residues_protein
label_groups = [
                [{'secondary_type': 'Helix', 'residue_type': '', 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 1},
                {'secondary_type': 'Sheet', 'residue_type': '', 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 2},
                {'secondary_type': 'Loop', 'residue_type': '', 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 3},
                {'secondary_type': '', 'residue_type': ','.join(residues_RNA), 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 4}],
                
                [{'secondary_type': '', 'residue_type': residues_protein[0], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 1},
                {'secondary_type': '', 'residue_type': residues_protein[1], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 2},
                {'secondary_type': '', 'residue_type': residues_protein[2], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 3},
                {'secondary_type': '', 'residue_type': residues_protein[3], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 4},
                {'secondary_type': '', 'residue_type': residues_protein[4], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 5},
                {'secondary_type': '', 'residue_type': residues_protein[5], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 6},
                {'secondary_type': '', 'residue_type': residues_protein[6], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 7},
                {'secondary_type': '', 'residue_type': residues_protein[7], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 8},
                {'secondary_type': '', 'residue_type': residues_protein[8], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 9},
                {'secondary_type': '', 'residue_type': residues_protein[9], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 10},
                {'secondary_type': '', 'residue_type': residues_protein[10], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 11},
                {'secondary_type': '', 'residue_type': residues_protein[11], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 12},
                {'secondary_type': '', 'residue_type': residues_protein[12], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 13},
                {'secondary_type': '', 'residue_type': residues_protein[13], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 14},
                {'secondary_type': '', 'residue_type': residues_protein[14], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 15},
                {'secondary_type': '', 'residue_type': residues_protein[15], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 16},
                {'secondary_type': '', 'residue_type': residues_protein[16], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 17},
                {'secondary_type': '', 'residue_type': residues_protein[17], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 18},
                {'secondary_type': '', 'residue_type': residues_protein[18], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 19},
                {'secondary_type': '', 'residue_type': residues_protein[19], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 20},
                {'secondary_type': '', 'residue_type': residues_RNA[0], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 21},
                {'secondary_type': '', 'residue_type': residues_RNA[1], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 22},
                {'secondary_type': '', 'residue_type': residues_RNA[2], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 23},
                {'secondary_type': '', 'residue_type': residues_RNA[3], 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 24}],

                [{'secondary_type': '', 'residue_type': '', 'atom_type': 'CA', 'element_type': '', 'metal_type': '', 'label': 1},
                {'secondary_type': '', 'residue_type': '', 'atom_type': '', 'element_type': 'P', 'metal_type': '', 'label': 2},
                {'secondary_type': '', 'residue_type': '', 'atom_type': ','.join(atoms_sugar_ring), 'element_type': '', 'metal_type': '', 'label': 3},],
                ]

label_inputs = {
    'csv_path':'CryoDataBot_Data/Metadata/ribosome_res_1-4_001/ribosome_res_1-4_001_Final.csv',
    'label_groups':label_groups,
    'group_names':group_names,
}

test_inputs = {
    'emdb_id':'12345',
    'label_groups':label_groups,
    'group_names':group_names,
}

inputs = {'pipeline_inputs':pipeline_inputs,
         'fetch_inputs':fetch_inputs,
         'filter_inputs':filter_inputs,
         'preprocess_inputs':preprocess_inputs,
         'label_inputs':label_inputs,
         'test_inputs':test_inputs,
}


with open('input.json', 'w') as f:
    f.write(json.dumps(inputs, indent=4))