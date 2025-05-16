# Seems you cant get the total number of search results easily. idk why, lowkey scraping the website would be faster.
# For a preview, I only want the first 10 results. But I also want the number of total search hits. 
# Approach 1: 2 separate https requests.
# - first request asks for minimal metadata (just emdb_id)
# - second request asks for first 10 rows on page 1, aka first 10 results, with a little more metadata, such as the title, and resolution maybe.
#
# Approach 2: just request all entries will all the metadata i need (will only be 2 to 3 fields tho).
#
# So debate is is a 2nd https request faster, or sending at minimum double the data. the Titles are much longer than the emdb_ids. so even triple would be a safe lowerbound estimate.
#
# To find out, benchmark the two. Tho EMDB might tell you to slow down.

# Both scale with the number of search results which is bad. Grabbing the first 10 entries is constant relative to the query (tests below show it). So just missing a better way to get total count, which the database prob already calculates
# EDIT: tested it in another script by scraping the html of the site and it's deadass faster. And it's constant time too cuz the site loading is prob slower than the actual database query. ~1.85 - 2.5 seconds. So combined with the 0.67 for fetching first 10 samples, it would be about 2.5-3.3 seconds for any query.
# regarding the webscraping approach, the first page already shows you the preview of the first 10 results, so you might just parse the html instead of making a 2nd request thru the API.
# ^ this is practically CONSTANT time (call it Approach 1.1)
# EDIT 2: nvm found a better solution than scraping the html. Use this request: "https://www.ebi.ac.uk/emdb/api/facet/{query}?field=current_status" Combined with the 0.67 for fetching first 10 samples, it's like 1.4-16 seconds which makes sense since it's essentially the same size request, if not smaller. so should approximately double the time of just fetching the first 10 samples alone. But anyways, the combined time of these 2 https requests is faster than scraping the site's html for the total count alone. So it's easily better.
# ^ this is also practically CONSTANT time, but a better CONSTANT time (call it Approach 1.2)


from timeit import default_timer as timer

import requests
import urllib.parse

# Approach 0: Constant in query complexity. Needs a better way to fetch the total count tho, or just forget about it, since it's not worth the extra delay.
# Runtime: constant, ~0.67 seconds             
def preview_emdb_approach0(query, rows=10, page=1, fl="emdb_id,title,resolution"):
    """
    Search EMDB and return a preview. Return the first 10 entries (EMDB ID and title) and the total count of results.

    Parameters:
        query (str): The search query (e.g., "spliceosome")
        rows (int): Number of entries per page (default 10)
        page (int): Current page (default 1)
        fl (string): List of fields to be shown (CSV exclusive). (default: emdb_id,title,resolution)
    
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
    
    # Formatting search preview info into a dictionary
    preview_info = {
        'query': query,
        'hitCount': len(entries),
        'preview': [{'emdb_id': entry.get('emdb_id', 'N/A'),
                     'title': entry.get('title', 'N/A'),
                     'resolution': entry.get('resolution', 'N/A')} for entry in entries]
    }
    return preview_info



# Approach 1:
# Runtime: scales with number of search results
def preview_emdb_approach1(query, preview_rows=10, page=1, fl="emdb_id,title,resolution"):
    """
    Search EMDB and return a preview. Return the first 10 entries (EMDB ID and title) and the total count of results.

    Parameters:
        query (str): The search query (e.g., "spliceosome")
        rows (int): Number of entries per page (default 10)
        page (int): Current page (default 1)
        fl (string): List of fields to be shown (CSV exclusive). (default: emdb_id,title,resolution)
    
    Returns:
        dict: Contains total hits and the first 10 entries with their names.
    """
    base_url = "https://www.ebi.ac.uk/emdb/api/search/"
    encoded_query = urllib.parse.quote(query)
    request_url = f"{base_url}{encoded_query}"
    params = {
        "rows": preview_rows,
        "page": page,
        "fl": fl,
    }

    # first request for count only, no extra fields
    response = requests.get(request_url, params={"rows": 9999999}, headers={'Accept': 'text/csv'})
    result_count = len(response.text.splitlines()) - 1      # first line is the list of (metadata) fields

    # second request for first 10 results with desired additional fields
    response = requests.get(request_url, params=params, headers={'Accept': 'text/csv'})     # overwrite the response variable since dont need the first requests data anymore

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
    
    # Formatting search preview info into a dictionary
    preview_info = {
        'query': query,
        'hitCount': result_count,
        'preview': [{'emdb_id': entry.get('emdb_id', 'N/A'),
                     'title': entry.get('title', 'N/A'),
                     'resolution': entry.get('resolution', 'N/A')} for entry in entries]
    }
    return preview_info



### Approach 2
# Runtime: scales with number of search results
def preview_emdb_approach2(query, preview_rows=10, fl="emdb_id,title,resolution"):
    """
    Search EMDB and return a preview. Return the first 10 entries (EMDB ID and title) and the total count of results.

    Parameters:
        query (str): The search query (e.g., "spliceosome")
        rows (int): Number of entries per page (default 10)
        page (int): Current page (default 1)
        fl (string): List of fields to be shown (CSV exclusive). (default: emdb_id,title,resolution)
    
    Returns:
        dict: Contains total hits and the first 10 entries with their names.
    """
    base_url = "https://www.ebi.ac.uk/emdb/api/search/"
    encoded_query = urllib.parse.quote(query)
    request_url = f"{base_url}{encoded_query}"
    params = {
        "rows": 9999999,
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
    
    # Formatting search preview info into a dictionary
    preview_info = {
        'query': query,
        'hitCount': len(entries),
        'preview': [{'emdb_id': entry.get('emdb_id', 'N/A'),
                     'title': entry.get('title', 'N/A'),
                     'resolution': entry.get('resolution', 'N/A')} for entry in entries[:preview_rows]]
    }
    return preview_info



# Approach 1.1. Improvement on approach 1, constant time total count. Scrapes website's html to get count. Slightly Slower for small queries, but the tradeoff is it's constant time (constant time since the database query is much faster than the https request and the html scraping).
# Runtime: constant, ~2.5 - 3.3 seconds
from preview_count_results_UNUSED import get_total_count_from_web
def preview_emdb_approach1_1(query, rows=10, page=1, fl="emdb_id,title,resolution"):
    """
    Search EMDB and return a preview. Return the first 10 entries (EMDB ID and title) and the total count of results.

    Parameters:
        query (str): The search query (e.g., "spliceosome")
        rows (int): Number of entries per page (default 10)
        page (int): Current page (default 1)
        fl (string): List of fields to be shown (CSV exclusive). (default: emdb_id,title,resolution)
    
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
    
    total_hits = get_total_count_from_web(query)

    # Formatting search preview info into a dictionary
    preview_info = {
        'query': query,
        'hitCount': total_hits,
        'preview': [{'emdb_id': entry.get('emdb_id', 'N/A'),
                     'title': entry.get('title', 'N/A'),
                     'resolution': entry.get('resolution', 'N/A')} for entry in entries]
    }
    return preview_info



