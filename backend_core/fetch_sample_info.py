from importlib import metadata
import logging
import os
from concurrent.futures import ThreadPoolExecutor
from configparser import ConfigParser

import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm
from urllib3.util.retry import Retry

import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from backend_helpers.helper_funcs import calculate_title_padding


def search_emdb(
        query,
        save_path='Metadata',
        file_name=None,
        fl=("emdb_id,title,structure_determination_method,resolution,resolution_method,fitted_pdbs,current_status,"
          "deposition_date,map_release_date,primary_citation_author_string,primary_citation_title,xref_DOI,"
          "xref_PUBMED,primary_citation_year,primary_citation_journal_name,sample_info_string,microscope_name,"
          "illumination_mode,imaging_mode,electron_source,specimen_holder_name,segmentation_filename,slice_filename,"
          "additional_map_filename,half_map_filename,software,assembly_molecular_weight,xref_UNIPROTKB,xref_CPX,"
          "xref_EMPIAR,xref_PFAM,xref_CATH,xref_GO,xref_INTERPRO,xref_CHEBI,xref_CHEMBL,xref_DRUGBANK,xref_PDBEKB,"
          "xref_ALPHAFOLD"),
        rows=9999999,
        fetch_classification=False,
        fetch_qscore=True):
    """
    Search the Electron Microscopy Data Bank (EMDB) for entries matching the given query and save the results.

    Parameters:
    query (str): The search query for the EMDB.
    save_path (str): The directory where the results will be saved. Default is 'Metadata'.
    file_name (str): The name of the file to save the results. If None, a unique name will be generated.
    fl (str): The fields to fetch from the EMDB. Default is a predefined set of fields.
    rows (int): The maximum number of rows to fetch. Default is 9999999.
    fetch_classification (bool): Whether to fetch classification information. Default is False.
    fetch_qscore (bool): Whether to fetch Q-score and atom inclusion information. Default is True.

    Returns:
    str: The path to the final CSV file containing the fetched data.
    """
    # get logger
    logger = logging.getLogger('Fetch_Sample_Info_Logger')
    logger.setLevel(logging.DEBUG)

    os.makedirs(save_path, exist_ok=True)   # bugfix: if save_path doesnt exist yet, next line will throw an error
    # check file names
    num = 1
    if file_name is None:
        file_name = f'download_file_{num:03}'
        while any(filename.startswith(f'download_file_{num:03}') for filename in os.listdir(save_path)):
            num += 1
            file_name = f'download_file_{num:03}'
    else:
        user_filename = file_name
        file_name = f'{user_filename}_{num:03}'
        while any(filename.startswith(f'{user_filename}_{num:03}') for filename in os.listdir(save_path)):
            num += 1
            file_name = f'{user_filename}_{num:03}'

    save_path = os.path.join(save_path, file_name)
    os.makedirs(save_path, exist_ok=True)   
    file_path = os.path.join(save_path, f'{file_name}_full.csv')

    # configure logger
    std_out_hdlr = logging.StreamHandler()
    std_out_hdlr.setLevel(logging.INFO)
    file_hdlr = logging.FileHandler(os.path.join(save_path, f'{file_name}_fetch_sample_info.log'))
    file_hdlr.setLevel(logging.INFO)
    #std_out_hdlr.setFormatter(logging.Formatter(''))
    file_hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'))
    logger.addHandler(std_out_hdlr)
    logger.addHandler(file_hdlr)

    # search emdb
    logger.info('-'*50+'Fetching Sample Information'+'-'*50)
    logger.info(f'Query: {query}')
    url = 'https://www.ebi.ac.uk/emdb/api/search/'
    output = ''
    logger.info('Fetching EMDB Search Data...')
    try:
        logging.disable(logging.WARNING)
        r = requests.get(url + query + ' AND xref_links:"pdb"',
                         params={'rows': rows, 'fl': fl}, headers={'accept': 'text/csv'})
        logging.disable(logging.NOTSET)
        if r.status_code == 200:
            output += r.text
        else:
            logger.error(f"Error Fetching Data: Status Code - {r.status_code}")
            logger.error('Error may Occur due to Network Problems, Please Try Again Later')
            logger.error(calculate_title_padding('Failed Fetching Sample Info'))
            raise requests.HTTPError(f"Error Fetching Data: Status Code - {r.status_code}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error Fetching Data: {e}")
        logger.error('Error may Occur due to Network Problems, Please Try Again Later')
        logger.error(calculate_title_padding('Failed Fetching Sample Info'))
        raise requests.HTTPError(f"Error Fetching Data: {e}")
    
    # save EMDB data
    with open(file_path, 'w') as out:
        out.write(output)
    logger.info('Successfully Fetched EMDB Search Data')

    # classification info
    if fetch_classification:
        try:
            search_rcsb(file_path)
        except Exception as e:
            logger.warning(f'!!! Unexpected Error Occurred while Fetching Classification Info !!!: {e}') 
            logger.warning('Error may Occur due to Network Problems, Please Try Again Later')

    # q_score and atom_inclusion
    if fetch_qscore:
        try:
            search_qscore(file_path)
        except Exception as e:
            logger.warning(f'!!! Unexpected Error Occurred while Fetching Q-score and atom_inclusion !!!: {e}')
            logger.warning('Error may Occur due to Network Problems, Please Try Again Later')

    df = pd.read_csv(file_path)
    # List of required columns
    review_columns = ['title', 'resolution', 'emdb_id', 'fitted_pdbs', 'xref_UNIPROTKB',\
                       'xref_ALPHAFOLD', 'Q-score', 'atom_inclusion', 'recommended_contour_level']
    # Check which required columns are present in the DataFrame
    existing_columns = [col for col in review_columns if col in df.columns]
    # Print a message if any columns are missing
    missing_columns = [col for col in review_columns if col not in df.columns]
    if missing_columns:
        #print(f"Warning: Missing columns in CSV file: {', '.join(missing_columns)}")
        logger.warning(f"Missing Columns in CSV File: {', '.join(missing_columns)}, which may be Required for CSV Refinement")

    # Create a new DataFrame with the existing required columns
    new_df = df[existing_columns]
    # Splitting (rare) lists of pdb ids and keeping only the first one
    new_df.loc[:, 'fitted_pdbs'] = new_df['fitted_pdbs'].str.split(',', n=1, expand=False).str[0]
    final_path = os.path.join(save_path, f'{file_name}.csv')
    new_df.to_csv(final_path, index=False)

    logger.info(calculate_title_padding('Successfully Fetched Sample Info'))
    logger.info('')

    return final_path


