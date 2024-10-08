import logging
import os
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed

import numpy as np
import pandas as pd
from tqdm import tqdm

from helper_funcs import calculate_title_padding


def filter_csv(input_csv, q_threshold: float = 0.0, uni_threshold: float = 1.0):
    """
    :param file_path: path to .csv file
    :param uni_threshold: percentage uniprot similarity
    :param uni_threshold: q_score threshold
    """
    save_path = os.path.dirname(input_csv)

    # configure logger
    logger = logging.getLogger('Redundancy_Filter_Logger')
    logger.setLevel(logging.INFO)  
    std_out_hdlr = logging.StreamHandler()
    std_out_hdlr.setLevel(logging.INFO)
    file_hdlr = logging.FileHandler(os.path.join(save_path, os.path.split(save_path)[-1]+"_redundancy_filter.log"))
    file_hdlr.setLevel(logging.INFO)
    file_hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'))
    logger.addHandler(std_out_hdlr)
    logger.addHandler(file_hdlr)

    logger.info(calculate_title_padding('Filtering EMDB Entries'))
    logger.info(f'Filtering Sample Information with Q_Score = {q_threshold} and Similarity_Threshold = {uni_threshold*100}%')
    logger.info('')

    # path
    archive_path = os.path.join(save_path, "Archive")
    os.makedirs(archive_path, exist_ok=True)

    # Q-Score filter
    logger.info(f'Going Through Q-Score Filter - Removing Entries with Q-score Less Than or Equal to {q_threshold}')
    q_score_kept_path, q_score_filter_kept_num_entries, q_score_filter_removed_num_entries = q_score_filter(input_csv, archive_path, q_threshold)
    logger.info(f'Entries Kept After Q-Score Filter: {q_score_filter_kept_num_entries} Entries')
    logger.info(f'Entries Removed After Q-Score Filter: {q_score_filter_removed_num_entries} Entries')
    logger.info(f'File Saved at {os.path.abspath(q_score_kept_path)}')
    logger.info('')

    # Manual Check Filter
    logger.info('Going Through Manual Check Filter- Identifying Entries Without UNIPROT or ALPHAFOLD IDs')
    xRef_present_path, manual_check_num, toFilter_num = clean_input_data(q_score_kept_path, archive_path)
    logger.info(f'Entries to Be Manually Checked: {manual_check_num} Entries')
    logger.info(f'Entries to Be Further Filtered: {toFilter_num} Entries')
    logger.info(f'File Saved at {os.path.abspath(xRef_present_path)}')
    logger.info('')

    # First Filter
    logger.info('Going Through First Filter - Removing Non-Unique Entries')
    first_filter_kept_path, num_entries_removed_by_first_filter, num_entries_kept_by_first_filter  = first_filter(xRef_present_path, archive_path)
    logger.info(f'Entries Kept After First Filter: {num_entries_kept_by_first_filter} Entries')
    logger.info(f'Entries Removed After First Filter: {num_entries_removed_by_first_filter} Entries')
    logger.info(f'File Saved at {os.path.abspath(first_filter_kept_path)}')
    logger.info('')

    # Second Filter
    logger.info(f'Going Through Second Filter - Removing Entries with UNIPROT Similarity Less Than or Equal to {uni_threshold*100}%')
    final_filter_kept_path, final_filter_kept_num_entries, final_filter_removed_num_entries = second_filter(first_filter_kept_path, archive_path, uni_threshold)
    logger.info(f'Entries Kept After Second Filter: {final_filter_kept_num_entries} Entries')
    logger.info(f'Entries Removed After Second Filter: {final_filter_removed_num_entries} Entries')
    logger.info(f'File Saved at {os.path.abspath(final_filter_kept_path)}')

    logger.info(calculate_title_padding('Filtering Completed'))
    logger.info('')

    return final_filter_kept_path


