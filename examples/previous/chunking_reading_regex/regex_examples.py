"""
Using Regular Expressions to Find e-mails
"""

import re
from prettytable import PrettyTable


CHUNK_SIZE = 4096 # Read it in Chunks of 4096

EMAIL_PATTERN = re.compile(
    rb"[a-z]+@[a-z]+\.[a-z]{2,4}"
)

URL_PATTERN = re.compile(rb'(?:https?:\/\/)?(?:www\.)?[a-z]+\.(?:com|org|gov)')

data_counts = {}

# mem.raw is in D2L since it is a huge file
# DO NOT TRY TO COMMIT mem.raw To GitHub
# It will error out due to its size and will cause a pain when trying to fix it.
# I will not help you, you'll be on your own and possibly need to start again.
# You should however add it locally to test this

with open("../dumps/mem.raw", "rb") as binary_file:

    while True:
        chunk = binary_file.read(CHUNK_SIZE)
        if not chunk:
            break

        # data_pattern = URL_PATTERN
        data_pattern = EMAIL_PATTERN

        for data in data_pattern.findall(chunk):
            cleaned_data = data.lower()
            data_counts[data] = data_counts.get(cleaned_data, 0) + 1


data_table = PrettyTable(["Occurrences", "Data Point"])
data_table.align = "l"

for info, count in data_counts.items():
    data_table.add_row([count, info.decode("ascii", "ignore")])

print("Data Point: Sorted by Occurrence")

# Pretty Table Has a Sort Option!
print(data_table.get_string(sortby="Occurrences", reversesort=True))
print()

# Pretty Table also has a CSV Export Function that can make life easier!

# Get CSV text
csv_text = data_table.get_csv_string(sortby="Occurrences", reversesort=True)

# Write to a file
CSV_TARGET = "../docs/test_output.csv"

with open(CSV_TARGET, "w", newline="") as file:
    file.write(csv_text)

print(f"Table Successfully Exported to {CSV_TARGET}")