def get_class(pdb_id):
    """
    Fetch classification and description for a given PDB ID.

    Parameters:
    pdb_id (str): The PDB ID to fetch classification for.

    Returns:
    tuple: A tuple containing the classification and description.
    """
    logger = logging.getLogger('Fetch_Sample_Info_Logger')
    logger.info(f'Fetching for {pdb_id}...')
    # for handling api calls
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.1, status_forcelist=[429])   # status_forcelist defaults to None; can be set to custom values or Retry.RETRY_AFTER_STATUS_CODES, which is [413, 429, 503]
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    url = 'https://data.rcsb.org/rest/v1/core/entry/'
    if pdb_id == '':
        return '', ''
    try:
        r = session.get(url + pdb_id)
        file = r.json()
        return file["struct_keywords"]["pdbx_keywords"], file["struct_keywords"]["text"]
    except Exception:
        return '', ''
    finally:
        session.close()


def search_rcsb(file_path):
    """
    Read fitted_pdbs info and add classification and classification description for each entry.

    Parameters:
    file_path (str): Path to the .csv file containing the data.
    """
    logger = logging.getLogger('Fetch_Sample_Info_Logger')
    logger.info('')
    logger.info("Fetching Classification Info...")
    df = pd.read_csv(file_path)

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
        #logging.disable(logging.WARNING)
        with logging_redirect_tqdm([logger]):
            with ThreadPoolExecutor() as executor:
                results = list(tqdm(executor.map(get_class, pdb_ids), total=len(df)))
        #logging.disable(logging.NOTSET)

        # Unpack results into separate lists
        RCSB_classification, RCSB_description = zip(*results)

        # Assign the results to the DataFrame
        df["RCSB_classification"] = RCSB_classification
        df["RCSB_description"] = RCSB_description

        df.to_csv(file_path, index=False)
        logger.info('Classification Info Fetched')

        for index, info in df['RCSB_classification'].items():
            if info == '':
                error_entries.append(str(df['emdb_id'][index]))
        if error_entries:
            logger.warning(f"Classification Info not Found for {len(error_entries)} Enterie(s):")
            length = len(error_entries)
            for idx in range(0, length, num:=10):
                logger.info(f'  {", ".join(error_entries[idx:idx + num])}')
    else:
        #print("The column 'fitted_pdbs' does not exist in the DataFrame.")
        logger.warning(f"The Column 'fitted_pdbs' Does not Exist in the DataFrame, Cannot Fetch Classification Info")


