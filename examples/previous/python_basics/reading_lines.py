# How to read a txt doc line by line:


FILE_PATH = "../../../docs/_notes.txt"  # This is in the docs directory for example.
# The "../" goes back one directory
# "./" would be the current directory so ./_notes.txt would read the notes in the example directory.

with open(FILE_PATH, "r") as text_file:
    for each_line in text_file:
        print(each_line)