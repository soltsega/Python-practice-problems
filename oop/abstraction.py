# Abstraction - Hiding the internal details and showing only the functionality to the user.
# The difference between abstraction and encapsulation is that abstraction focuses on hiding the complexity of the system and showing only the necessary details to the user, 
# while encapsulation focuses on hiding the internal state of an object and only allowing access to it through methods.

# Let's demonstrate abstraction in Python using an example of a car. We will create a Car class that has some internal details (like engine and fuel) that are hidden from the user, and we will provide a method to start the car.
from abc import ABC, abstractmethod
# ABC - Abstract Base Class which is a class that cannot be instantiated and is meant to be subclassed. 
# It can contain abstract methods, which are methods that are declared but not implemented in the base class. Subclasses


# abstractmethod - A decorator that is used to declare a method as abstract. 
# An abstract method is a method that is declared but not implemented in the base class. 
# Subclasses are required to implement the abstract method.
class Car(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = "V8 Engine"  # internal detail
        self.fuel = "Gasoline"  # internal detail

    @abstractmethod  # abstract method
    def start(self):
        return f"The {self.make} {self.model} is starting with {self.engine} and runs on {self.fuel}."
    
# Now, when we create an instance of the Car class and call the start method, we don't need to worry about the internal details of the engine and fuel. We just get the functionality of starting the car.
my_car = Car("Ford", "Mustang")
print(my_car.start())

# But what is being hidden from the user here🤨
# The internal details of the car, such as the type of engine and fuel, are hidden from the user. The user only interacts with the start method, which provides the necessary functionality without exposing the complexities of how the car works internally.


print(chr(54))
print(ord(' '))

print(all([1,2,3,4,4,3]))
print(any([1,2,3,4,4,3]))


x = 'print(4**2)'
eval(x)



# hiow to use @abstractmethod
# It is used to  