def get_qscore(emdb_map_id):
    """
    Fetch Q-score and atom inclusion for a given EMDB map ID.

    Parameters:
    emdb_map_id (str): The EMDB map ID to fetch Q-score for.

    Returns:
    tuple: A tuple containing the Q-score, atom inclusion, and recommended contour level.
    """
    # get logger
    logger = logging.getLogger('Fetch_Sample_Info_Logger')

    logger.info(f'Fetching for {emdb_map_id}...')
    entry_id = emdb_map_id.replace('EMD-', '')
    url = f"https://www.ebi.ac.uk/emdb/api/analysis/{entry_id}"
    file = requests.get(url).json()

    try:
        qscore = file[entry_id]["qscore"]["allmodels_average_qscore"]
    except KeyError as e:
        #logger.debug(f"Error Fetching Q-score for {emdb_map_id}: {e}")
        qscore = ''
    try:
        atom_inclusion = file[entry_id]["atom_inclusion_by_level"]["average_ai_allmodels"]
    except KeyError as e:
        #logger.debug(f"Error Fetching atom_inclusion for {emdb_map_id}: {e}")
        atom_inclusion = ''
    try:
        recl = file[entry_id]["recommended_contour_level"]["recl"]
    except KeyError as e:
        #logger.debug(f"Error Fetching recommended_contour_level for {emdb_map_id}: {e}")
        recl = ''

    return qscore, atom_inclusion, recl


def search_qscore(file_path):
    """
    Append Q-score and atom inclusion to .csv file.

    Parameters:
    file_path (str): Path to the .csv file containing the data.
    """
    #print('\nFetching Q-score and atom inclusion...')
    logger = logging.getLogger('Fetch_Sample_Info_Logger')
    logger.info('')
    logger.info('Fetching Q-score, atom inclusion, and recommended_contour_level...')
    tqdm.pandas()
    df = pd.read_csv(file_path)
    #logging.disable(logging.WARNING)
    with ThreadPoolExecutor() as executor:
        with logging_redirect_tqdm([logger]):
            results = list(tqdm(executor.map(get_qscore, df['emdb_id']), total=len(df)))
    #logging.disable(logging.NOTSET)
    df['Q-score'], df['atom_inclusion'], df['recommended_contour_level'] = zip(*results)
    df.to_csv(file_path, index=False)
    #print('Q-score, atom_inclusion, and recommended_contour_level fetched.')
    logger.info('Q-score, atom_inclusion, and recommended_contour_level Fetched')
    
    # Output error message
    q_error = []
    a_error = []
    c_error = []
    for index, qscore in df['Q-score'].items():
        if qscore == '':
            q_error.append(str(df['emdb_id'][index]))
        if str(df['atom_inclusion'][index]) == '':
            a_error.append(str(df['emdb_id'][index]))
        if str(df['recommended_contour_level'][index]) == '':
            c_error.append(str(df['emdb_id'][index]))
    if q_error:
        #print(f'No Q-score fetched for {len(q_error)} enterie(s):\n{q_error}')
        logger.info('')
        logger.warning(f'No Q-score Fetched for {len(q_error)} Enterie(s):')
        length = len(q_error)
        for idx in range(0, length, num:=10):
            logger.info(f'  {", ".join(q_error[idx:idx + num])}')
    if a_error:
        #print(f'No atom_inclusion fetched for {len(a_error)} enterie(s):\n{a_error}')
        logger.info('')
        logger.warning(f'No atom_inclusion Fetched for {len(a_error)} Enterie(s):')
        length = len(a_error)
        for idx in range(0, length, num:=10):
            logger.info(f'  {", ".join(a_error[idx:idx + num])}')
    if c_error:
        #print(f'No recommended_contour_level fetched for {len(c_error)} enterie(s):\n{c_error}')
        logger.info('')
        logger.warning(f'No recommended_contour_level Fetched for {len(c_error)} Enterie(s):')
        length = len(c_error)
        for idx in range(0, length, num:=10):
            logger.info(f'  {", ".join(c_error[idx:idx + num])}')


def main():
        # from config file read default values
    fetch_sample_info_config = ConfigParser(default_section='fetch_sample_info')
    fetch_sample_info_config.read('CryoDataBotConfig.ini')
    fetch_qscore = fetch_sample_info_config.getboolean('user_settings', 'fetch_qscore')
    fetch_classification = fetch_sample_info_config.getboolean('user_settings', 'fetch_classification')
    rows = fetch_sample_info_config.getint('user_settings', 'rows')

    path = search_emdb(query="ribosome AND resolution:[1 TO 4}",
                       file_name='ribosome_res_1-4',
                       save_path='CryoDataBot_Data/Metadata',
                       fetch_qscore=fetch_qscore,
                       fetch_classification=fetch_classification, 
                       rows=20,
                       )
    print('Metadata saved to:', path)


if __name__ == '__main__':
    main()