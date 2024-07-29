import requests
import pandas as pd
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor, as_completed
from collections import Counter

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
        save_path=DATA_PATH,
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

    # save_path(required): string, path to save
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
        # file_name = query
        full_path = os.path.join(save_path, file_name)
        while any(filename.startswith(f'download_file_{num:02}') for filename in os.listdir(save_path)):
            num += 1
            file_name = f'download_file_{num:02}.csv'
            full_path = os.path.join(save_path, file_name)
    else:
        full_path = save_path + file_name + '.csv'
    with open(full_path, 'w') as out:
        out.write(output)
        count = output.count('\n') - 1
    print('EMDB data fetched.')

    if fetch_classification and not fetch_qscore:
        new_path = search_rcsb(full_path, save_path)
    elif fetch_qscore and not fetch_classification:
        new_path = search_qscore(full_path)
    elif fetch_classification and fetch_qscore:
        new_path = search_qscore(search_rcsb(full_path, save_path))
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

    return final_path


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


def search_rcsb(file_path, save_path):
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
        save_path = save_path + file_name + '_classified.csv'
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
    response = requests.get(url)
    try:
        qscore = response.json()[entry_id]["qscore"]["allmodels_average_qscore"]
    except Exception:
        qscore = ''
    return qscore


def search_qscore(file_path):
    """
    Append Q-score to .csv file
    """
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


def process_similar(uniprotkb_1, uniprotkb_2, threshold) -> bool:
    # change df to lists
    list1 = str(uniprotkb_1).split(',')
    list2 = str(uniprotkb_2).split(',')

    # Count elements in both lists
    counter1 = Counter(list1)
    counter2 = Counter(list2)

    # Find common elements and their counts
    common_elements = counter1 & counter2
    longer_list_length = max(len(list1), len(list2))
    percentage = sum(common_elements.values())/longer_list_length*100

    if percentage < threshold:
        return True
    else:
        return False


def hard_pass_filter(raw_df: pd.DataFrame, threshold):
    process_df = raw_df
    saved_df = pd.DataFrame()
    dropped_df = pd.DataFrame()
    pbar = tqdm(total=len(raw_df))  # Progress bar
    while True:
        # Compare the aim row with other rows
        aim = process_df['xref_UNIPROTKB'][0]
        target = process_df['xref_UNIPROTKB'][0:-1]
        # Append the first row of process_df to save_df
        first_row = process_df.head(1)
        saved_df = pd.concat([saved_df, first_row], ignore_index=True)
        # remove first row
        process_df = process_df[0:-1]
        # comparing (multiprocess to improve runtime)
        with ProcessPoolExecutor() as executor:
            futures = [executor.submit(process_similar, aim, row, threshold) for row in target]
            mask = []
            for future in as_completed(futures):
                mask.append(future.result())
        # Update dropped rows
        rows_to_append = process_df[~pd.Series(mask)]
        if not rows_to_append.empty:
            dropped_df = pd.concat([dropped_df, rows_to_append], ignore_index=True)
        # Update process_df with new indexing
        process_df = process_df[pd.Series(mask)].reset_index(drop=True)
        # progress bar
        pbar.update(mask.count(False)+1)
        if len(process_df) <= 1:
            saved_df = pd.concat([saved_df, process_df.head(1)], ignore_index=True)
            pbar.update(1)
            break
        saved_df.columns = raw_df.columns
        dropped_df.columns = raw_df.columns
    return saved_df, dropped_df


def q_score_filter(df, threshold):
    # Sort the DataFrame by 'q_score'
    df_sorted = df.sort_values(by='Q-score')

    # Split the DataFrame into 'filtered' and 'kept'
    filtered = df_sorted[df_sorted['Q-score'] < threshold].reset_index(drop=True)
    kept = df_sorted[df_sorted['Q-score'] >= threshold].reset_index(drop=True)

    return kept, filtered


def refine_csv(file_path, save_path, uni_threshold, q_threshold):
    """
    :param file_path: path to .csv file
    :param save_path:
    :param uni_threshold: percentage uniprot similarity
    :param uni_threshold: q_score threshold
    """
    print('\n--------------------------------------------------------------------------------\nRefining .csv file...')
    file_name = os.path.basename(file_path)
    file_name = file_name.replace('.csv', '')
    raw_df = pd.read_csv(file_path)

    # filter by Q-score
    q_kept, q_filtered = q_score_filter(raw_df,q_threshold)
    # filter by hard_pass
    hard_kept, hard_filtered = hard_pass_filter(q_kept, uni_threshold)
    # join hard_pass filtered and q_score filtered
    final_filtered = pd.concat([hard_filtered, q_filtered], ignore_index=True)

    kept_path = save_path + file_name + '_kept.csv'
    hard_kept.to_csv(kept_path, index=False)
    filtered_path = save_path + file_name + '_filtered.csv'
    final_filtered.to_csv(filtered_path, index=False)

    print(f'Refinement completed, entries kept: {len(hard_kept)}. File wrote at {kept_path}.')
    print('--------------------------------------------------------------------------------\n')

    return kept_path, filtered_path
