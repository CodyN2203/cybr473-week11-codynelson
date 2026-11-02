"""
Extract image URLs and alt text from a webpage using BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = "https://www.python.org"

HEADERS = {"User-Agent": "Mozilla/5.0 (Teaching Example)"}

try:
    response = requests.get(URL, headers=HEADERS, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    images = soup.find_all("img")
    for img in images:
        img_url = urljoin(URL, img.get("src", ""))   # safe URL joining
        alt_text = img.get("alt", "No alt text")     # avoids KeyError
        print("Image URL:", img_url)
        print("Alt text:", alt_text)
        print()

except requests.RequestException as e:
    print(f"Error fetching {URL}: {e}")

print("\nScript Complete")