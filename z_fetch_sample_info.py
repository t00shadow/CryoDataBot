import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import pandas as pd
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import logging

# for handling api calls
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.1, status_forcelist=[ 429 ])   # status_forcelist defaults to None; can be set to custom values or Retry.RETRY_AFTER_STATUS_CODES, which is [413, 429, 503]
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# for logging
logger = logging.getLogger(__name__)


def search_emdb(
        query,
        save_path='./CSV',
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


    # checking for file names
    num = 1
    if file_name is None:
        file_name = f'download_file_{num:02}'
        while any(filename.startswith(f'download_file_{num:02}') for filename in os.listdir(save_path)):
            num += 1
            file_name = f'download_file_{num:02}'
            
    save_path = os.path.join(save_path, file_name)   
    os.makedirs(save_path, exist_ok=True)   
    full_path = os.path.join(save_path, f'{file_name}_full.csv')
    
    # configure logger
    logging.basicConfig(filename=save_path+'/'+file_name+'.log', encoding='utf-8', level=logging.INFO,\
                    format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    
    # search emdb
    logger.info('-'*5+f'Log for fetching sample information with query:"{query}".'+'-'*5)
    print('\n--------------------------------------------------------------------------------\nFetching EMDB data...')
    url = 'https://www.ebi.ac.uk/emdb/api/search/'
    output = ''
    try:
        logging.disable(logging.WARNING)
        r = requests.get(url + query + ' AND xref_links:"pdb"',
                         params={'rows': rows, 'fl': fl}, headers={'accept': 'text/csv'})
        logging.disable(logging.NOTSET)
        if r.status_code == 200:
            output += r.text
        else:
            print(f"Error fetching data query: {query}. Unexpected error.")
            logger.error(f"Error fetching data. Unexpected error.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data query: {query}. Exception: {e}.")
        logger.error(f"Error fetching data. Exception: {e}.")

    with open(full_path, 'w') as out:
        out.write(output)
    print('EMDB data fetched.')
    logger.info('Successfully fetched EMDB data.')

    # classification info
    if fetch_classification:
        try:
            logger.info('Start fetching classification info.')
            search_rcsb(full_path)
            logger.info('Successfully fetched classification info.')
        except Exception as e:
            logger.error(f'Unexpected exception while fetching classification info: {e}.') 
    # q_score and atom_inclusion
    if fetch_qscore:
        try:
            logger.info('Start fetching q_score and atom_inclusion.')
            search_qscore(full_path)
            logger.info('Successfully fetched q_score and atom_inclusion.')
        except Exception as e:
            logger.error(f'Unexpected exception while fetching q_score and atom_inclusion: {e}.')

    df = pd.read_csv(full_path)
    # List of required columns
    review_columns = ['title', 'resolution', 'emdb_id', 'fitted_pdbs', 'sample_info_string',
                        'xref_UNIPROTKB', 'xref_ALPHAFOLD', 'Q-score', 'atom_inclusion']
    # Check which required columns are present in the DataFrame
    existing_columns = [col for col in review_columns if col in df.columns]
    # Print a message if any columns are missing
    missing_columns = [col for col in review_columns if col not in df.columns]
    if 'RCSB_classification' in missing_columns:
        missing_columns.remove('RCSB_classification')
    if missing_columns:
        print(f"Warning: Missing columns in CSV file: {', '.join(missing_columns)}")
        logger.warning(f"Missing columns in CSV file: {', '.join(missing_columns)}.")

    # Create a new DataFrame with the existing required columns
    new_df = df[existing_columns]
    final_path = os.path.join(save_path, f'{file_name}.csv')
    new_df.to_csv(final_path, index=False)
    print('\n--------------------------------------------------------------------------------\n')
    print('Entries file created.')
    logger.info('-'*5+f'Successfully fetched sample info.'+'-'*5)
    return final_path


def get_class(pdb_id):
    url = 'https://data.rcsb.org/rest/v1/core/entry/'
    if pdb_id == '':
        return '', ''
    try:
        r = session.get(url + pdb_id)
        file = r.json()
        return file["struct_keywords"]["pdbx_keywords"], file["struct_keywords"]["text"]
    except Exception:
        return '', ''


def search_rcsb(file_path):
    """
    Read fitted_pdbs info and add classification and classification description for each entry
    file_path: path to .csv file
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
        logging.disable(logging.WARNING)
        with ThreadPoolExecutor() as executor:
            results = list(tqdm(executor.map(get_class, pdb_ids), total=len(df)))
        logging.disable(logging.NOTSET)

        # Unpack results into separate lists
        RCSB_classification, RCSB_description = zip(*results)

        # Assign the results to the DataFrame
        df["RCSB_classification"] = RCSB_classification
        df["RCSB_description"] = RCSB_description

        # file_name = os.path.basename(file_path)
        # file_name = file_name.replace('.csv', '_classified.csv')
        # save_path = save_path + file_name + '_classified.csv'
        df.to_csv(file_path, index=False)
        # os.remove(file_path)
        print('Classification info fetched.')
        for index, info in df['RCSB_classification'].items():
            if info == '':
                error_entries.append(str(df['emdb_id'][index]))
        if error_entries:
            print(f"Classification info not found for {len(error_entries)} enterie(s):\n{error_entries}")
            logger.warning(f"Classification info not found for {len(error_entries)} enterie(s):\n{error_entries}")
        # return file_path
    else:
        print("The column 'fitted_pdbs' does not exist in the DataFrame.")
        logger.warning(f"The column 'fitted_pdbs' does not exist in the DataFrame.")


def get_qscore(emdb_map_id):
    entry_id = emdb_map_id.replace('EMD-', '')
    url = f"https://www.ebi.ac.uk/emdb/api/analysis/{entry_id}"
    try:
        file = requests.get(url).json()
    except:
        return '', ''
        
    try:
        qscore = file[entry_id]["qscore"]["allmodels_average_qscore"]
    except Exception:
        qscore = ''
    try:
        atom_inclusion = file[entry_id]["atom_inclusion_by_level"]["average_ai_allmodels"]
    except Exception:
        atom_inclusion = ''

    return qscore, atom_inclusion


def search_qscore(file_path):
    """
    Append Q-score and atom inclusion to .csv file
    file_path: path to .csv file
    """
    print('\nFetching Q-score and atom inclusion...')
    tqdm.pandas()
    df = pd.read_csv(file_path)
    logging.disable(logging.WARNING)
    with ThreadPoolExecutor() as executor:
        results = list(tqdm(executor.map(get_qscore, df['emdb_id']), total=len(df)))
    logging.disable(logging.NOTSET)
    df['Q-score'], df['atom_inclusion'] = zip(*results)
    df.to_csv(file_path, index=False)
    print('Q-score and atom inclusion fetched.')

    # output error message
    q_error = []
    a_error = []
    for index, qscore in df['Q-score'].items():
        if qscore == '':
            q_error.append(str(df['emdb_id'][index]))
        if str(df['atom_inclusion'][index]) == '':
            a_error.append(str(df['emdb_id'][index]))
    if q_error:
        print(f'No Q-score fetched for {len(q_error)} enterie(s):\n{q_error}')
        logger.warning(f'No Q-score fetched for {len(q_error)} enterie(s):\n{q_error}')
    if a_error:
        print(f'No atom_inclusion fetched for {len(a_error)} enterie(s):\n{a_error}')
        logger.warning(f'No atom_inclusion fetched for {len(a_error)} enterie(s):\n{a_error}')


if __name__ == '__main__':
    search_emdb(query="ribosome AND resolution:[1 TO 4}", save_path='./CSV', file_name="ribosome_res_1-4",\
                       fetch_qscore= True, fetch_classification=True)

    '''# for testing RCSB function
    for i in range(20):
        try:
            search_emdb(query="ribosome AND resolution:[1 TO 4}", save_path='./CSV', file_name="ribosome_res_1-4",\
                        fetch_qscore= False, fetch_classification=True)
        except Exception:
            print(Exception)'''