"""
CSV Exporting Example
"""

import csv

HEADERS = ["Type", "News"] # Set My Headers

# Let's say your data is not in a neat location
text = "Violent Python is the best course I ever took."
real = True

text_2 = "Violent Python is not fun."
real_2 = False


rows = [] # Rows to be added to the csv

row_1 = {} # Create an empty row dictionary

# Add the data
row_1['Type'] = "Real" if real else "Fake"
row_1['News'] = text
rows.append(row_1)

row_2 = {'Type': "Real" if real_2 else "Fake", 'News': text_2} # Create the row in one line
rows.append(row_2)

# Define CSV output file
output_file = "../docs/example-output.csv"  # Notice the Relative Path to Docs

# Write to CSV
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = HEADERS
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

print(f"results written to {output_file}")

# If you plan ahead an ensure your data is in a neat output, you can save a bunch of steps
# Some Dummy Data - a list of dictionaries

news_with_labels = [
    {
        "Type": "Real",
        "News": "Violent Python is the best course I ever took.",
    },
    {
        "Type": "Fake",
        "News": "Violent Python is not fun."
    },
]


output_file = "../docs/example-output2.csv"

# Write to CSV
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = HEADERS
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for news in news_with_labels:
        writer.writerow(news)

print(f"results written to {output_file}")
