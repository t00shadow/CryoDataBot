from downloading_and_preprocessing import map_normalizing, map_output
from generate_dataset_lockfree import data_to_npy

# normalize = False
normalize = True
# raw_map_path = "Testing_Files/EMD_10769/emd_10769.map"
# raw_map_path = r"C:\Users\noelu\CryoDataBot\Testing_Files\EMD_10769\emd_10769.map"
#raw_map_path = "Testing_Files/EMD_23501/emd_23501.map"
raw_map_path = r"C:\Users\noelu\CryoDataBot\Testing_Files\EMD_23501\emd_23501.map"
# model_paths = "Testing_Files/EMD_10769/6ybd.cif"
# model_paths = r"C:\Users\noelu\CryoDataBot\Testing_Files\EMD_10769\6ybd.cif"
#model_paths = "Testing_Files/EMD_23501/7ls2.cif"
model_paths = r"C:\Users\noelu\CryoDataBot\Testing_Files\EMD_23501\7ls2.cif"
recl = 0.015
#recl = 4.0

if normalize:
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
    # map_F, origin_info, _ = map_normalizing(raw_map_path, recl)

    map_path = f"{raw_map_path.split('.map')[0]}_normalized.mrc"
    map_output(raw_map_path, map_F, map_path, is_model=False)
    print(f'Normalized Map Saved as "{map_path}"')

map_path = f"{raw_map_path.split('.map')[0]}_normalized.mrc"
group_names = ['secondary_strctures', 'residue_types', 'key_atoms']
from atom_in_models import atoms_sugar_ring, residues_RNA, residues_protein
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

data_to_npy(map_path, model_paths, label_groups, None, group_names, None, generate_test=True)