# list_of_lists_of_dicts.py

def create_list_of_lists_of_dicts(group_name, secondary, residue, atom, element, metal):
    """Create and return a list of lists of dictionaries."""
    list_of_lists_of_dicts = [
        [
            "Group 1",
            {'secondary_type': 'Helix', 'residue_type': 'ALA', 'atom_type': 'CA', 'element_type': '', 'metal_type': '', 'label': 1},
            {'secondary_type': 'Helix', 'residue_type': 'ALA', 'atom_type': 'N', 'element_type': '', 'metal_type': '', 'label': 2},
            {'secondary_type': '', 'residue_type': 'ALA', 'atom_type': 'CA', 'element_type': '', 'metal_type': '', 'label': 3},
            {'secondary_type': 'Loop', 'residue_type': '', 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 4},
            {'secondary_type': 'Sheet', 'residue_type': '', 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 5},
            {'secondary_type': 'Sheet,Helix', 'residue_type': 'ALA', 'atom_type': 'CA', 'element_type': '', 'metal_type': '', 'label': 6},
            {'secondary_type': '', 'residue_type': 'A,C,G,U,DA,DC,DG,DT', 'atom_type': '', 'element_type': 'N', 'metal_type': '', 'label': 7},
            {'secondary_type': '', 'residue_type': '', 'atom_type': '', 'element_type': '', 'metal_type': 'Mg', 'label': 8}
        ],
        [
            "Group 2",
            {'secondary_type': 'Helix', 'residue_type': '', 'atom_type': '', 'element_type': 'P', 'metal_type': '', 'label': 1},
            {'secondary_type': 'Sheet', 'residue_type': '', 'atom_type': '', 'element_type': 'P', 'metal_type': '', 'label': 2},
            {'secondary_type': 'Loop', 'residue_type': '', 'atom_type': '', 'element_type': 'P', 'metal_type': '', 'label': 3}
        ],
        [
            group_name,
            {'secondary_type': '', 'residue_type': '', 'atom_type': '', 'element_type': '', 'metal_type': '', 'label': 0},
            {"name": "Eve", "age": 22, "message": "this is just to show u can put anything"},
            {'secondary_type': secondary, 'residue_type': residue, 'atom_type': atom, 'element_type': element, 'metal_type': metal, 'label': "uh automate this later"}
        ],
        [
            "Group 4",
            {'secondary_type': 'Helix', 'residue_type': '', 'atom_type': '', 'element_type': 'O', 'metal_type': '', 'label': 1},
            {'secondary_type': 'Sheet', 'residue_type': '', 'atom_type': '', 'element_type': 'O', 'metal_type': '', 'label': 2},
            {'secondary_type': 'Loop', 'residue_type': '', 'atom_type': '', 'element_type': 'O', 'metal_type': '', 'label': 3}
        ]
    ]
    return list_of_lists_of_dicts

def print_list_of_lists_of_dicts(list_of_lists_of_dicts):
    """Print the list of lists of dictionaries."""
    for i, inner_list in enumerate(list_of_lists_of_dicts):
        print(f"Group {i+1}:")
        for item in inner_list:
            print(f"  {item}")

def main():
    # Create the list of lists of dictionaries
    list_of_lists_of_dicts = create_list_of_lists_of_dicts("hooganooga", "protein-helix", "ALA, GLY", ["dang", "you", "can", "put lists as values"], "all", 'none')
    
    # Print the list of lists of dictionaries
    print_list_of_lists_of_dicts(list_of_lists_of_dicts)

    print("divider")
    # print(list_of_lists_of_dicts[0])
    print(list_of_lists_of_dicts[0][0]) 
    print(list_of_lists_of_dicts[0][1])    # first index is group number/index. second index is label number/index within respective group
    print(list_of_lists_of_dicts[0][1]["secondary_type"])
    print(list_of_lists_of_dicts[0][1]["atom_type"])

if __name__ == "__main__":
    main()