def fixDataFrame(input_df_path: str) -> pd.DataFrame:
    """
    Reads a CSV file from the given path and type casts all fields. Additionally empty fields are replaced with np.nan.

    Args:
        input_df_path (str): The path to the input CSV file.

    Returns:
        pd.DataFrame: The fixed DataFrame.

    """
    input_df = pd.read_csv(input_df_path, dtype={'emdb_id':'string', 'sample_info_string': 'string','resolution': float, 'fitted_pdbs':'string', 'title':'string', 'xref_UNIPROTKB': 'string', 'xref_ALPHAFOLD': 'string', 'Q-score': float, 'atom_inclusion': float},
                                                     na_values=['', ' ', 'N/A', 'N/a', 'n/a', 'NA', 'Na', 'na', 'NAN', 'Nan', 'nan', 'NANAN',
                                                     'NanNan', 'nanNan', 'NANANAN', 'NanNanNan', 'nanNanNan', 'NANANANAN', 
                                                     'NanNanNanNan', 'nanNanNanNan', 'NANANANANAN', 'NanNanNanNanNan', 'nanNanNanNanNan', 'NANANANANANAN', 'NanNanNanNanNanNan', 
                                                     'nanNanNanNanNanNan', 'NANANANANANANAN', 'NanNanNanNanNanNanNan', 'nanNanNanNanNanNanNan', 'NANANANANANANANAN', 
                                                     'NanNanNanNanNanNanNanNan', 'nanNanNanNanNanNanNanNan', 'NANANANANANANANANAN', 'NanNanNanNanNanNanNanNanNan', 
                                                     'nanNanNanNanNanNanNanNanNan', 'N'])

    return input_df


def clean_input_data(input_csv_path: str, output_dir: str):
    # Read CSV as DataFrame and log the number of original entries    
    csv_df = pd.read_csv(input_csv_path)
    manual_check_filter_path = os.path.join(output_dir, 'Manual_Check_Filter')
    os.makedirs(manual_check_filter_path, exist_ok=True)
    
    # Drop entries with NaN or NA values in specified columns
    csv_df = csv_df.dropna(subset=['emdb_id', 'title', 'resolution', 'fitted_pdbs'])
    
    # Identify and separate duplicates
    duplicates_df = csv_df[csv_df.duplicated(subset=['emdb_id', 'title', 'fitted_pdbs'], keep='first')]
    unique_df = csv_df.drop(duplicates_df.index)
      
    # Find rows with NaN in both 'xref_UNIPROTKB' and 'xref_ALPHAFOLD' columns
    raw_data_without_xRef = unique_df[unique_df[['xref_UNIPROTKB', 'xref_ALPHAFOLD']].isna().all(axis=1)]
    manualCheck_num_entries = len(raw_data_without_xRef)
    raw_data_without_xRef.to_csv(os.path.join(manual_check_filter_path, "NaN_xRef.csv"), index=False)
    
    # Save the cleaned data to a CSV file
    raw_data_with_xREF = unique_df.dropna(subset=['xref_UNIPROTKB', 'xref_ALPHAFOLD'])
    xRef_present_path = os.path.join(manual_check_filter_path, "xRef_present.csv")
    raw_data_with_xREF.to_csv(xRef_present_path, index=False)
    toBeFiltered_num_entries = len(raw_data_with_xREF)
    
    return xRef_present_path, manualCheck_num_entries, toBeFiltered_num_entries


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


def compute_similarity(i, mask, first_filter_df, threshold):
    switch = ('xref_ALPHAFOLD','xref_UNIPROTKB')
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
    

