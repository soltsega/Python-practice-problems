# Decorators in python
# They are used to modify the behavior of a function without changing its code.
# They are defined using the @ symbol followed by the name of the decorator function.

# How it works:
# WE will demonstrate how it works without useing the @ symbol first, and then we will use the @ symbol.
def div(a,b):
    return a/b

def smart_div(func):

    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner

div = smart_div(div)
print(div)


# Now we will use the @ symbol to achieve the same result.


def smart_div(func):

    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner

@smart_div
def div(a,b):
    return a/b
div1= div(2,4)
print(div1)

