''' 
PrettyTable Usage example

'''
from prettytable import PrettyTable
import os

# Create a tbl object that also defines the headings
tbl = PrettyTable(['FilePath','FileSize'])

DIR = '..'
file_list = os.listdir(DIR)
for each_file in file_list:
    file_path = os.path.join(DIR, each_file)
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        tbl.add_row( [ file_path, file_size] )                    

tbl.align = "l" 
result_string = tbl.get_string(sortby="FileSize", reversesort=True)
print(result_string)

