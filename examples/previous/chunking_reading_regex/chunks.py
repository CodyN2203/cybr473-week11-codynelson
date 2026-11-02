"""
Working with Large Data in Chunks
"""

import re
from prettytable import PrettyTable


CHUNK_SIZE = 32 # Read it in Chunks of 32 for Testing Purposes
# you may want to consider a much larger size in your script

OVERLAP_SIZE = 16 # For Chunk Reading
# you may want to consider a much larger size in your script
# note it's smaller than the chunk size

GOOGLE_STRING = rb"google"
GMAIL_STRING = "gmail"
GMAIL_STRING_AS_BYTES = GMAIL_STRING.encode("ascii")

GOOGLE_PATTERN = re.compile(
    re.escape(GOOGLE_STRING) + rb'|' + re.escape(GMAIL_STRING_AS_BYTES),
    re.IGNORECASE # Ignores case!
)

data_counts = {}

# mem.raw is in D2L since it is a huge file
# DO NOT TRY TO COMMIT mem.raw To GitHub
# It will error out due to its size and will cause a pain when trying to fix it.
# I will not help you, you'll be on your own and possibly need to start again.
# You should however add it locally to test this


tail = b""  # This buffer stores the end of the previous chunk.
with open("../dumps/mem.raw", "rb") as binary_file:

    while True:
        chunk = binary_file.read(CHUNK_SIZE)
        if not chunk:
            break
        data_pattern = GOOGLE_PATTERN

        # Consider when reading chunk by chunk..
        # What if a data point starts at one chunk
        # and ends at another?
        # imagine Chunk 1 ends with: goo
        # Chunk 2 starts with: gle
        # We'd get some sloppy results right?

        combined = tail + chunk # Attach tail to new chunk
        tail_len = len(tail)


        for match in data_pattern.finditer(combined):
            # ignore matches fully inside the old tail
            if match.end() <= tail_len:
                continue

            data = match.group(0)
            cleaned_data = data.lower()
            data_counts[cleaned_data] = data_counts.get(cleaned_data, 0) + 1

        tail = combined[-OVERLAP_SIZE:]


# Test What if we didn't process chunk overlaps?
# with open("../dumps/mem.raw", "rb") as binary_file:
#
#     while True:
#         chunk = binary_file.read(CHUNK_SIZE)
#         if not chunk:
#             break
#
#         data_pattern = GOOGLE_PATTERN
#
#         for data in data_pattern.findall(chunk):
#             cleaned_data = data.lower()
#             data_counts[data] = data_counts.get(cleaned_data, 0) + 1

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

