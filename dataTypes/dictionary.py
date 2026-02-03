# dicitonaries in python
# thery are used to store data values in a key: value pair
# they are unorderd and muable data types in python
# creatig a dictionary
my_dict = {
    "name" : "John",
    "age" : 30,
}

print(type(my_dict))  # <class 'dict'>
print("Dictionary:", my_dict)  # {'name': 'John', 'age': 30}  this will output all the keys and their value pairs

# methods to access te dictionary items
# 1. methods to acces all the keys and the values at once
def dictionary_operations():
    my_dict = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    print("Dictionary type:", type(my_dict))
    print("Dictionary items:", my_dict.items())  # returns a view object with key-value pairs
    print("Dictionary keys:", my_dict.keys())    # returns a view object with keys
    print("Dictionary values:", my_dict.values())  # returns a view object with values

    # 2. Accessing individual items
    print("Name:", my_dict["name"])  # Accessing value by key
    print("Age:", my_dict.get("age"))  # Accessing value using get() method

    # 3. Adding or updating items
    my_dict["email"] = "john@example.com"
    my_dict["age"] = 31  # updating age
    print("Updated Dictionary:", my_dict)

    # 4. Removing items: all the methods of removing iterms from a dictionary
    del my_dict["email"]  # removes the item with key 'email'
    removed_value = my_dict.pop("city")  # removes the item with key 'city'
    print("Removed city:", removed_value)
    print("Dictionary after removals:", my_dict)

    # which one of the removign method is most efficient in terms of performance
    my_dict.clear()  # removes all items from the dictionary
    print("Cleared Dictionary:", my_dict)
    del my_dict  # deletes the dictionary entirely
    # what is the difference between clear() and del keyword when removing items from a dictionary
    # clear() removes all items but keeps the dictionary object, del deletes the entire dictionary object