import time
from concurrent.futures import ThreadPoolExecutor
import os
import requests

print("sadfasf")
# Initialize a requests session
session = requests.Session()

# URL for the API request
url = "https://www.ebi.ac.uk/emdb/api/analysis/37271"

# Example task that makes an HTTP GET request
def example_task():
    # session.get(url)
    try:
        file = session.get(url).json()
    except:
        print("empty")
        return '', ''
        
    try:
        qscore = file[entry_id]["qscore"]["allmodels_average_qscore"]
    except Exception:
        qscore = ''
    try:
        atom_inclusion = file[entry_id]["atom_inclusion_by_level"]["average_ai_allmodels"]
    except Exception:
        atom_inclusion = ''

    print("request finished")
    return qscore, atom_inclusion


# SIMPLIFIED Example task that makes an HTTP GET request
def example_task_SIMPLIFIED():
    # session.get(url)
    session.get(url).json()


# Empirical testing to find the optimal number of max_workers
results = {}
cpu_count = os.cpu_count()
print(cpu_count)

for max_workers in range(1, cpu_count * 3):
    start_time = time.time()
    
    n_times = 5
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # futures = [executor.submit(example_task) for _ in range(n_times)]
        futures = [executor.submit(example_task_SIMPLIFIED) for _ in range(n_times)]
        # Wait for all futures to complete
        for f in futures:
            f.result()
    
    elapsed_time = time.time() - start_time
    results[max_workers] = elapsed_time
    print(f"Max Workers: {max_workers}, Average Time Taken: {(elapsed_time/n_times):.2f} seconds")

# Output the results to see which max_workers value is optimal
print("\nOptimal max_workers based on time taken:")
optimal_max_workers = min(results, key=results.get)
print(f"Optimal Max Workers: {optimal_max_workers}, Average Time Taken: {(results[optimal_max_workers]/n_times):.2f} seconds")
