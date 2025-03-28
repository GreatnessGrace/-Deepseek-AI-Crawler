import asyncio
import json

from utils.scraper_utils import fetch_github_results, extract_iocs_from_files
from utils.data_utils import save_iocs_to_csv


async def crawl_github_iocs():
    """
    Crawls GitHub for APT41-related IOCs and saves them.
    """
    results = fetch_github_results()
    if not results:
        print("No results found on GitHub.")
        return

    # Extract raw URLs of files
    file_urls = [item["html_url"].replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/") for item in results]
    
    # Extract IOCs
    ioc_data = extract_iocs_from_files(file_urls)

    if ioc_data:
        save_iocs_to_csv(ioc_data, "apt41_iocs.csv")
        print(f"Saved {len(ioc_data)} IOC files to 'apt41_iocs.csv'.")
    else:
        print("No IOCs extracted.")


async def main():
    await crawl_github_iocs()


if __name__ == "__main__":
    asyncio.run(main())
