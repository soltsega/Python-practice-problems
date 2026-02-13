# Working with JSON files and data in Python
# JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. In Python, we can work with JSON files using the built-in json module.
# The json module provides two main functions for working with JSON data: json.load() and json.dump(). The json.load() function is used to read JSON data from a file and convert it into a Python object, while the json.dump() function is used to write a Python object to a file in JSON format.
# To read a JSON file, we can use the following code:
import json

with open('C:/Users/My Device/Desktop/pythonWorkspace/file_management/jsonFile.json', 'r') as file:
    data = json.load(file)
    print(data)
# In this code, we open the JSON file in read mode ('r') and use the json.load() function to read the data from the file and convert it into a Python object (in this case, a dictionary). We then print the data to the console.
# To write a Python object to a JSON file, we can use the following code:
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open('C:/Users/My Device/Desktop/pythonWorkspace/file_management/jsonFile.json', 'w') as file:
    json.dump(data, file)
# In this code, we create a Python object (in this case, a dictionary) and use the json.dump() function to write it to a JSON file in write mode ('w'). 


# We can also use the json.dumps() function to convert a Python object into a JSON string, and the json.loads() function to convert a JSON string into a Python object. For example:
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(data)
print(json_string)
# In this code, we create a Python object (in this case, a dictionary) and use the json.dumps() function to convert it into a JSON string. We then print the JSON string to the console.
json_data = '{"name": "John", "age": 30, "city": "New York"}'
python_data = json.loads(json_data)
print(python_data)
# In this code, we create a JSON string (in this case, a dictionary) and use the json.loads() function to convert it into a Python object. We then print the Python object to the console.

# In summary, the json module in Python provides a simple and efficient way to work with JSON data. We can use the json.load() and json.dump() functions to read and write JSON data from and to files, and the json.dumps() and json.loads() functions to convert between Python objects and JSON strings.