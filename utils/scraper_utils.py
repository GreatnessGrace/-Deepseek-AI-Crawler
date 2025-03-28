import json
import requests
from typing import List, Dict

from config import BASE_URL, HEADERS


def fetch_github_results() -> List[Dict]:
    """
    Fetches search results from GitHub API for APT41 IOCs.

    Returns:
        List[Dict]: A list of files containing potential IOCs.
    """
    print(f"Fetching data from GitHub: {BASE_URL}")
    response = requests.get(BASE_URL, headers=HEADERS)

    if response.status_code != 200:
        print(f"Error: GitHub API returned {response.status_code}")
        return []

    data = response.json()
    return data.get("items", [])  # List of code search results


def extract_iocs_from_files(file_urls: List[str]) -> List[Dict]:
    """
    Extracts IOCs from raw file URLs found in GitHub search.

    Args:
        file_urls (List[str]): List of raw URLs of files containing IOCs.

    Returns:
        List[Dict]: Extracted IOC data.
    """
    iocs = []

    for url in file_urls:
        print(f"Fetching IOC file: {url}")
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            print(f"Error fetching {url}: {response.status_code}")
            continue

        content = response.text
        # Attempt to parse JSON, otherwise store raw content
        try:
            ioc_data = json.loads(content)
            iocs.append(ioc_data)
        except json.JSONDecodeError:
            iocs.append({"raw_text": content})

    return iocs
