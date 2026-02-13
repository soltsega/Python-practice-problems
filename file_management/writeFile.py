import json
text = 'my name is solomon and I am the CEO of this company'
file_name = 'C:/Users/My Device/Desktop/pythonWorkspace/file_management/textFile.txt'
# with open(file_name, 'w') as file:  #this will overwr as ite the content that is already there. we have to change the mode if we want to append
with open(file_name, 'a') as file:
    file.write(text)

