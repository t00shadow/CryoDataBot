import requests
import pandas as pd
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor, as_completed
from collections import Counter
import numpy as np

DATA_PATH = r'C:\Users\micha\OneDrive\Desktop\QIBO\DATA_GEN_08012024'
fields = ("emdb_id,title,structure_determination_method,resolution,resolution_method,fitted_pdbs,current_status,"
          "deposition_date,map_release_date,primary_citation_author_string,primary_citation_title,xref_DOI,"
          "xref_PUBMED,primary_citation_year,primary_citation_journal_name,sample_info_string,microscope_name,"
          "illumination_mode,imaging_mode,electron_source,specimen_holder_name,segmentation_filename,slice_filename,"
          "additional_map_filename,half_map_filename,software,assembly_molecular_weight,xref_UNIPROTKB,xref_CPX,"
          "xref_EMPIAR,xref_PFAM,xref_CATH,xref_GO,xref_INTERPRO,xref_CHEBI,xref_CHEMBL,xref_DRUGBANK,xref_PDBEKB,"
          "xref_ALPHAFOLD")

def fixDataFrame(input_df_path: pd.DataFrame) -> pd.DataFrame:
    """
    Reads a CSV file from the given path and type casts all fields. Additionally empty fields are replaced with np.nan.

    Args:
        input_df_path (pd.DataFrame): The path to the input CSV file.

    Returns:
        pd.DataFrame: The fixed DataFrame.

    """
    input_df = pd.read_csv(input_df_path, dtype={'emdb_id':'string', 'sample_info_string': 'string','resolution': float, 'title':'string', 'xref_UNIPROTKB': 'string', 'xref_ALPHAFOLD': 'string', 'Q-score': float},
                           na_values=['', ' ', 'N/A', 'N/a', 'n/a', 'NA', 'Na', 'na', 'NAN', 'Nan', 'nan', 'NANAN',
                                                     'NanNan', 'nanNan', 'NANANAN', 'NanNanNan', 'nanNanNan', 'NANANANAN', 
                                                     'NanNanNanNan', 'nanNanNanNan', 'NANANANANAN', 'NanNanNanNanNan', 'nanNanNanNanNan', 'NANANANANANAN', 'NanNanNanNanNanNan', 
                                                     'nanNanNanNanNanNan', 'NANANANANANANAN', 'NanNanNanNanNanNanNan', 'nanNanNanNanNanNanNan', 'NANANANANANANANAN', 
                                                     'NanNanNanNanNanNanNanNan', 'nanNanNanNanNanNanNanNan', 'NANANANANANANANANAN', 'NanNanNanNanNanNanNanNanNan', 
                                                     'nanNanNanNanNanNanNanNanNan', 'N'])

    return input_df

def clean_input_data(input_csv_path: str, output_dir: str) -> tuple:
    # Read CSV as DataFrame and log the number of original entries    
    csv_df = pd.read_csv(input_csv_path)
    og_num_entries = len(csv_df)
    
    # Drop entries with NaN or NA values in specified columns
    csv_df = csv_df.dropna(subset=['emdb_id', 'title', 'resolution', 'fitted_pdbs'])
    
    # Identify and separate duplicates
    duplicates_df = csv_df[csv_df.duplicated(subset=['emdb_id', 'title', 'fitted_pdbs'], keep='first')]
    unique_df = csv_df.drop(duplicates_df.index)
    
   
    # Find rows with NaN in both 'xref_UNIPROTKB' and 'xref_ALPHAFOLD' columns
    raw_data_without_xRef = unique_df[unique_df[['xref_UNIPROTKB', 'xref_ALPHAFOLD']].isna().all(axis=1)]
    manualCheck_numEntries = len(raw_data_without_xRef)
    raw_data_without_xRef.to_csv(os.path.join(output_dir, "NaN_xRef.csv"), index=False)
    
    # Save the cleaned data to a CSV file
    raw_data_with_xREF = unique_df.dropna(subset=['xref_UNIPROTKB', 'xref_ALPHAFOLD'])
    raw_data_with_xREF.to_csv(os.path.join(output_dir, "Data_to_be_filtered.csv"), index=False)
    toBeFiltered_num_entries = len(raw_data_with_xREF)
    
    return (manualCheck_numEntries, toBeFiltered_num_entries)

