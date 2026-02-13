# This code reads the content of a text file and prints it to the console. It also checks if the file is closed after reading.
# We use the open() function to open the file in read mode ('r'). 
# The with statement ensures that the file is properly closed after its suite finishes, even if an exception is raised on the way. We then use the read() method to read the entire content of the file and print it. 
# Finally, we check if the file is closed using the closed attribute.
import json
file_name = 'C:/Users/My Device/Desktop/pythonWorkspace/file_management/textFile.txt'
with open(file_name, 'r') as file:
    content = file.read()
    print(content)
print(file.closed)

# read binary mode
file_name = 'C:/Users/My Device/Desktop/pythonWorkspace/file_management/textFile.txt'
with open(file_name, 'rb') as file:
    content = file.read()
    print(content)
print(file.closed)

# to red the first line only
file_name = 'C:/Users/My Device/Desktop/pythonWorkspace/file_management/textFile.txt'
with open(file_name, 'r') as file:
    content = file.readline()
    print(content)
print(file.closed)

# to read the file line by line
file_name = 'C:/Users/My Device/Desktop/pythonWorkspace/file_management/textFile.txt'
with open(file_name, 'r') as file:
    for line in file:
        print(line)