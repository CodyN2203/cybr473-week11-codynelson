'''
Hash File Functions and usage example
'''
from __future__ import print_function
import hashlib
import sys

def hash_file(file_path):
    '''
        function takes one input a valid file_path
        returns the hexdigest of the file
        or error
    '''
    try:
        with open(file_path, 'rb') as file_to_hash: # Note that 'rb" is opening the file in binary mode
            file_contents = file_to_hash.read()
            hash_obj = hashlib.md5()
            hash_obj.update(file_contents)
            digest = hash_obj.hexdigest()
            return digest
    except Exception as err:
        return str(err)

print("Hash File Function Demonstration")

file_name = input("Enter file to hash: ")

hex_digest = hash_file(file_name)
print(hex_digest)
