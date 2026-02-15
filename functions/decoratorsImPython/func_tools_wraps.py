# Functools.wraps is a decorator that is used to preserve the original function name, docstring, and signature when you wrap a function with another function.
# what does it specifically do?
# It is used to preserve the original function's metadata (name, docstring, and signature) when you wrap it with another function. This is important because when you wrap a function, the wrapper function can obscure the original function's metadata, making it difficult to debug and understand the code.
# By using functools.wraps, you can ensure that the wrapper function retains the original function's
from functools import wraps

# Let's demonstrate it with code snippet
def decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("This is the decorator")
        return func(*args, **kwargs)
    return inner

# 