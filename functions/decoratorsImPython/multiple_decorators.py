# We have seen about decorators in python and now we will be seeing about multiple decorators in python.
# Multiple decorators are used when we want to apply more than one decorator to a single function.
# We can apply multiple decorators to a single function by stacking them on top of each other using the @ symbol.
# The order of the decorators matters, as they are applied in the order they are defined.


# decorator 1
def decorator1(func):
    def inner():
        print("This is decorator 1")
        func()
    return inner

# decorator 2
def decorator2(func):
    def inner():
        print("This is decorator 2")
        func()
    return inner

# applying multiple decorators to a function
@decorator1
@decorator2
def func():
    print("This is the original function")


# calling the  decorated function
func() 