def process_similar(uniprotkb_1: str, uniprotkb_2: str, threshold: float) -> bool:
    """
    Helper function to check if the similarity between two lists of UniProtKB IDs exceeds a given threshold.

    Args:
        uniprotkb_1 (str): A comma-separated string of UniProtKB IDs.
        uniprotkb_2 (str): A comma-separated string of UniProtKB IDs.
        threshold (float): The threshold value for similarity comparison.

    Returns:
        bool: True if the similarity exceeds the threshold, False otherwise.
    """
    # change df to lists
    list1 = str(uniprotkb_1).split(',')
    list2 = str(uniprotkb_2).split(',')

    # Count elements in both lists
    counter1 = Counter(list1)
    counter2 = Counter(list2)

    # Find common elements and their counts
    common_elements = counter1 & counter2

    longer_list_length = max(len(list1), len(list2))
    percentage = sum(common_elements.values())/longer_list_length

    if percentage <= threshold:
        return False
    else:
        return True
    
def evaluate_resoloution(df: pd.DataFrame, dTest: list, row: int) -> int:
    """
    Helper function to evaluate the resolution of a DataFrame based on a given list of indices.

    Args:
        df (pd.DataFrame): The DataFrame containing the resolution values.
        dTest (list): The list of indices to evaluate.
        row (int): The index of the row to compare against.

    Returns:
        tuple: A tuple containing the new minimum index and the excluded indices.
    """

    min_res = float('inf')
    new_min_index = 0
    dTest = np.array(dTest)
    for i in dTest:
        if df.at[i, 'resolution'] < min_res:
            min_res = df.at[i, 'resolution']
            new_min_index = i
        else:
            continue

    if new_min_index == row:
        if len(dTest) > 1:
            new_min_index = dTest[0]
            excluded = np.delete(dTest, 0)
        excluded = [new_min_index]
    else:
        excluded = [row]

    return new_min_index, excluded
        
def compute_similarity(i, mask, switch, first_filter_df, threshold):
    target = first_filter_df.at[i, switch[mask[i]]]
    results = []
    for j in range(len(mask)):
        aim = first_filter_df.at[j, switch[mask[j]]]
        if i == j:
            results.append((i, j, True))
        else:
            q = process_similar(target, aim, threshold)
            results.append((i, j, q))
    return results

def update_dict_test(corr_matrix, i):
    return (i, [j for j in range(len(corr_matrix[i])) if corr_matrix[i][j]])

def count_IDs(df: pd.DataFrame) -> bool:
    """
    Helper function that counts the xRefIDs in the given DataFrame and returns a boolean value based on which column has more IDs.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the IDs.

    Returns:
    bool: True if the conditions are met, False otherwise.
    """
    if pd.isna(df['xref_UNIPROTKB']):
        return False
    elif pd.isna(df['xref_ALPHAFOLD']):
        return True
    elif len(df['xref_UNIPROTKB']) >= len(df['xref_ALPHAFOLD']):
        return True
    else:
        return False
    
def second_filter (output_dir:str, threshold: float = 0.50):   
    from multiprocessing import Pool
    from tqdm import tqdm
    
    #Get CSV as DataFrame
    first_filter_df = fixDataFrame(os.path.join("r",output_dir,"First_Filter.csv"))
    switch = ['xref_ALPHAFOLD','xref_UNIPROTKB']
    mask = []
    for i, row in first_filter_df.iterrows():
        mask.append(count_IDs(row))
    

    corr_matrix = np.full((len(mask), len(mask)), False)    
    
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(compute_similarity, i, mask, switch, first_filter_df, threshold) for i in range(len(mask))]

        for future in tqdm(as_completed(futures), total=len(mask)):
            results = future.result()
            for i, j, value in results:
                corr_matrix[i][j] = value

                    

    corr_matrix_csv = pd.DataFrame(corr_matrix)
    corr_matrix_csv.to_csv(os.path.join("r",output_dir,"Correlation_Matrix.csv"), index = False)
    dict_test = {x: [] for x in range(len(mask))}
    
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(update_dict_test, corr_matrix, i) for i in range(len(corr_matrix))]
        
        for future in tqdm(as_completed(futures), total=len(corr_matrix)):
            i, indices = future.result()
            dict_test[i].extend(indices)
        
                
    elements_no_looky = np.full(len(mask), False)
    kept_mask = np.full(len(mask), False)
    for i in tqdm(range(len(mask))):
        if elements_no_looky[i]:
            continue
        
        append_min, excluded = evaluate_resoloution(first_filter_df, dict_test[i], i)
        elements_no_looky[excluded] = True
        kept_mask[append_min] = True
        
        
            
    final_df = first_filter_df[kept_mask]
    filtered_data = first_filter_df[~kept_mask]
    filtered_data.to_csv(os.path.join("r",output_dir,"Similar_Removed.csv"), index = False)
    final_df.to_csv(os.path.join("r",output_dir,"Final_Filter.csv"), index = False)
    final_filter_num_entries = len(final_df)
    initial_filter_num_entries = len(first_filter_df)
    
    
    return (final_filter_num_entries, initial_filter_num_entries)

