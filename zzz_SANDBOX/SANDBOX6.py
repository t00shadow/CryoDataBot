### WHAT IS THIS?? It's a simple measurement of API call speeds.

import time
import requests

# List of API endpoints from different databases
api_urls = {
    "Database1": "https://data.rcsb.org/rest/v1/core/entry/8w51",
    "Database2": "https://www.ebi.ac.uk/emdb/api/analysis/37271",
}

# Function to measure the speed of API calls
def test_api_speed(url):
    session = requests.Session()
    start_time = time.time()
    
    try:
        response = session.get(url)
        response.raise_for_status()  # Check for HTTP errors
        elapsed_time = time.time() - start_time
        return elapsed_time
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# Main function to run the tests
def main():
    results = {}
    for name, url in api_urls.items():
        print(f"Testing {name}...")
        time_taken = test_api_speed(url)
        if time_taken is not None:
            results[name] = time_taken
        else:
            results[name] = "Failed"
    
    # Print results
    print("\nAPI Call Speed Results:")
    for name, result in results.items():
        if result == "Failed":
            print(f"{name}: Request failed")
        else:
            print(f"{name}: {result:.2f} seconds")

if __name__ == "__main__":
    main()
