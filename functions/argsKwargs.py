# args and kwargs in python
# *args allows a function to accept any number of positional arguments
# now we will discuss about args and the operations that can be done on them

def example_args(*args):
    for index, value in enumerate(args, start=0):  #the "start = n" is a keyword argument that specifies the starting index for enumeration
                                                    # you can't change the keyword as it is predefined in the function definition
        print(f"Argument {index}: {value}")

# calling the function with different number of arguments
example_args(1, 2, 3)
example_args(1, 2, 3, "hello", 4.5)

# **kwargs allows a function to accept any number of keyword arguments
def example_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# calling the function
example_kwargs(name="Alice", age=30, city="New York")
example_kwargs(product="Laptop", price=999.99, stock=50)


# the properties of kwargs and args in python
def combined_example(*args, **kwargs):
    print("Positional arguments (args):")
    for index, value in enumerate(args):
        print(f"Argument {index}: {value}")
    
    print("\nKeyword arguments (kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# calling the function with both args and kwargs
combined_example(1, 2, 3, name="Bob", age=25)

