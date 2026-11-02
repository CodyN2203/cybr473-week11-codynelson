'''
Scripting Assignment #11 - Python PCAP Analysis

Please follow the general assignment submission guidelines in Guidelines.md

---

Scenario:

Following up on the sniffer you built for ChirpyHub last week, the security
team captured a full day of traffic from a suspicious host and saved it as
a set of PCAP files.

You have been asked to process these captures and turn them into something
the team can actually use: unique traffic flows, the busiest destinations,
and anything unusual worth flagging.

---

Task:


Create a Python script that reads a PCAP file from the pcap/ folder.
Use the pcap_reader_example.py as a starting baseline.
Adjust the script to perform the following:

Run it on PCAP-1.pcap for your submission. Your script should still work on any
file in the pcap/ folder, since the other files will be used for testing your code.

1) Count unique traffic by source and destination (by IP) (export to unique_flows.csv)
    Format as so:
    SRC | Dest | Count | PCAP File Name
2) Count the unique destinations per source (export to unique_destinations.csv)
    Format as so:
    SRC | Unique Dest Count | PCAP File Name

Then:

Export another CSV called pcap_data.csv

3) Track the largest packets (by byte_size) and identify what they are.
    - Explain in your reflection what they are or could be.
    - You don't have to call out what they are in your CSV unless this is something you calculate in Step 5.

4) Add at least four additional fields that are not already explored in the example.
	- Two can be something already available with Scapy
	- The other two fields must be something "calculated"
	    - This part should involve some additional research.
	    - Make sure you cite your sources.
		- One example of a calculated field is the manufacturer of the source or destination device.
	 	- You could use the MAC address and 3rd Party Libraries to find out.
	 	- If you do use an additional 3rd Party Library, make sure you explain clearly what it does, and add it to requirements.txt
5) Export the data to the pcap_data.csv in a neat way that would assist your cyber investigation.
6) Explain in docs/reflection.md what your results mean, which fields you added and why, and how did the data contribute to the investigation.

---

Submit:

1) Your Python script (this file edited)
2) reflection.md in the docs folder.
3) Your CSVs Exported to the docs folder.

'''