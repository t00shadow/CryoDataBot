import requests
from timeit import default_timer as timer
import sys

log_file = open("logs.txt","w")

sys.stdout = log_file

print("this will be written to message.log")
print(">>> qscore_extractor.py runtimes <<<")





def get_emdb_validation_data(entry_id):
    start = timer()
    # Send API request
    url = f"https://www.ebi.ac.uk/emdb/api/analysis/{entry_id}"
    response = requests.get(url)
    end = timer()
    print("function: get_emdb_validation_data")
    print("elapsed time (s):", end - start) # Time in seconds, e.g. 5.38091952400282
    if response.status_code == 200:
        return response.json()
    else:
        return f"Failed to retrieve data: {response.status_code}"

def get_average_qscore(entry_id):
    start = timer()
    data = get_emdb_validation_data(entry_id)
    sys.stdout = sys.__stdout__
    print(data)
    sys.stdout = log_file
    end = timer()
    print("function: get_average_qscore")
    print("elapsed time (s):", end - start) # Time in seconds, e.g. 5.38091952400282
    print("oops get_average_qscore calls get_emdb_validation so its run time is mostly get_emdb_validation data. so it's extra runtime is just the difference btwn those 2 numbers")
    try:
        qscore = data[entry_id]["qscore"]["allmodels_average_qscore"]
        return qscore
    except Exception as e:
        # print(e)
        return "Q-score not found in the data"

# Example usage with an actual EMDB ID. 
# For actual usage, loop over list of EMDB IDs, and remove entries with Q-Scores that do not meet user defined threshold
entry_id = "9964"
average_qscore = get_average_qscore(entry_id)
print("average_qscore", average_qscore)


sys.stdout = sys.__stdout__
log_file.close()
print("done")
