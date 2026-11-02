'''
Hash File Class/Object and usage example
'''
from __future__ import print_function

import hashlib
import os
import sys
import time

class FileHasher:

    def __init__(self):
        ''' Create object variables and Constants '''
        self.file_path = ''
        self.file_size = ''
        self.modified_time = ''
        self.create_time = ''
        self.file_hash = ''
        self.hash_type = ''
        self.VALID_HASH_TYPES = ['MD5', 'SHA1', 'SHA256', 'SHA512']
        self.last_err = ''

    def set_file_path(self, file_path):
        ''' Set the file path if valid
            Obtain file size and timestamps
            return True if valid and set the self.file_path object variable
        '''
        if os.path.isfile(file_path):
            if os.access(file_path, os.R_OK):
                self.file_path = file_path
                stats = os.stat(self.file_path) # Check Out https://docs.python.org/3/library/os.html#os.stat
                self.file_size = stats.st_size
                self.modified_time = time.ctime(stats.st_mtime)
                self.create_time       = time.ctime(stats.st_atime)
                self.last_err = ''
                return True
            else:
                self.file_path = ''
                self.last_err = 'Invalid File Path'
                return False

    def set_hash_type(self, hash_type):
        ''' Set the Hash Type verify it is supported '''
        if hash_type in self.VALID_HASH_TYPES:
            self.hash_type = hash_type
            self.last_err = ''
            return True
        else:
            self.hash_type = ''
            self.last_err = 'Invalid Hash Type'
            return False

    def __initialize_hash_object(self):

        if self.hash_type == 'MD5':
            self.hash_obj = hashlib.md5()
        elif self.hash_type == 'SHA1':
            self.hash_obj = hashlib.sha1()
        elif self.hash_type == 'SHA256':
            self.hash_obj = hashlib.sha256()
        elif self.hash_type == 'SHA512':
            self.hash_obj = hashlib.sha512()
        else:
            self.hash_obj = hashlib.md5()

    def hash_file(self):
        ''' Using the object variables hash the file '''
        try:
            if self.hash_type:
                self.__initialize_hash_object()
            else:
                self.last_err = 'Hash Type not Set'
                return False
            with open(self.file_path, 'rb') as file_to_hash:
                file_contents = file_to_hash.read()
                self.hash_obj.update(file_contents)
                self.file_hash = self.hash_obj.hexdigest()
                self.last_err = ''
                return True
        except Exception as err:
            self.last_err = str(err)
            return False
