"""
Quick dictionary example
Counting word occurrences
"""

# Used only for Type Checking
from typing import Dict, Any

# Open the text of Alice in Wonderland
with open("../texts/carroll-alice.txt") as file:
    # Replace Double hyphens/ Em Dashes with spaces first
    words = file.read().replace("--", " ").split()

word_counts = {} # Create an Empty Dictionary

for word in words: # Go through each word
    normalized = word.lower() # Lowercase it to normalize
    normalized = normalized.strip("[].(),:;\"'-!?") # Remove Symbols at start and end
    word_counts[normalized] = word_counts.get(normalized, 0) + 1 # Increment word count

items = list(word_counts.keys())

first_five = items[:5]
last_five = items[-5:]

print("First Five Words:", ", ".join(first_five))
print("Last Five Words: ", ", ".join(last_five))

print(items[:10])
print(items[-10:])

print("\nFirst 100 Words")
for entry in items[:100]:
    print(entry)

print("\nLast 100 Words")
for entry in items[-100:]:
    print(entry)

# Sort a dictionary

# This code is explained in more depth here:
# https://www.geeksforgeeks.org/python/python-sort-python-dictionaries-by-key-or-value/

# This does what sort_dict_by_value does in one line:
sorted_dict = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))
# See Below for more details

print(sorted_dict)

print("\nend script")


def sort_dict_by_value(unsorted_dictionary : Dict[Any, Any]):
    """
    Takes a dictionary `d` and returns a new dictionary
    sorted by values from largest to smallest.
    """

    # Step 1: Turn dictionary into a list of (key, value) pairs
    items = list(unsorted_dictionary.items())

    # Example: {"Joe":3, "Alice":7} -> [("Joe",3), ("Alice",7)]

    # Step 2: Define a function to get the value from a pair
    def get_value(pair):
        # pair is a tuple like ("apple", 3)
        return pair[1]  # return the number (value) # this is what the lambda does above

    # Step 3: Sort the list of pairs by value, biggest first
    sorted_items = sorted(items, key=get_value, reverse=True)
    # Example: [("Joe",3), ("Alice",7)] → [("Alice",7), ("Joe",3)]

    # Step 4: Turn the sorted list of pairs back into a dictionary
    sorted_dict = dict(sorted_items)

    # Step 5: Return the sorted dictionary
    return sorted_dict


## Lambdas Explained

## Imagine you have:
def add_one(x):
    return x + 1

## You can write that as:
lambda x: x + 1

numbers = [1, 2, 3]
squares = list(map(lambda x: x**2, numbers))

# map maps each item in the list to a new list
# Resulting in [1, 4, 9]