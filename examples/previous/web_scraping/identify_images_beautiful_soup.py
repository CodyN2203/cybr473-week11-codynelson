"""
Download all images from a webpage using BeautifulSoup + requests.
"""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = "https://www.python.org"
HEADERS = {"User-Agent": "Mozilla/5.0 (Teaching Example)"}
OUTPUT_DIR = "../../../images"

# Ensure output folder exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

try:
    response = requests.get(URL, headers=HEADERS, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    images = soup.find_all("img")
    for img in images:
        img_url = urljoin(URL, img.get("src", ""))
        img_name = os.path.basename(img_url.split("?")[0]) or "unnamed.jpg"

        try:
            img_response = requests.get(img_url, headers=HEADERS, timeout=10)
            img_response.raise_for_status()

            # Save to disk
            filepath = os.path.join(OUTPUT_DIR, img_name)
            with open(filepath, "wb") as f:
                f.write(img_response.content)
            print(f"Saved {img_name}")

        except requests.RequestException as e:
            print(f"Failed to download {img_url}: {e}")

except requests.RequestException as e:
    print(f"Error fetching {URL}: {e}")

print("\nScript Complete")