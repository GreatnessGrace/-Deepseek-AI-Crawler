# config.py

# BASE_URL = "https://www.theknot.com/marketplace/wedding-reception-venues-atlanta-ga"
# CSS_SELECTOR = "[class^='info-container']"
# REQUIRED_KEYS = [
#     "name",
#     "price",
#     "location",
#     "capacity",
#     "rating",
#     "reviews",
#     "description",
# ]
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get token from environment variable
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

BASE_URL = "https://api.github.com/search/code?q=APT41+IOC"
HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {GITHUB_TOKEN}",
}
