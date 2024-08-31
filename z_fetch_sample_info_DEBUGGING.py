import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import pandas as pd
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor


CSV_DOWNLOAD_PATH = "./"  # we set a default path

# Fetch from user's input
QUERY = "ribosome AND resolution:[1 TO 4}"  # ohhhh curly braces are for exclusive ranges: https://www.ebi.ac.uk/emdb/documentation/search#:~:text=AND%20natural_source_ncbi_code%3A9606-,Range%20Search,-The%20search%20egnine
FILE_NAME = None  # user input for the name of the generated csv file
FETCH_CLASS = True  # user input for RCSB search


##### ------- DEBUG FLAGS/VARIABLES -------
PRINT_429_MSG = True   # prints every single 429 status code message
#  might spam ur command line
#  If the retry thing is set up properly, 429 messages wont be the end of the world since itll just... retry
#       In that case, you can turn this flag back on since it shouldn't spam anymore.

LOG_RCSB_RESULTS_VARIABLE = True    # if set to True, dump the results variable inside search_rcsb into a file

LOOPS = 1              # number of times to run search_emdb
#  I dont think loops rly do anything in terms of pushing the api limit
#  Time btwn loops is much slower than btwn rcsb requests since there's extra print statements after all the requests finish and probably some loop overhead too.

MAXWORKERS = None      # for setting Thread_Pool_Executor's max_workers parameter.
#  The higher this value, the faster the query (b/c it creates more threads), but consumes more sources.
#  From Thread_Pool_Executor's docstring: max_workers is "the maximum number of threads that can be used to execute the given calls".
#       By default max_workers is set as min(32, (os.cpu_count() or 1) + 4). For me it's 12.
#       Crank this value up to like 25 to simulate a faster internet connection.



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
        save_path=CSV_DOWNLOAD_PATH,
        file_name=FILE_NAME,
        fl=fields,
        rows=9999999,
        fetch_classification=False,
        fetch_qscore=True):
    
    ##### testing out docstring formatting, can ignore this change
    """
    Search the EMDB and generate .csv file using the searching query.

    Inputs:
    -------
    query(required): string, searching queries
    Example: 'structure_determination_method:"singleParticle"'
    The query can also be composed by multiple search terms concatenated by AND or OR terms
    Example: 'sample_type:"virus" and resolution [* TO 3]'

    save_path(required): string, path to save
    Default: DATA_PATH

    file_names(optional): string, desired file names
    Example: 'Ribosome'
    Default: 'download_file_0'

    fl(optional): a string of fields to be shown in the csv file; each item is separated by ','
    Example: 'emdb_id,resolution,fitted_pdbs'
    Default: 'emdb_id,title,resolution,fitted_pdbs,xref_UNIPROTKB,xref_ALPHAFOLD'

    rows(optional): int, how many entries to fetch
    Example: 100
    Default: 9999999

    fetch_classification: bool, fetching classificiation info or not
    Default: False

    fetch_qscore: bool, fetching Q-score or not
    Default: True
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

    save_path = os.path.join(save_path, file_name)
    os.makedirs(save_path, exist_ok=True)

    # checking for file names
    num = 1
    if file_name is None:
        file_name = f'download_file_{num:02}'
        # file_name = query
        full_path = os.path.join(save_path, f'{file_name}.csv')
        while any(filename.startswith(f'download_file_{num:02}') for filename in os.listdir(save_path)):
            num += 1
            file_name = f'download_file_{num:02}'
            full_path = os.path.join(save_path, f'{file_name}.csv')
    else:
        full_path = os.path.join(save_path, f'{file_name}_full.csv')
    with open(full_path, 'w') as out:
        out.write(output)
        #count = output.count('\n') - 1
    print('EMDB data fetched.')

    if fetch_classification:
        search_rcsb(full_path)
    if fetch_qscore:
        search_qscore(full_path)

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

    # Create a new DataFrame with the existing required columns
    new_df = df[existing_columns]
    final_path = os.path.join(save_path, f'{file_name}.csv')
    new_df.to_csv(final_path, index=False)
    print('\n--------------------------------------------------------------------------------\n')
    print(f'Entries file created at {final_path}.')

    return final_path     # ig this could be used in the gui?


def get_class(pdb_id):
    url = 'https://data.rcsb.org/rest/v1/core/entry/'
    if pdb_id == '':
        return '', ''
    try:
        r = session.get(url + pdb_id)
        if PRINT_429_MSG and r.status_code == 429:
            print(f"DEBUGGING > 429 code encountered for {pdb_id}")
        file = r.json()
        return file["struct_keywords"]["pdbx_keywords"], file["struct_keywords"]["text"]
    except Exception:
        return '', ''
        ##### empty pdb_id returns the same value as the Exception, so change to something different to be 100% sure (example below)
        # return str(r.status_code), ''


def search_rcsb(file_path):
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
        with ThreadPoolExecutor(max_workers=MAXWORKERS) as executor:
            print("DEBUGGING > ThreadPoolExecutor max_workers = ", executor._max_workers)
            results = list(tqdm(executor.map(get_class, pdb_ids), total=len(df)))

        ##### Some print statements
        print("DEBUGGING > Finished RCSB fetch requests") 
        print("DEBUGGING > Length of results variable:", len(results))
        ##### Checking the results variable (type is list btw). 
        ##### The final csv has all the rows, but might
        if LOG_RCSB_RESULTS_VARIABLE:
            with open(os.path.join(os.path.dirname(file_path), 'results_variable.txt'), 'w') as f:
                for line in results:
                    f.write(f"{line}\n")
            print(f"results variable dumped into {os.path.join(os.path.dirname(file_path), 'results_variable.txt')}")

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
        print(f'Classification info fetched. Saved at {file_path}')
        for index, info in df['RCSB_classification'].items():
            if info == '':
                error_entries.append(str(df['emdb_id'][index]))
        if error_entries:
            # print(f"Classification info not found for {len(error_entries)} enteries:\n{error_entries}")
            print(f"Classification info not found for {len(error_entries)} enteries")
        # return file_path
    else:
        print("The column 'fitted_pdbs' does not exist in the DataFrame.")


def get_qscore(emdb_map_id):
    entry_id = emdb_map_id.replace('EMD-', '')
    url = f"https://www.ebi.ac.uk/emdb/api/analysis/{entry_id}"
    try:
        file = session.get(url).json()
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
    """
    print('\nFetching Q-score and atom inclusion...')
    tqdm.pandas()
    df = pd.read_csv(file_path)
    with ThreadPoolExecutor() as executor:
        results = list(tqdm(executor.map(get_qscore, df['emdb_id']), total=len(df)))
    df['Q-score'], df['atom_inclusion'] = zip(*results)
    df.to_csv(file_path, index=False)
    # new_file_path = file_path.replace('.csv', '_qscore.csv')
    # os.rename(file_path, new_file_path)
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
        print(f'No Q-score fetched for {len(q_error)} enteries:\n{q_error}')
    if a_error:
        print(f'No atom_inclusion fetched for {len(a_error)} enteries:\n{a_error}')
    # return file_path