# Approach 1.2. Improvement on approach 1, constant time. Uses https://www.ebi.ac.uk/emdb/api/facet/{query}?field=current_status to request the count. Count may be slightly off for some queries* but more than good enough for an estimate. UNEQUIVOCALLY the best version. Half the speed of Approach 1.1. Seems like an https request is at least half a second (500 ms). Makes sense. Seems like the fastest this can get since the entry and total count data come from two dif endpoints on the emdb server (/emdb/api/search/{query} and /emdb/api/facet/{query}). Also approach 1.1 also uses 2 https requests, so this totally kills the need for approach 1.1.
# *This API request only returns the number of entries with "current_status" as "REL", or publicly released. In most cases, this is a nonissue. The one case I noticed a dif, is when you query the entire database. But regardless it doesnt matter, since no files are downloaded by this function. It's merely a search preview for queries.
# Runtime: constant, ~1.4 seconds
def preview_emdb_approach1_2(query, rows=10, page=1, fl="emdb_id,title,resolution"):
    """
    Search EMDB and return a preview. Return the first 10 entries (EMDB ID and title) and the total count of results.

    Parameters:
        query (str): The search query (e.g., "spliceosome")
        rows (int): Number of entries per page (default 10)
        page (int): Current page (default 1)
        fl (string): List of fields to be shown (CSV exclusive). (default: emdb_id,title,resolution)
    
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
    count_estimate = data["current_status"]["rel"]       # REL is a status code meaning the entry has been publicly released. also the only status code this API request seems to return

    # Formatting search preview info into a dictionary
    preview_info = {
        'query': query,
        'hitCount': count_estimate,
        'preview': [{'emdb_id': entry.get('emdb_id', 'N/A'),
                     'title': entry.get('title', 'N/A'),
                     'resolution': entry.get('resolution', 'N/A')} for entry in entries]
    }
    return preview_info



# Benchmarking
if __name__ == "__main__":
    start = timer()
    # query = "spliceosome AND resolution:[2 TO 4]"        # 381 results, Approach 2 faster. Count matches site.
    # query = "ribosome AND resolution:[2 TO 4]"           # 2651 results, Approach 2 faster. Count discrepancy, script says 2659, site says 2651
    # query = "ribosome"                                   # 4464 results, Approach 2 faster. Count discrepancy, script says 4415, site says 4464
    query = ""                                           # 57994 results, About the same. Count discrepancy, script says 57994, site says 60118. Also "" is equivalent to "*"
    # results = preview_emdb_approach1(query)
    # results = preview_emdb_approach2(query)
    # results = preview_emdb_approach0(query)
    # results = preview_emdb_approach1_1(query)    # improved version of approach 1, closer to approach 0 in code and time complexity
    results = preview_emdb_approach1_2(query)    # improved version of approach 1, closer to approach 0 in code and time complexity
    end = timer()

    print(f"Query: {results['query']}")
    print(f"Total Results: {results['hitCount']}")
    print("Preview of First 10 Entries:")
    for entry in results['preview']:
        print(f"- {entry['emdb_id']}: {entry['title']}, resolution: {entry['resolution']} ")

    print(f"Runtime: {end - start} seconds")


# Results:
# For basically all queries, approach 2 is faster. Approach 1 essentially adds ~0.67 seconds. So essentially getting the first 10 results for any query should take about that long.
# Only when you query the entire EMDB, does approach 1 equal approach 2, so approach 2 is better. HOWEVER, IF can get the count a different way, approach 1 is better. Or if you dont care about the count.
# ALSO, if add addtional metadata fields, i'd imagine Approach 2 would get slower. Tho i think emdb_id, title, and resolution are all you need for a preview/sanity check.

# added appraoch 0 which is just the same as appraoch 1 minus getting the total count.
