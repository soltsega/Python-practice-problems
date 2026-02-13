import json
file_name = 'C:/Users/My Device/Desktop/pythonWorkspace/file_management/jsonFile.json'
with open(file_name, 'r') as file:
    content = json.load(file)
    print(content)
print(file.closed) # checks whether the file is cloed or not