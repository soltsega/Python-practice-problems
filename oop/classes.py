# classes in python
# classes are blueprints of the objects or instances of classes

# classes in python
# classes are blueprints of the objects or instances of classes

# class syntax
# class MyClass:
#     <statement(s)>
# the class keyword is used to define a class
# the class name must start with a capital letter
# the class name can contain letters, numbers and underscores
# the class name should be a noun

# class body
# the class body contains the code that defines the class
# the class body is indented under the class header
# the class body contains the attributes and methods of the class

# attributes
# attributes are the data that is associated with an object
# attributes are used to store the state of an object
# attributes are accessed using the dot notation
# class MyClass:
#     def __init__(self, name):
#         self.name = name
# my_object = MyClass("John")
# print(my_object.name)

# methods
# methods are functions that are associated with an object
# methods are used to define the behavior of an object
# methods are accessed using the dot notation
# class MyClass:
#     def say_hello(self):
#         print("Hello, my name is", self.name)
# my_object = MyClass("John")
# my_object.say_hello()

# special methods
# special methods are methods that are used to define the behavior of an object
# special methods are used to overload operators
# special methods are used to define the behavior of an object when it is used in a particular context
# class MyClass:
#     def __add__(self, other):
#         return self.value + other.value
# my_object = MyClass(10)
# other_object = MyClass(20)
# result = my_object + other_object
# print(result)

# inheritance
# inheritance is the process of creating a new class based on an existing class
# inheritance is used to create a hierarchy of classes
# inheritance is used to share code between classes
# class MyClass:
#     def say_hello(self):
#         print("Hello, my name is", self.name)
# class MySubClass(MyClass):
#     def say_goodbye(self):
#         print("Goodbye, my name is", self.name)
# my_object = MySubClass("John")
# my_object.say_hello()
# my_object.say_goodbye()

# polymorphism
# polymorphism is the ability of an object to take on multiple forms
# polymorphism is used to define the behavior of an object when it is used in a particular context
# polymorphism is used to write code that is flexible and reusable
# class MyClass:
#     def say_hello(self):
#         print("Hello, my name is", self.name)
# class MySubClass(MyClass):
#     def say_hello(self):
#         print("Good morning, my name is", self.name)
# my_object = MySubClass("John")
# my_object.say_hello()

# encapsulation
# encapsulation is the process of hiding the implementation details of an object from the outside world
# encapsulation is used to protect the data of an object from being modified accidentally
# encapsulation is used to define the interface of an object
# class MyClass:
#     def __init__(self, name):
#         self.__name = name
#     def get_name(self):
#         return self.__name
#     def set_name(self, name):
#         self.__name = name
# my_object = MyClass("John")
# print(my_object.get_name())
# my_object.set_name("Jane")
# print(my_object.get_name())


# sample code snippets on classes
class Person:
    def__init__(self, name, age)
    self.name = name
    self.age = age

def greet(self):
    print("Hello, my name is", self.name)


person = Person("John", 30)
person.greet()

# builtin dunder methods
# dunder methods are methods that are used to define the behavior of an object
# dunder methods are used to overload operators
# dunder methods are used to define the behavior of an object when it is used in a particular context
# lists of dunder methods
# __init__ method: is used to initialize the object
def __init__(self, name, age):
    self.name = name
    self.age = age

# __del__ method: is used to delete the object
def __del__(self):
    print("Object deleted")

# __str__ method: used to 


# __repr__ method
# __len__ method
# __getitem__ method
# __setitem__ method
# __delitem__ method


class Book:
   def __init__(self, title, pages):
       self.title = title
       self.pages = pages

   def __len__(self):
       return self.pages

   def __str__(self):
       return f"'{self.title}' has {self.pages} pages"

   def __eq__(self, other):
       return self.pages == other.pages
  
book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

print(len(book1)) # 420
print(len(book2)) # 420
print(str(book1)) # 'Built Wealth Like a Boss' has 420 pages
print(str(book2)) # 'Be Your Own Start' has 420 pages
print(book1 == book2) # True



class Cart:
   def __init__(self):
       self.items = []

   def add(self, item):
       self.items.append(item)

   def remove(self, item):
       if item in self.items:
           self.items.remove(item)
       else:
           print(f'{item} is not in cart')

   def list_items(self):
       return self.items

   def __len__(self):
       return len(self.items)

   def __getitem__(self, index):
       return self.items[index]

   def __contains__(self, item):
       return item in self.items

   def __iter__(self):
       return iter(self.items)

cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

for item in cart:
   print(item, end=' ') # Laptop Wireless mouse Ergo keyboard Monitor

print(len(cart)) # 4
print(cart[3]) # Monitor

print('Monitor' in cart) # True
print('banana' in cart) # False

cart.remove('Ergo keyboard')

print(cart.list_items()) # ['Laptop', 'Wireless mouse', 'Monitor']

cart.remove('banana') # banana is not in cart