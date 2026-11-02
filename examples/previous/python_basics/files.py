'''
Copyright (c) 2019 Python Forensics

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.
'''
from __future__ import print_function

# Exploiting the Python OS module

#
# Python Forensics, Inc.

# Importing Modules

import os                   # Std Library OS Module
from time import ctime      # Std Library Time import
                            # just the ctime method

# Examples of some key methods 

# get the current working directory
print("Current Working Directory")
print(os.getcwd())

print("=========================================\n")

# Get the filenames in the current directory
# and store them in a list
print("List of File Names")
file_list = os.listdir("../..")

# print(each filename 
for each_file in file_list:
    print(each_file)

print("=========================================\n")

# Determine the type of each file in the list
# and print(each type and filename
print("File and Type")
for each_file in file_list:
    if os.path.isdir(each_file):
        print("DIR:  ", each_file)
    elif os.path.isfile(each_file):
        print("FILE: ", each_file)
    elif os.path.islink(each_file):
        print("LINK: ", each_file)
    elif os.path.ismount(each_file):
        print("MNT:  ", each_file)
    else:
        print("UNKNOWN: ", each_file)
        
print("=========================================\n")
        
# Store the file details in a list
# then sort the resulting list and then
# print the results

print("Store File Details in a List, Sort and Print")
file_details = []
for each_file in file_list:
    if os.path.isdir(each_file):
        file_details.append(["DIR:  ", each_file])
    elif os.path.isfile(each_file):
        file_details.append(["FILE: ", each_file])
    elif os.path.islink(each_file):
        file_details.append(["LINK: ", each_file])
    elif os.path.ismount(each_file):
        file_details.append(["MNT:  ", each_file])

file_details.sort()

for each_item in file_details:
    print(each_item)

print("=========================================\n")

# Obtain additional file details 
# Store the file details in a list
# then sort the resulting list and print
# the results

print("Extract additional file details")

file_details = []
for each_file in file_list:
    
    stats = os.stat(each_file)
    m_time = stats.st_mtime
    m_time = ctime(m_time)
    f_size = stats.st_size
            
    if os.path.isdir(each_file):
        file_details.append(["DIR:  ", each_file, f_size, m_time])
    elif os.path.isfile(each_file):
        file_details.append(["FILE: ", each_file, f_size, m_time])
    elif os.path.islink(each_file):
        file_details.append(["LINK: ", each_file, f_size, m_time])
    elif os.path.ismount(each_file):
        file_details.append(["MNT:  ", each_file, f_size, m_time])

file_details.sort()

for each_item in file_details:
    print(each_item)

print("=========================================\n")

print("Walk a the Path and print the relative path")
# Use the os.walk method to walk the path from
# root to bottom

my_root = "."
for root, dirs, files in os.walk(my_root):

    # Walk the path from top to bottom.
    # For each file obtain the filename 
    # and print the relative path
    
    for file in files:
        relative_path = os.path.join(root, file)
        print(relative_path)
        
