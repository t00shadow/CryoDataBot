# does it by scraping html

from timeit import default_timer as timer

import requests
from bs4 import BeautifulSoup

def get_total_count_from_web(query):
    # Build the URL for the search page
    search_url = f"https://www.ebi.ac.uk/emdb/emsearch/?q={query}"

    # Send the GET request to the website
    response = requests.get(search_url)
    
    if response.status_code != 200:
        print(f"Error fetching page: {response.status_code}")
        return None
    
    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the span element with the result count text
    result_text = soup.find('span', class_='results_header_text')

    if result_text:
        # Extract the text like "Showing 1 - 10 of 535. Page 1 of 54"
        text = result_text.get_text()
        # print(text)
        
        # Extract the total count (e.g., 535 from "Showing 1 - 10 of 535. Page 1 of 54")
        total_count = text.split(".")[0].split("of")[-1].strip()        # splits at period, then takes left side, then splits at "of" and right side. split removes spaces before and after (actually worked without split, but just keep it)
        # print(total_count)
        return int(total_count)
    else:
        print("Error: Could not find the result count on the page.")
        return None

# Example usage
if __name__ == "__main__":
    start = timer()
    query = ""
    total_hits = get_total_count_from_web(query)
    end = timer()

    if total_hits is not None:
        print(f"Total Results: {total_hits}")

    print(f"Runtime: {end - start} seconds")
