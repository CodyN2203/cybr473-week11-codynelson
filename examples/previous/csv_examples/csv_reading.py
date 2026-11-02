"""
CSV Reading Example
"""

import csv

# Run the CSV Exporting Example First so this file exists.
input_file = "../docs/example-output.csv"

rows = []  # A list that will store each row as a dictionary

# Read from CSV
with open(input_file, "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    # Each row is an OrderedDict
    # (this behaves like a normal dict)
    for row in reader:
        rows.append(row)

# Print what we read
for row in rows:
    print(row)
