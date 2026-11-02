import requests
import hashlib
import json

# Import the .env loader
from dotenv import load_dotenv
import os

# Load from .env file
load_dotenv()

API_KEY = os.getenv("VIRUS_TOTAL_API_KEY")

# Test file content (EICAR test file)
SAMPLE = b"X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
SAMPLE_SHA256 = hashlib.sha256(SAMPLE).hexdigest()
SAMPLE_MD5 = hashlib.md5(SAMPLE).hexdigest()

# VirusTotal file report API endpoint
url = f"https://www.virustotal.com/api/v3/files/{SAMPLE_SHA256}"

# Set headers
headers = {
    "x-apikey": API_KEY
}

# Make the request
response = requests.get(url, headers=headers)

# Print the response in a readable JSON format
if response.status_code == 200:
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Error: {response.status_code}, Message: {response.text}")