# def first_filter(output_dir: str):
#     # Get CSV as DataFrame
#     raw_data_with_xREF = pd.read_csv(os.path.join(output_dir, "Data_to_be_filtered.csv"))
#     firstFilter_Path = os.path.join(output_dir, "First_Filter")
#     os.makedirs(firstFilter_Path, exist_ok=True)

#     # Identify non-unique rows based on 'xref_UNIPROTKB' and 'xref_ALPHAFOLD'
#     non_unique_mask = raw_data_with_xREF.duplicated(subset=['xref_UNIPROTKB', 'xref_ALPHAFOLD'], keep=False)
#     non_unique_df = raw_data_with_xREF[non_unique_mask]
#     unique_df = raw_data_with_xREF.drop(non_unique_df.index)

#     uniquexRef_num_entries = len(unique_df)
#     nonUnique_xRef_num_entries = len(non_unique_df)

#     nonNan_xRefUniprot = non_unique_df.dropna(subset=['xref_UNIPROTKB'])
#     nonNan_xRefAlphaFold = non_unique_df.dropna(subset=['xref_ALPHAFOLD'])

#     # Save grouped data with 'xref_UNIPROTKB'
#     grouped_proteins = nonNan_xRefUniprot.groupby("xref_UNIPROTKB")
#     grouped_proteins_df = grouped_proteins.apply(lambda x: x).reset_index(level=0).rename(columns={'level_0': 'group'}).sort_values(by=['group'])
#     grouped_proteins_df.to_csv(os.path.join(firstFilter_Path, "same_xRef.csv"), index=False)

#     # Find the highest resolution entries
#     highest_res_entries = []
#     for _, group in grouped_proteins:
#         highest_res_entries.append(group.loc[group["resolution"].idxmin()])
#     for _, group in nonNan_xRefAlphaFold.groupby("xref_ALPHAFOLD"):
#         highest_res_entries.append(group.loc[group["resolution"].idxmin()])

#     high_res_df = pd.DataFrame(highest_res_entries)

#     # Combine unique and highest resolution entries, remove duplicates by 'emdb_id'
#     result = pd.concat([unique_df, high_res_df], ignore_index=True).drop_duplicates(subset=['emdb_id']).sort_values(by='title')
#     result.to_csv(os.path.join(output_dir, "First_Filter.csv"), index=False)

#     postSoftPassNum_entries = len(result)

#     return postSoftPassNum_entries


