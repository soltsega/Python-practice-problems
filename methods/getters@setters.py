# Getters and setters are methods that allow you to access and modify the attributes of a class. They are often used to encapsulate the internal state of an object and provide a controlled way to access and modify it.
# Getters are methods that return the value of an attrubute. They are often used to povide read-only access to an attribute. They are defined using the @property decorator.
# Setters are methods that set the value of an attribute. They are often used to provide write-only access to an attribute. They are defined using the @attribute_name.setter decorator.
# sample code snippets


class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


# what is the difference between using the getters and just returning the attribute directly?
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    @property   # getter
    def name(self):
        return self._name

    @property   # getter
    def age(self):
        return self._age



# lets' demonstrate the difference between using getters and using the regular attribute access
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    @property   # getter
    def name(self):
        return self._name

    @property   # getter
    def age(self):
        return self._age
    

    c = MyClass("Alice", 30)
    print(c.get_name())  # Output: Alice
    print(c.name)  # Output: Alice
# The main difference is that getters and setters provide a level of abstraction and control over how attributes




# here are the use cases we have to prefer using getters and setters over regular attribute access:
# 1. Encapsulation: Getters and setters allow you to encapsulate the internal state of an object. This means that you can control how the attributes are accessed and modified, which can help to prevent unintended side effects and maintain the integrity of the object's state.>



# deleter is a method that allows you to delete an attribute of a class. It is defined using the @attribute_name.deleter decorator. 
# It is often used to provide a controlled way to delete an attribute and perform any necessary cleanup.

# lets' see with an example of how to use it
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @age.deleter
    def age(self):
        del self._age


# lets' see how to use it
c = MyClass("Alice", 30)
print(c.name)  # Output: Alice
c.name = "Bob"
print(c.name)  # Output: Bob
del c.name





