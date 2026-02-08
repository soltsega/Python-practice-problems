class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

my_object = MyClass("John", 30)
print(my_object.get_name())
my_object.set_name("Jane")
print(my_object.get_name())
print(my_object.get_age())
my_object.set_age(31)
print(my_object.get_age())



# They are used to store the state of an object
# can be getattr, setattr, hasattr and delattr
# getattr is used to get the value of an attribute. It returns the value of the attribute. It takes two parameters: the object and the attribute name
# setattr is used to set the value of an attribute. It takes three parameters: the object, the attribute name and the value(new value)
#      setattr(object, attribute_name, new_value). It returns None. It does not distinguish between existing and non-existing attributes. It will just overwrites it

# hasattris used to check whether an object has an attribute or not
#  - it returns boolean value

# delattr is used to delete an attribute. It retunrs None
#  - it taks two parameters: the object and the attribute name
# The parameters they take are the object and the attribute name
# attribute name means the name of the attribute
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

person = Person('John Doe', 30)
attribute_name = input("Enter the attribute name: ")

if hasattr(person, attribute_name):
    print(getattr(person, attribute_name))
else:
    print("Attribute not found")

# to delete the atribute if it is found
if hasattr(person, attribute_name):
    delattr(person, attribute_name)
else:
    print("Attribute not found")

# To set an attribute if it doesn't exist
if hasattr(person, attribute_name):
    print("Attribute already exists. We will update it")
    setattr(person, attribute_name, 'New value')
else:
    print("Attribute not found. We will create it")
    setattr(person, attribute_name, 'New value')