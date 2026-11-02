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

# Python Sets
# Python Fundamentals
#
# Python Sets
#
# Python Forensics, Inc.

print("\nPython Sets\n")

# Set Demonstration
print("Simple Demonstration of Sets in Python")
print("======================================")
print()

# Create an empty set
empty_set = set()
print("Empty Set", empty_set)
print()

# Create a set with initial values
set_a = {1,2,3,4}

print("set A = ",set_a)
print()

# Add a value to a set
set_a.add(5)
print("Added Value 5 to set A = ", set_a)
print()

# Create a new set B
set_b = {3,4,11,13,15,17}
print("set_b = ", set_b)
print()

# Create a union of two sets
set_c = set_a.union(set_b)
print("Union of Set A and B = ", set_c)
print()

# Create the intersection of two sets
set_d = set_a.intersection(set_b)

print("Intersection of Set A and B = ", set_d)
print()

case_a = {"Kevin Mitnick", "Jonathon James", "Kevin Poulsen", "Robert Morris"}
case_b = {"Kevin Poulsen", "Robert Morris", "Stephen Wozniak", "Richard Stallman"}
union_case_ab = case_a.union(case_b)
intersection_case_ab = case_a.intersection(case_b)


print("Suspects Case A =          ", case_a)
print("Suspects Case B =          ", case_b)
print("Union of Suspects =        ", union_case_ab)
print("Intersection of Suspects = ", intersection_case_ab)
print()

print("\nIterate through the union of suspects")
print("notice that the sort order has not changed")

for value in union_case_ab:
    print(value)
    
print()


new_list = list(union_case_ab)
new_list.sort()
print(new_list)

# Sorting a set

print("Sorted Set = ", sorted(union_case_ab))
print()

print("Because sets are unordered, only the output is sorted not the actual set")
print("This is fundamental to math, as sorting sets is irrelevant")
print("\nIterating through the union of suspects again yields the same result")
for value in union_case_ab:
    print(value)
    
print()

