
import pandas as pd
import requests
import csv
import os


DATA_PATH = "dddd"


def search_emdb(
        query,
        save_directory=DATA_PATH,
        file_name=None,
        fl='emdb_id,title,resolution,fitted_pdbs,xref_UNIPROTKB,xref_ALPHAFOLD',
        rows=9999999,
        fetch_classification=True):
    """
    # Search the EMDB and generate .csv file using the searching query.

    # Inputs:
    # query(required): a string of searching queries
    # Example: 'structure_determination_method:"singleParticle"'
    # The query can also be composed by multiple search terms concatenated by AND or OR terms
    # Example: 'sample_type:"virus" and resolution [* TO 3]'

    # save_directory(required): path to save

    # file_names(optional): a string of desired file names
    # Example: 'Ribosome'
    # Default: 'download_file_0'

    # fl(optional): a string of fields to be shown in the csv file; each item is separated by ','
    # Example: 'emdb_id,resolution,fitted_pdbs'
    # Default: 'emdb_id,title,resolution,fitted_pdbs,xref_UNIPROTKB,xref_ALPHAFOLD'

    # rows(optional): an int indicating how many entries to fetch
    # Example: 100
    # Default: 9999999
    """
    url = 'https://www.ebi.ac.uk/emdb/api/search/'
    output = ''
    try:
        r = requests.get(url + query, params={'rows': rows, 'fl': fl}, headers={'accept': 'text/csv'})
        if r.status_code == 200:
            output += r.text
        else:
            print(f"Error fetching data query: {query}. Unexpected error.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

    if file_name is None:
        file_name = f'download_file_0' + '.csv'
        full_path = save_directory + file_name
        num = 1
        while os.path.exists(full_path):
            full_path = save_directory + f'download_file_{num}' + '.csv'
            num += num
    else:
        full_path = save_directory + file_name + '.csv'
    with open(full_path, 'w') as out:
        out.write(output)
        count = output.count('\n') - 1
    print(f'File wrote: {file_name} at {full_path}\nEntries fetched: {count}.')
    if fetch_classification:
        search_rcsb(full_path)


def search_rcsb(file_path):
    """
    Read fitted_pdbs info and add classification and classification description for each entry
    file_path: path to .csv file
    """
    df = pd.read_csv(file_path)
    if 'fitted_pdbs' in df.columns:
        url = 'https://data.rcsb.org/rest/v1/core/entry/'
        classification = []
        classification_des = []
        for i in range(len(df['fitted_pdbs'])):
            pdb_id = str(df['fitted_pdbs'][i])
            if pdb_id == 'nan':
                classification.append('')
                classification_des.append('')
                continue
            r = requests.get(url + pdb_id)
            file = r.json()
            classification.append(file["struct_keywords"]["pdbx_keywords"])
            classification_des.append(file["struct_keywords"]["text"])
        df["RCSB_classification"] = classification
        df["RCSB_description"] = classification_des
        file_name = os.path.basename(file_path)
        file_name.replace('.csv', '')
        save_path = DATA_PATH+file_name+'_classified.csv'
        df.to_csv(save_path, index=False)
        print(f'Classification info fetched. File wrote: {file_name} at {save_path}')
    else:
        print("The column 'fitted_pdbs' does not exist in the DataFrame.")


# This is a helper function that sends and receives requests
def get_emdb_validation_data(entry_ids):
    data = {}
    # Send API request for each entry ID
    for entry_id in entry_ids:
        url = f"https://www.ebi.ac.uk/emdb/api/analysis/{entry_id}"
        response = requests.get(url)
        if response.status_code == 200:
            data[entry_id] = response.json()
        else:
            data[entry_id] = f"Failed to retrieve data: {response.status_code}"
    return data


# This function retrieves the qscores from the dictionary returned from the request
def get_average_qscores(entry_ids):
    data = get_emdb_validation_data(entry_ids)
    qscores = {}
    for entry_id in entry_ids:
        try:
            if isinstance(data[entry_id], dict):
                qscores[entry_id] = data[entry_id][entry_id]["qscore"]["allmodels_average_qscore"]
            else:
                # Contains the error response status code because a dictionary was not returned
                qscores[entry_id] = data[entry_id]  
        except Exception as e: # Catches some strange errors. Usually won't happen
            # print(e)
            qscores[entry_id] = "Q-score not found in the data"
    return qscores


# This function writes the qscores to a CSV file
def write_qscores_to_csv(qscores, filename="emdb_qscores.csv"):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['EMDB ID', 'Average Q-score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for emdb_id, qscore in qscores.items():
            writer.writerow({'EMDB ID': emdb_id, 'Average Q-score': qscore})


# This function appends qscores to an existing CSV file with an option to include EMDB IDs
def append_qscores_to_csv(qscores, include_ids=True, filename="emdb_qscores.csv"):
    # Check if the file exists and read the existing data if it does
    if os.path.exists(filename):
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            existing_data = [row for row in reader]
    else:
        existing_data = []

    # Determine the next available column index
    next_column = len(existing_data[0]) if existing_data else 0

    # Prepare the new header if needed
    if not existing_data:
        if include_ids:
            existing_data.append(['EMDB ID', 'Average Q-score'])
        else:
            existing_data.append(['Average Q-score'])

    # Add new data to the existing data structure
    for idx, (emdb_id, qscore) in enumerate(qscores.items()):
        if include_ids:
            if len(existing_data) <= idx + 1:  # Add new row if necessary
                existing_data.append([''] * next_column)
            existing_data[idx + 1].extend([emdb_id, qscore])
        else:
            if len(existing_data) <= idx + 1:  # Add new row if necessary
                existing_data.append([''] * next_column)
            existing_data[idx + 1].append(qscore)

    # Write the updated data back to the file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(existing_data)


# # Example usage with a list of EMDB IDs
# entry_ids = ["9964", "3000", "1010", "10778", "14864"]  # Add more IDs as needed
# average_qscores = get_average_qscores(entry_ids)
# print(average_qscores) # Returns dictionary

# # write_qscores_to_csv(average_qscores)
# # append_qscores_to_csv(average_qscores, include_ids=True)

# # Formating for terminal output
# for id, score in average_qscores.items():
#     print(f"EMDB ID {id}: Q-score = {score}")
