import requests
import pandas as pd
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

DATA_PATH = r'C:/Users/30105/PycharmProjects/pythonProject/'
fields = ("emdb_id,title,structure_determination_method,resolution,resolution_method,fitted_pdbs,current_status,"
          "deposition_date,map_release_date,primary_citation_author_string,primary_citation_title,xref_DOI,"
          "xref_PUBMED,primary_citation_year,primary_citation_journal_name,sample_info_string,microscope_name,"
          "illumination_mode,imaging_mode,electron_source,specimen_holder_name,segmentation_filename,slice_filename,"
          "additional_map_filename,half_map_filename,software,assembly_molecular_weight,xref_UNIPROTKB,xref_CPX,"
          "xref_EMPIAR,xref_PFAM,xref_CATH,xref_GO,xref_INTERPRO,xref_CHEBI,xref_CHEMBL,xref_DRUGBANK,xref_PDBEKB,"
          "xref_ALPHAFOLD")


# fields = 'emdb_id,title,resolution,fitted_pdbs,xref_UNIPROTKB,xref_ALPHAFOLD'


def search_emdb(
        query,
        save_directory=DATA_PATH,
        file_name=None,
        fl=fields,
        rows=9999999,
        fetch_classification=False,
        fetch_qscore=True):
    """
    # Search the EMDB and generate .csv file using the searching query.

    # Inputs:
    # query(required): string, searching queries
    # Example: 'structure_determination_method:"singleParticle"'
    # The query can also be composed by multiple search terms concatenated by AND or OR terms
    # Example: 'sample_type:"virus" and resolution [* TO 3]'

    # save_directory(required): string, path to save
    # Default: DATA_PATH

    # file_names(optional): string, desired file names
    # Example: 'Ribosome'
    # Default: 'download_file_0'

    # fl(optional): a string of fields to be shown in the csv file; each item is separated by ','
    # Example: 'emdb_id,resolution,fitted_pdbs'
    # Default: 'emdb_id,title,resolution,fitted_pdbs,xref_UNIPROTKB,xref_ALPHAFOLD'

    # rows(optional): int, how many entries to fetch
    # Example: 100
    # Default: 9999999

    # fetch_classification: bool, fetching classificiation info or not
    # Default: False

    # fetch_qscore: bool, fetching Q-score or not
    # Default: True
    """
    print('\n--------------------------------------------------------------------------------\nFetching EMDB data...')
    url = 'https://www.ebi.ac.uk/emdb/api/search/'
    output = ''
    try:
        r = requests.get(url + query + ' AND xref_links:"pdb"',
                         params={'rows': rows, 'fl': fl}, headers={'accept': 'text/csv'})
        if r.status_code == 200:
            output += r.text
        else:
            print(f"Error fetching data query: {query}. Unexpected error.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

    # checking for file names
    num = 1
    if file_name is None:
        file_name = f'download_file_{num:02}.csv'
        full_path = os.path.join(save_directory, file_name)
        while any(filename.startswith(f'download_file_{num:02}') for filename in os.listdir(save_directory)):
            num += 1
            file_name = f'download_file_{num:02}.csv'
            full_path = os.path.join(save_directory, file_name)
    else:
        full_path = save_directory + file_name + '.csv'
    with open(full_path, 'w') as out:
        out.write(output)
        count = output.count('\n') - 1
    print('EMDB data fetched.')

    if fetch_classification and not fetch_qscore:
        new_path = search_rcsb(full_path, save_directory)
    elif fetch_qscore and not fetch_classification:
        new_path = search_qscore(full_path)
    elif fetch_classification and fetch_qscore:
        new_path = search_qscore(search_rcsb(full_path, save_directory))
    else:
        new_path = full_path

    df = pd.read_csv(new_path)
    # List of required columns
    review_columns = ['title', 'resolution', 'emdb_id', 'fitted_pdbs', 'sample_info_string',
                        'xref_UNIPROTKB', 'RCSB_classification', 'Q-score']
    # Check which required columns are present in the DataFrame
    existing_columns = [col for col in review_columns if col in df.columns]
    # Print a message if any columns are missing
    missing_columns = [col for col in review_columns if col not in df.columns]
    if missing_columns:
        print(f"Warning: Missing columns in CSV file: {', '.join(missing_columns)}")
    # Create a new DataFrame with the existing required columns
    new_df = df[existing_columns]
    final_path = full_path.replace('.csv','_review.csv')
    new_df.to_csv(final_path, index=False)
    print('--------------------------------------------------------------------------------\n')
    print(f'Final review file created: {final_path}')
    print('--------------------------------------------------------------------------------\n')


def get_class(pdb_id):
    url = 'https://data.rcsb.org/rest/v1/core/entry/'
    if pdb_id == '':
        return '', ''
    r = requests.get(url + pdb_id)
    file = r.json()
    try:
        return file["struct_keywords"]["pdbx_keywords"], file["struct_keywords"]["text"]
    except Exception:
        return '', ''


def search_rcsb(file_path, save_directory):
    """
    Read fitted_pdbs info and add classification and classification description for each entry
    file_path: path to .csv file
    return: path to classified .csv file
    """
    df = pd.read_csv(file_path)
    print("\nFetching classification info...")
    if 'fitted_pdbs' in df.columns:
        error_entries = []
        pdb_ids = []
        for _, pdb_id in df['fitted_pdbs'].items():
            if pdb_id == 'nan':
                pdb_ids.append('')
            else:
                pdb_id = pdb_id.split(',')
                pdb_id = pdb_id[0]
                pdb_ids.append(pdb_id)

        # Use ThreadPoolExecutor to process rows in parallel
        with ThreadPoolExecutor() as executor:
            results = list(tqdm(executor.map(get_class, pdb_ids), total=len(df)))

        # Unpack results into separate lists
        RCSB_classification, RCSB_description = zip(*results)

        # Assign the results to the DataFrame
        df["RCSB_classification"] = RCSB_classification
        df["RCSB_description"] = RCSB_description

        file_name = os.path.basename(file_path)
        file_name = file_name.replace('.csv', '')
        save_path = save_directory + file_name + '_classified.csv'
        df.to_csv(save_path, index=False)
        os.remove(file_path)
        print(f'Classification info fetched.')
        for index, info in df['RCSB_classification'].items():
            if info == '':
                error_entries.append(str(df['emdb_id'][index]))
        if error_entries:
            print(f"Classification info not found for {len(error_entries)} enteries:\n{error_entries}")
        return save_path
    else:
        print("The column 'fitted_pdbs' does not exist in the DataFrame.")


def get_qscore(emdb_map_id):
    entry_id = emdb_map_id.replace('EMD-', '')
    url = f"https://www.ebi.ac.uk/emdb/api/analysis/{entry_id}"
    session = requests.Session()
    response = session.get(url)
    try:
        qscore = response.json()[entry_id]["qscore"]["allmodels_average_qscore"]
    except Exception:
        qscore = ''
    return qscore


def search_qscore(file_path):
    # # Example usage with a list of EMDB IDs
    # entry_ids = ["9964", "3000", "1010", "10778", "14864"]  # Add more IDs as needed
    # average_qscores = get_average_qscores(entry_ids)
    # print(average_qscores) # Returns dictionary

    # # write_qscores_to_csv(average_qscores)
    # # append_qscores_to_csv(average_qscores, include_ids=True)

    # # Formating for terminal output
    # for id, score in average_qscores.items():
    #     print(f"EMDB ID {id}: Q-score = {score}")
    print('\nFetching Q-score...')
    tqdm.pandas()
    df = pd.read_csv(file_path)
    with ThreadPoolExecutor() as executor:
        df['Q-score'] = list(tqdm(executor.map(get_qscore, df['emdb_id']), total=len(df)))
    df.to_csv(file_path, index=False)
    new_file_path = file_path.replace('.csv', '')
    new_file_path += '_qscore.csv'
    os.rename(file_path, new_file_path)
    print(f'Q-score fetched. File created: {new_file_path}.')
    # output error message
    error = []
    for index, qscore in df['Q-score'].items():
        if qscore == '':
            error.append(str(df['emdb_id'][index]))
    if error:
        print(f'No Q-score fetched for {len(error)} enteries:\n{error}')
    return new_file_path