##### Changes
#     NEW DEBUG FLAGS/VARIABLES AT TOP OF FILE
#     Added main guard
#     NEW file created (same folder as the two csv's):
#         > results_variable.txt     - this is the results variable inside search_rcsb
#     Added print statements that start with "DEBUGGING > ". It's not some special package. It's just a string to differentiate btwn original prints.
#     Added some comments. Most of them have 5 #'s to distinguish from the original comments.
#     Slightly modifed a few print statements to also print the paths of output files

##### Issues/Findings
#     For the sake of consistency, I used the default query in this file (1513 entries).
#
#     Getting a 429 status code doesn't automatically mean Retry is not working, but getting it multiple times (like
#     for ALL of the last 500 ish entries probably suggests Retry is not working.
#
#     There's probably 2 scenarios:
#       1) Retry doesnt work (the lines Qibo highlighted in notion)
#       2) Retry does work, but the requests variable inside search_rcsb is not getting updated.
#
#     To reproduce the results:
#          Run the code and if you see "Classification info not found for 513 enteries" (or some other nonzero number)
#          printed in the command line, open up results_variable.txt, and you'll see lines with ('', '').
#          So even if Retry does work, those values are never being updated again.
#
#     EDIT:
#        I sorted/counted the print statements, and found all the 429 print messages were unique.
#        The command I used:
#           .venv/Scripts/python.exe z_fetch_sample_info_DEBUGGING.py | sort | uniq --count --repeated
#        A more general version:
#           python3 z_fetch_sample_info_DEBUGGING.py | sort | uniq --count --repeated
#        Also, this is with my scuffed debug flag PRINT_429_MSG = True (which is the default).
#
#        Here is my output from that linux command:
#           4 
#           2 --------------------------------------------------------------------------------
#           2 DEBUGGING > 429 code encountered for 4v92
#           2 DEBUGGING > 429 code encountered for 5jup
#
#        I checked the csv file (both actually), and they're actually different rows in the csvs, just with repeated pdb ids. [sidenote: either repeats aren't filtered out at this step or they're different enough to slip through]
#        So ALL of the 429 print messages are unique. Either they all worked on a Retry (kinda odd that it would trigger a 429 every time)
#        or Retry is not working, and it keeps requesting at the same rate, hence the continuous 429 status codes.
#
#        TLDR: seems like it's scenario 1: Retry doesn't work

##### TLDR: this is a debugging version of z_fetch_sample_info.py
#     Change the debug flags/variables (at top of file) to suppress some prints or use more threads for the request.

if __name__ == '__main__':
    #QUERY = "ribosome AND resolution:[4 TO 9}"  # user input for EMDB search
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    for i in range(1):
        print(f"DEBUGGING > loop: {i+1}")    # running multiple times shouldnt rly do antyhing cuz its the rate of re
        output_filepath = search_emdb(query=QUERY, save_path=CSV_DOWNLOAD_PATH, file_name="ribosome_res_1-4",\
                            fetch_qscore= False, fetch_classification=FETCH_CLASS)

    # for testing
    #for i in range(20):
    #    try:
    #        search_emdb(query=QUERY, save_path=CSV_DOWNLOAD_PATH, file_name="ribosome_res_1-4",\
    #                       fetch_qscore= True, fetch_classification=FETCH_CLASS)
    #    except Exception:
    #        print(Exception)