'''
Copyright (c) 2019 Python Forensics -
With Some Updates By Rodolfo Madero @ University of Arizona 2026

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.
'''
from __future__ import print_function

# Using the Python Hashing Module

# Importing Modules

import os           # Std Lib OS Module
import hashlib      # Std Lib Hashing Module

# Read current directory contents
# into a list

DIRECTORY_TO_HASH = "../.."
files_to_hash = os.listdir(DIRECTORY_TO_HASH)

# Loop through each file
for each_file in files_to_hash:
    full_path = os.path.join(DIRECTORY_TO_HASH, each_file)
    # Validate that the each entry is
    # a file (i.e. not a directory or link)
    # and we have proper rights to read the file
    if os.path.isfile(full_path):
        if os.access(full_path, os.R_OK):
            try:
                # Attempt to open the file
                with open(full_path, "rb") as the_file:
                    # Create a new hashing object
                    hash_obj = hashlib.sha256()
                    chunk_size = 2**16
                    # Now read in the file in chunks
                    # and hash each chunk
                    while True:
                        chunk = the_file.read(chunk_size)
                        # if we still have data
                        # keep updating the hash
                        if len(chunk) > 0:
                            hash_obj.update(chunk)
                        # otherwise we are finished hashing
                        else:
                            print(each_file, hash_obj.hexdigest())
                            break
            except Exception as e:
                print(each_file, "Hashing Failed:", e)
    else:
        print(each_file, "Not a File")
