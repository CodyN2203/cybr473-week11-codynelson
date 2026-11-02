import os
import certifi

# Do this to avoid SSL Cert Issues
os.environ["SSL_CERT_FILE"] = certifi.where()
# It's done before importing VT which initializes some network settings

import hashlib
import vt # Virus Total
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("VIRUS_TOTAL_API_KEY")
if not API_KEY:
    raise ValueError("VIRUS_TOTAL_API_KEY not found in environment variables.")


SAMPLE = b"X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
SAMPLE_SHA256 = hashlib.sha256(SAMPLE).hexdigest()

file_hash = SAMPLE_SHA256

print("SHA-256:", file_hash)

print("\n-------------------")
print("Virus Total Summary")
print("-------------------")

with vt.Client(API_KEY) as client:
    try:
        vt_file_object = client.get_object(f"/files/{file_hash}")

        stats = vt_file_object.last_analysis_stats # Review Stats

        ai_analysis = vt_file_object.get("crowdsourced_ai_results")
        if ai_analysis:
            print("\n-------------------")
            print("AI Analysis Results")
            print("-------------------\n")
            print(f"{ai_analysis[0]["analysis"]}")

    except vt.error.APIError as e:
        print("VirusTotal APIError:", e)