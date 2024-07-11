
import pandas as pd
import urllib.request as requests


DATA_PATH = "dddd"


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