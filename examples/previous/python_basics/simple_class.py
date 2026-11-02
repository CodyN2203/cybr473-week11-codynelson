'''
Simple Class Example
'''
from __future__ import print_function
import sys

class SystemInfo:
    ''' Simple SystemInfo Class that obtains
        the major python version and the
        operating system type
    '''
    def __init__(self):
        ''' Create object variables and Constants '''
        if sys.version_info[0] < 3:
            self.PYTHON_VERSION = 2
        else:
            self.PYTHON_VERSION = 3

        self.OS = sys.platform

    def print_sys_info(self):
        ''' Print out the system information '''
        print(f"Python Version #: {self.PYTHON_VERSION}")
        print(f"Operating System: {self.OS.capitalize()}")

sys_info = SystemInfo()              # create an object

print("-" * 50)
print("System Information Obtained by Accessing the Object:")
print(sys_info.PYTHON_VERSION)       # print the PYTHON_VERSION
print(sys_info.OS.capitalize())                   # print the OS
print("-" * 50)
print("System Information Obtained by calling the print method on the object:")
# Invoke the object print_sys_info Method
sys_info.print_sys_info()
print("-" * 50)
