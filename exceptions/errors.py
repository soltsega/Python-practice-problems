# Errors in python

# There are many types of errors in python and in other languages as well

# 1. syntax errors: are errors that happen because of the invalid syntax and are easy to figure out

# 2. NameErrors: are errors that happen bacuase of the invalid variable name 
# eg. accessing a variable before it is declared

# 3. TypeError: are errors that happen because of the invalid type of the variable
# eg. adding a string and an integer

# 4. ValueError: are errors that happen because of the invalid value of the variable
# eg. converting a string to an integer

# 5. IndexError: are errors that happen because of the invalid index of the variable
# eg. accessing an index that is out of range

# 6. KeyError: are errors that happen because of the invalid key of the variable
# eg. accessing a key that is not in the dictionary

# 7. AttributeError: are errors that happen because of the invalid attribute of the variable
# eg. accessing an attribute that is not in the object



# Debuggung techniques:

# 1. print statements
# 2. debugger
# 3. logging
# 4. Using the python builtin Debugger(pdb)
# eg. python -m pdb your_script.py
# sample code:
def calculate_total(price, tax):
    total = price + (price * tax)
    # breakpoint()  # The debugger will start here
    return total

returned = calculate_total(100, 0.05)
print(returned)

# 5. Leveraging IDE  Debugging tools