def second_filter(input_csv_path:str, output_dir:str, threshold: float = 0.50):   
    #Get CSV as DataFrame
    first_filter_df = fixDataFrame(input_csv_path)
    mask = []
    for i, row in first_filter_df.iterrows():
        mask.append(count_IDs(row))
    

    corr_matrix = np.full((len(mask), len(mask)), False)    
    
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(compute_similarity, i, mask, first_filter_df, threshold) for i in range(len(mask))]

        for future in tqdm(as_completed(futures), total=len(mask)):
            results = future.result()
            for i, j, value in results:
                corr_matrix[i][j] = value

                    

    corr_matrix_csv = pd.DataFrame(corr_matrix)
    corr_matrix_csv.to_csv(os.path.join(output_dir,"Correlation_Matrix.csv"), index = False)
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
    second_filter_path = os.path.join(output_dir, 'Second_Filter')
    os.makedirs(second_filter_path, exist_ok=True)
    filtered_data.to_csv(os.path.join(second_filter_path, "Second_Filter_Removed.csv"), index = False)
    final_filter_kept_path = os.path.join(dir:=os.path.dirname(output_dir), f"{os.path.split(dir)[-1]}_Final.csv")
    final_df.to_csv(final_filter_kept_path, index = False)
    final_filter_kept_num_entries = len(final_df)
    final_filter_removed_num_entries = len(filtered_data)
    
    
    return final_filter_kept_path, final_filter_kept_num_entries, final_filter_removed_num_entries


def first_filter(input_csv_path: str, output_dir:str):
    
    #Get CSV as DataFrame
    raw_data_with_xREF = fixDataFrame(input_csv_path)
    firstFilter_Path = os.path.join(output_dir,"First_Filter")
    os.makedirs(firstFilter_Path, exist_ok=True)


    #Besides removing the weird stuff (Duplicates in ID or Title), we also want to remove the rows that have the same xref_UNIPROTKB
    #non_unique_mask = raw_data_with_xREF.sort_values('resolution', ascending=False).duplicated(subset=['xref_UNIPROTKB','xref_ALPHAFOLD'], keep=False)
    non_unique_mask = raw_data_with_xREF.duplicated(subset=['xref_UNIPROTKB', 'xref_ALPHAFOLD'], keep=False)
    non_unique_df = raw_data_with_xREF[non_unique_mask] #Gives you a dataframe that has all the duplicates    
    unique_df = raw_data_with_xREF.drop(non_unique_df.index) #Drops the rows that are not unique based on previous dataframe
    
    #uniquexRef_num_entries = len(unique_df)
    #nonUnique_xRef_num_entries = len(non_unique_df)

    #nonNan_xRefUniprot = non_unique_df[~non_unique_df['xref_UNIPROTKB'].isna()]
    nonNan_xRefUniprot = unique_df[~unique_df['xref_UNIPROTKB'].isna()]
    #nonNan_xRefAlphaFold = non_unique_df[~non_unique_df['xref_ALPHAFOLD'].isna()]
    nonNan_xRefAlphaFold = unique_df[~unique_df['xref_ALPHAFOLD'].isna()]

    #Save Exact Matches with xref_UNIPROTKB
    #Sort by groups of xref_UNIPROTKB
    grouped_proteins = nonNan_xRefUniprot.groupby("xref_UNIPROTKB")

    grouped_proteins_df = pd.concat([nonNan_xRefAlphaFold])
    #print(grouped_proteins_df)
    ##### ======= DEBUGGING =======
    grouped_proteins_df = pd.concat([grouped_proteins.get_group(g) for g in grouped_proteins.groups], keys=grouped_proteins.groups.keys())
    #print("after concat")
    #print(grouped_proteins_df)
    grouped_proteins_df.reset_index(level=0, inplace=True)
    grouped_proteins_df.rename(columns={'level_0': 'group'}, inplace=True)
    grouped_proteins_df = grouped_proteins_df.sort_values(by=['group'])
    
    grouped_proteins_alpha = nonNan_xRefAlphaFold.groupby("xref_ALPHAFOLD")
    grouped_proteins_df_alpha = pd.concat([grouped_proteins_alpha.get_group(g) for g in grouped_proteins_alpha.groups], keys=grouped_proteins_alpha.groups.keys())
    grouped_proteins_df_alpha.reset_index(level=0, inplace=True)
    grouped_proteins_df_alpha.rename(columns={'level_0': 'group'}, inplace=True)
    grouped_proteins_df_alpha = grouped_proteins_df_alpha.sort_values(by=['group'])
    
    
    
    grouped_proteins_df.to_csv(os.path.join(firstFilter_Path,"same_xRef.csv"), index=False)
    
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
    # Identify and separate duplicates
    duplicates_df = result[result.duplicated(subset=['emdb_id', 'title', 'fitted_pdbs'], keep='first')]
    result = result.drop(duplicates_df.index)
    
    #Save the data
    first_filter_kept_path = os.path.join(firstFilter_Path,"First_Filter_Kept.csv")
    result.to_csv(first_filter_kept_path, index = False)

    #Save this stuff
    num_entries_kept_by_first_filter = len(result)
    num_entries_removed_by_first_filter = len(raw_data_with_xREF) - num_entries_kept_by_first_filter
    
    return first_filter_kept_path, num_entries_removed_by_first_filter, num_entries_kept_by_first_filter 