def first_filter(output_dir:str):
    
    #Get CSV as DataFrame
    raw_data_with_xREF = fixDataFrame(os.path.join("r",output_dir,"Data_to_be_filtered.csv"))
    firstFilter_Path = os.path.join("r",output_dir,"First_Filter")
    
    if not os.path.exists(firstFilter_Path):
        os.makedirs(firstFilter_Path)

    
    #Besides removing the weird stuff (Duplicates in ID or Title), we also want to remove the rows that have the same xref_UNIPROTKB
    #non_unique_mask = raw_data_with_xREF.sort_values('resolution', ascending=False).duplicated(subset=['xref_UNIPROTKB','xref_ALPHAFOLD'], keep=False)
    non_unique_mask = raw_data_with_xREF.duplicated(subset=['xref_UNIPROTKB','xref_ALPHAFOLD'], keep=False)
    non_unique_df = raw_data_with_xREF[non_unique_mask] #Gives you a dataframe that has all the duplicates    
    unique_df = raw_data_with_xREF.drop(non_unique_df.index) #Drops the rows that are not unique based on previous dataframe
    
    uniquexRef_num_entries = len(unique_df)
    nonUnique_xRef_num_entries = len(non_unique_df)
    
    nonNan_xRefUniprot = non_unique_df[~non_unique_df['xref_UNIPROTKB'].isna()]
    nonNan_xRefAlphaFold = non_unique_df[~non_unique_df['xref_ALPHAFOLD'].isna()]

    #Save Exact Matches with xref_UNIPROTKB
    #Sort by groups of xref_UNIPROTKB
    grouped_proteins = nonNan_xRefUniprot.groupby("xref_UNIPROTKB")
    grouped_proteins_df = pd.concat([grouped_proteins.get_group(g) for g in grouped_proteins.groups], keys=grouped_proteins.groups.keys())
    grouped_proteins_df.reset_index(level=0, inplace=True)
    grouped_proteins_df.rename(columns={'level_0': 'group'}, inplace=True)
    grouped_proteins_df = grouped_proteins_df.sort_values(by=['group'])
    
    grouped_proteins_alpha = nonNan_xRefAlphaFold.groupby("xref_ALPHAFOLD")
    grouped_proteins_df_alpha = pd.concat([grouped_proteins_alpha.get_group(g) for g in grouped_proteins_alpha.groups], keys=grouped_proteins_alpha.groups.keys())
    grouped_proteins_df_alpha.reset_index(level=0, inplace=True)
    grouped_proteins_df_alpha.rename(columns={'level_0': 'group'}, inplace=True)
    grouped_proteins_df_alpha = grouped_proteins_df_alpha.sort_values(by=['group'])
    
    
    
    grouped_proteins_df.to_csv(os.path.join("r",firstFilter_Path,"same_xRef.csv"), index=False)
    
    lst = []

    #Find the best resoloution for each group of similar proteins
    for ref, group in grouped_proteins:
        high_res = group.loc[group["resolution"].idxmin()]
        lst.append(high_res) #Only append highest-res entries   
    
    for ref, group in grouped_proteins_alpha:
        high_res = group.loc[group["resolution"].idxmin()]
        lst.append(high_res) #Only append highest-res entries
          
    #Keep the highest resolution entries
    high_res_df = pd.DataFrame(lst,columns = non_unique_df.columns)
    
    #Join 2 dataframes and remove any duplicated by EMDB_ID
    result = pd.concat([unique_df, high_res_df], ignore_index=True)
    result = result.sort_values(by='title')
    non_unique_mask_emdbId = ~result.duplicated(subset=['emdb_id'], keep=False)
    
    #Save the data
    result.to_csv(os.path.join("r",output_dir,"First_Filter.csv"), index = False)

    # #Save this stuff
    
    df=result
    postSoftPassNum_entries = len(result)
    
    return(uniquexRef_num_entries, postSoftPassNum_entries)

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
                        'xref_UNIPROTKB', 'xref_ALPHAFOLD','RCSB_classification', 'Q-score']
    # Check which required columns are present in the DataFrame
    existing_columns = [col for col in review_columns if col in df.columns]
    # Print a message if any columns are missing
    missing_columns = [col for col in review_columns if col not in df.columns]
    if missing_columns:
        print(f"Warning: Missing columns in CSV file: {', '.join(missing_columns)}")
    # Create a new DataFrame with the existing required columns
    new_df = df
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



def q_score_filter(df, threshold):
    # Sort the DataFrame by 'q_score'
    df_sorted = df.sort_values(by='Q-score')

    # Split the DataFrame into 'filtered' and 'kept'
    filtered = df_sorted[df_sorted['Q-score'] < threshold].reset_index(drop=True)
    kept = df_sorted[df_sorted['Q-score'] >= threshold].reset_index(drop=True)

    return kept, filtered 




def refine_csv(uni_threshold: float = 0.5):
    """
    :param file_path: path to .csv file
    :param save_path:
    :param uni_threshold: percentage uniprot similarity
    :param uni_threshold: q_score threshold
    """
    print('\n--------------------------------------------------------------------------------\nRefining .csv file...')
    
    
    save_path = os.path.join("r",DATA_PATH, "Refined_Entries")
    os.makedirs(save_path, exist_ok=True)
    file_path = os.path.join("r",DATA_PATH,"download_file_09_review.csv")
    
    manual_check_num, toFilter_num = clean_input_data(file_path, save_path)
    print(f'Entries to Manually Check: {manual_check_num} entries. Entries to be filtered: {toFilter_num} entries.')
    print(f'Files saved at {os.path.join("r",save_path)}')
    postFirstFilter_num = first_filter(save_path)
    print(f'Entries after first filter: {postFirstFilter_num} entries.')
    final_filter_num_entries, initial_filter_num_entries = second_filter(save_path, uni_threshold)
    print(f'Entries after second filter: {final_filter_num_entries} entries.')
    print(f'Refinement completed, entries kept: {final_filter_num_entries}. File wrote at {os.path.join("r",save_path,"Final_Filter.csv")}.')
    print('--------------------------------------------------------------------------------\n')

    return 
