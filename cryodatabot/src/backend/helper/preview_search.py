############################################
### Small script to mainly help with GUI ###
############################################

import requests
import urllib.parse


# Runtime: CONSTANT for all queries, ~1.4 seconds (ofc internet speeds can affect it)
def preview_emdb(query, rows=10, page=1, fl="emdb_id,title,resolution"):
    """
    Search EMDB and return a preview. Return the first 10 entries (EMDB ID and title) and the total count of search hits.

    Parameters:
        query (str): The search query (e.g., "spliceosome AND resolution:[2 TO 4]")
        rows (int, optional): Number of entries per page (default 10)
        page (int, optional): Current page (default 1)
        fl (string, optional): List of fields to be shown (CSV exclusive). (default "emdb_id,title,resolution")
    
    Returns:
        dict: Contains total hits and the first 10 entries with their names.
    """
    base_url = "https://www.ebi.ac.uk/emdb/api/search/"
    encoded_query = urllib.parse.quote(query)
    request_url = f"{base_url}{encoded_query}"
    params = {
        "rows": rows,
        "page": page,
        "fl": fl,
    }

    response = requests.get(request_url, params=params, headers={'Accept': 'text/csv'})

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return {}

    # Handle CSV data from the response
    lines = response.text.splitlines()
    entries = []

    # Parse CSV header and data
    header = lines[0].split(',')
    for line in lines[1:]:
        fields = line.split(',')
        entry = dict(zip(header, fields))
        entries.append(entry)
    
    count_estimate_response = requests.get(f"https://www.ebi.ac.uk/emdb/api/facet/{query}?field=current_status")
    data = count_estimate_response.json()
    count_estimate = data.get("current_status", {}).get("rel", 0)   # REL is a status code meaning the entry has been publicly released. also the only status code this API request seems to return. Correct count in most cases, can be slightly off in some cases, but doesn't matter.   #! minor detail: return value for no counts is 0, could change it to a message like "No entries found!" That's what EMDB does.

    # Formatting search preview info into a dictionary
    preview_info = {
        'query': query,
        'hitCount': count_estimate,
        'preview': [{'emdb_id': entry.get('emdb_id', 'N/A'),
                     'title': entry.get('title', 'N/A'),
                     'resolution': entry.get('resolution', 'N/A')} for entry in entries]
    }
    return preview_info

# Example usage
if __name__ == "__main__":
    # from timeit import default_timer as timer

    # start = timer()
    query = "spliceosome AND resolution:[2 TO 4]"    # Example query
    results = preview_emdb(query)
    # end = timer()

    print(f"Query: {results['query']}")
    print(f"Total Results: {results['hitCount']}")
    print("Preview of First 10 Entries:")
    for entry in results['preview']:
        print(f"- {entry['emdb_id']}: {entry['title']}, resolution: {entry['resolution']}")

    # print(f"Runtime: {end - start} seconds")
