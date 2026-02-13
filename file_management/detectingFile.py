# Sometimes we will have too check whether the file really existis or not before we try to access it
import os  # a library that we use to access files
file_name = 'C:/Users/My Device/Desktop/pythonWorkspace/file_management/textFile.txt'

if os.path.exists(file_name):
    print('That location exists!')
    if os.path.isfile(file_name):
        print('That is a file')
    elif os.path.isdir(file_name):
        print("That is directory")
else:
    print('That location does not exist!')
