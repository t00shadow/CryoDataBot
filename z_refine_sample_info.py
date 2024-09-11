import pandas as pd
import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from collections import Counter
import numpy as np
import logging

# SAVE_PATH = "./"  # user input for output files
INPUT_CSV = r"C:\Users\micha\OneDrive\Desktop\QIBO\DATA_CLEANUP_942024\download_file_09_review.csv"  # user input for inout csv file
THRE_UNI_SIMILARITY = 100  # user input for check UniportID similarity, 100 means loosest 
THRE_Q_SCORE = 0  # user input for check Q-score values, 0 means loosest

# for logging
logger = logging.getLogger(__name__)
save_path = os.path.dirname(INPUT_CSV)




def refine_csv(input_csv, q_threshold: float = THRE_Q_SCORE, uni_threshold: float = THRE_UNI_SIMILARITY):
    """
    :param file_path: path to .csv file
    :param uni_threshold: percentage uniprot similarity
    :param uni_threshold: q_score threshold
    """
    save_path = os.path.dirname(input_csv)
    # configure logger
    logging.basicConfig(filename=save_path+'/'+"refine_csv"+'.log', encoding='utf-8', level=logging.INFO,\
                    format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logger.info('-'*5+f'Refining sample information with Q_Score:"{THRE_Q_SCORE}"and Similarity_Threshold:"{THRE_UNI_SIMILARITY}".'+'-'*5)
    print('\n--------------------------------------------------------------------------------\nRefining EMDB entries...')

    # Q-Score filter
    save_path = os.path.dirname(input_csv)
    save_path_new = os.path.join(save_path, "Refined_Entries")
    os.makedirs(save_path_new, exist_ok=True)

    # make df from csv path
    df = pd.read_csv(input_csv)

    kept_df, filtered_df = q_score_filter(df, q_threshold)    
    kept_df.to_csv(os.path.join(save_path_new, "Q_Score_Kept.csv"), index=False)
    new_file_path = os.path.join(save_path_new, "Q_Score_Kept.csv")
    
    manual_check_num, toFilter_num = clean_input_data(new_file_path, save_path_new)
    logger.info('Entries to Manually Check: {manual_check_num} entries. Entries to be filtered: {toFilter_num} entries.')
    print(f'Entries to Manually Check: {manual_check_num} entries. Entries to be filtered: {toFilter_num} entries.')
    logging.info(f'Files saved at {os.path.join("r",save_path_new)}')
    print(f'Files saved at {os.path.join("r",save_path_new)}')
    postFirstFilter_num = first_filter(save_path_new)
    logging.info(f'Entries after first filter: {postFirstFilter_num} entries.')
    print(f'Entries after first filter: {postFirstFilter_num} entries.')
    final_filter_num_entries, initial_filter_num_entries = second_filter(save_path_new, uni_threshold)
    logging.info(f'Entries after second filter: {final_filter_num_entries} entries.')
    print(f'Entries after second filter: {final_filter_num_entries} entries.')
    logging.info(f'Refinement completed, entries kept: {final_filter_num_entries}. File wrote at {os.path.join("r",save_path_new,"Final_Filter.csv")}.')
    print(f'Refinement completed, entries kept: {final_filter_num_entries}. File wrote at {os.path.join("r",save_path_new,"Final_Filter.csv")}.')
    print('--------------------------------------------------------------------------------\n')

    return (os.path.join("r", save_path_new, "Final_Filter.csv"))


def fixDataFrame(input_df_path: pd.DataFrame) -> pd.DataFrame:
    """
    Reads a CSV file from the given path and type casts all fields. Additionally empty fields are replaced with np.nan.

    Args:
        input_df_path (pd.DataFrame): The path to the input CSV file.

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

    #nonNan_xRefUniprot = non_unique_df[~non_unique_df['xref_UNIPROTKB'].isna()]
    nonNan_xRefUniprot = unique_df[~unique_df['xref_UNIPROTKB'].isna()]
    #nonNan_xRefAlphaFold = non_unique_df[~non_unique_df['xref_ALPHAFOLD'].isna()]
    nonNan_xRefAlphaFold = unique_df[~unique_df['xref_ALPHAFOLD'].isna()]

    #Save Exact Matches with xref_UNIPROTKB
    #Sort by groups of xref_UNIPROTKB
    grouped_proteins = nonNan_xRefUniprot.groupby("xref_UNIPROTKB")
    ##### ======= DEBUGGING =======
    # seems like empty dataframe is not handled well in >> grouped_proteins = nonNan_xRefUniprot.groupby("xref_UNIPROTKB") <<
    # uncomment the print statements below for nonNan_xRefUniprot and nonNan_xRefAlphaFold and you'll see theyre both empty
    # This query has 3 entries, only 2 have BOTH xrefuniprot and xrefalphafold
    #
    # EDIT: ohhh its cuz look at line 272 and 273. theyre using non_unique_df. non_unique_df is not a superset of unique_df (it's just repeated rows im guesing)
    # so non_unique_df can be empty, and if it is empty, then nonNan_xRefUniprot and nonNan_xRefAlphaFold will also be empty
    # and then line 277 is trying to perform .groupby on an empty dataframe
    # need to go thru code later to see how it works. whys it using non_unique_df in lines 272 and 273 instead of unique_df (am i reading the code wrong?)

    # # quick df refresher
    # d = {'col1': [1, 2], 'col2': [3, 4]}
    # df = pd.DataFrame(data=d)
    # print(df)

    #print(raw_data_with_xREF)
    #print(firstFilter_Path)
    #print(non_unique_mask)
    #print(non_unique_df)
    #print(unique_df)
    #print(uniquexRef_num_entries)
    #print(nonUnique_xRef_num_entries)
    #print(nonNan_xRefUniprot)         # Empty DataFrame, just prints Columns (not empty) and then Index (empty array)
    #print(nonNan_xRefAlphaFold)       # Empty DataFrame, just prints Columns (not empty) and then Index (empty array)
    print(grouped_proteins)           # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000024382C12140>
    print(type(grouped_proteins))

    grouped_proteins_df = pd.concat([nonNan_xRefAlphaFold])
    print(grouped_proteins_df)
    ##### ======= DEBUGGING =======
    grouped_proteins_df = pd.concat([grouped_proteins.get_group(g) for g in grouped_proteins.groups], keys=grouped_proteins.groups.keys())
    print("after concat")
    print(grouped_proteins_df)
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
    # Identify and separate duplicates
    duplicates_df = result[result.duplicated(subset=['emdb_id', 'title', 'fitted_pdbs'], keep='first')]
    result = result.drop(duplicates_df.index)
    
    #Save the data
    result.to_csv(os.path.join("r",output_dir,"First_Filter.csv"), index = False)

    # #Save this stuff
    
    df=result
    postSoftPassNum_entries = len(result)
    
    return(uniquexRef_num_entries, postSoftPassNum_entries)


# def process_similar(uniprotkb_1, uniprotkb_2, threshold) -> bool:
#     # change df to lists
#     list1 = str(uniprotkb_1).split(',')
#     list2 = str(uniprotkb_2).split(',')

#     # Count elements in both lists
#     counter1 = Counter(list1)
#     counter2 = Counter(list2)

#     # Find common elements and their counts
#     common_elements = counter1 & counter2
#     longer_list_length = max(len(list1), len(list2))
#     percentage = sum(common_elements.values())/longer_list_length*100

#     if percentage < threshold:
#         return True
#     else:
#         return False


def q_score_filter(df, threshold):
    # Sort the DataFrame by 'q_score'
    df_sorted = df.sort_values(by='Q-score')

    # Split the DataFrame into 'filtered' and 'kept'
    filtered = df_sorted[df_sorted['Q-score'] < threshold].reset_index(drop=True)
    kept = df_sorted[df_sorted['Q-score'] >= threshold].reset_index(drop=True)

    return kept, filtered 



if __name__ == '__main__':
    #INPUT_CSV = "/home/qiboxu/MyProject/CryoDataBot/EVALUATION/ribosome_res_4-9/ribosome_res_4-9.csv"  # user input for inout csv file
    INPUT_CSV = r"C:\Users\micha\OneDrive\Desktop\QIBO\DATA_CLEANUP_942024\download_file_09_review.csv"
    THRE_UNI_SIMILARITY = 10  # user input for check UniportID similarity
    THRE_Q_SCORE = 0  # user input for check Q-score values

    refine_csv(input_csv=INPUT_CSV, q_threshold=THRE_Q_SCORE, uni_threshold=THRE_UNI_SIMILARITY)