def q_score_filter(input_csv_path:str, archive_path:str, threshold:float):
    # Sort the DataFrame by 'q_score'
    df = fixDataFrame(input_csv_path)
    df_sorted = df.sort_values(by='Q-score')

    # Split the DataFrame into 'removed' and 'kept'
    removed_df = df_sorted[(df_sorted['Q-score'] < threshold) | (df_sorted['Q-score'].isna())].reset_index(drop=True)
    kept_df = df_sorted[df_sorted['Q-score'] >= threshold].reset_index(drop=True)

    q_score_filter_path = os.path.join(archive_path, 'Q_Score_Filter')
    os.makedirs(q_score_filter_path,exist_ok=True)
    q_score_kept_path = os.path.join(q_score_filter_path, "Q_Score_Kept.csv")    
    kept_df.to_csv(q_score_kept_path, index=False)
    removed_df.to_csv(os.path.join(q_score_filter_path, "Q_Score_Removed.csv"), index=False)

    q_score_filter_removed_num_entries = len(removed_df)
    q_score_filter_kept_num_entries = len(kept_df)

    return q_score_kept_path, q_score_filter_kept_num_entries, q_score_filter_removed_num_entries 


def map_model_filter(df:pd.DataFrame, vof_threshold:float=0.25, dice_threshold:float=0.4):
    """
    Filter the DataFrame to remove entries with vof < vof_threshold and 
    dice_coefficient < dice_threshold.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the data.
    vof_threshold (float): The threshold for the vof values.
    dice_threshold (float): The threshold for the dice_coefficient values.

    Returns:
    tuple: A tuple containing two DataFrames:
        - kept_df: DataFrame with entries that meet the conditions.
        - removed_df: DataFrame with entries that were removed.
    """
    # Create a mask for the conditions
    mask = (df['vof'] >= vof_threshold) | (df['dice_coefficient'] >= dice_threshold)
    
    # Filter the DataFrame
    kept_df = df[mask]
    removed_df = df[~mask]

    return kept_df, removed_df


if __name__ == '__main__':
    #INPUT_CSV = "/home/qiboxu/MyProject/CryoDataBot/EVALUATION/ribosome_res_4-9/ribosome_res_4-9.csv"  # user input for inout csv file
    # INPUT_CSV = r"C:\Users\micha\OneDrive\Desktop\QIBO\DATA_CLEANUP_942024\download_file_09_review.csv"
    # INPUT_CSV = "CSV/ribosome_res_1-4.csv"
    INPUT_CSV = "CSV/ribosome_res_1-4.csv"
    THRE_UNI_SIMILARITY = 0.7  # user input for check UniportID similarity
    THRE_Q_SCORE = 0.39  # user input for check Q-score values

    filter_csv(input_csv=INPUT_CSV, q_threshold=THRE_Q_SCORE, uni_threshold=THRE_UNI_SIMILARITY)
