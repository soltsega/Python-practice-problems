# Exclusive Creation
# ------------------
# WE use the 'x' mode in the open() function to create a new file.
# If the file already exists, it raises a FileExistsError.
import os
from turtle import fd

file_name = 'C:/Users/My Device/Desktop/pythonWorkspace/file_management/textFile.txt'
with open(file_name, 'x') as f:
    f.write("This is a sample text file.")
