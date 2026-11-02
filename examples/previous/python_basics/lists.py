'''
Copyright (c) 2019 Python Forensics, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.

'''
from __future__ import print_function
#
# Experimenting with 
# Python Lists
# Python Fundamentals
#
# Python Forensics, Inc.
#
print("\nLab-3 Python Lists\n")

# List Demonstration

print("Simple Demonstration of Lists in Python")
print("=======================================")
print()

# Create an empty list
empty_list = []

print("Empty List ", empty_list)
print()

# Create a list with initial values
test_list = ['Suspect', 'Witness', 'Victim']
print("Initialized List ",test_list)
print()

# Append a value to a list
test_list.append("Accomplice")
print("Appended List ",test_list)
print()

# Insert a value into the list
test_list.insert(2, "Informant")
print("Inserted List ", test_list)
print()

# Pop a value off the list
pop_value = test_list.pop()
print("Value Popped from List ",pop_value)
print("New List ", test_list)
print()

# Iterate through the list
print("Iterate through the list")
for value in test_list:
    print(value)

print()

# Sorting a list

test_list.sort()
print("Sorted List = ", test_list)
print()

# A more complex List

complex_list = ["John Doe", ["Age", 50], ["Height", 5, 6]]
for each_item in complex_list:
    print(each_item)

for each_item in complex_list:
    if type(each_item) == list:
        for each_value in each_item:
            print(each_value, end=" ")
        print
    else:
        print(each_item)
