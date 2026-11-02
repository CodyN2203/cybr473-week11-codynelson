"""
Fetch a web page using Python's requests library and print the HTML.
"""

import requests

URL = "http://quotes.toscrape.com"
HEADERS = {"User-Agent": "Mozilla/5.0 (Teaching Example)"}

try:
    response = requests.get(URL, headers=HEADERS, timeout=10)
    response.raise_for_status()  # ensures status == 200
    print(response.text)
except requests.RequestException as e:
    print(f"Error fetching {URL}: {e}")

print("\nScript Complete")
