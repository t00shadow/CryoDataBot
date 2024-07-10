import requests

# This is a helper function that sends and receives requests
def get_emdb_validation_data(entry_ids):
    data = {}
    # Send API request for each entry ID
    for entry_id in entry_ids:
        url = f"https://www.ebi.ac.uk/emdb/api/analysis/{entry_id}?information=atom_inclusion_by_level"
        response = requests.get(url)
        if response.status_code == 200:
            data[entry_id] = response.json()
        else:
            data[entry_id] = f"Failed to retrieve data: {response.status_code}"
    return data

# This function retrieves the qscores from the dictionary returned from the request
def get_atom_inclusion(entry_ids):
    data = get_emdb_validation_data(entry_ids)
    atom_inclusion = {}
    for entry_id in entry_ids:
        try:
            average_ai_allmodels = data[entry_id]["atom_inclusion_by_level"]["average_ai_allmodels"]
            atom_inclusion[entry_id] = average_ai_allmodels
        except Exception as e:
            # print(e)
            atom_inclusion[entry_id] = "Atom-inclusion not found in the data"
    return atom_inclusion

# Example usage with a list of EMDB IDs
entry_ids = ["9964"]  # Add more IDs as needed
average_atom = get_atom_inclusion(entry_ids)
print(average_atom)  # Returns dictionary

# Formatting for terminal output
for id, score in average_atom.items():
    print(f"EMDB ID {id}: Average_atom = {score}")
