# data types  in python
# 1. Numeric Types
# 2. string Types
# 3. List Types
# 4. Tuple Types
# 5. Set Types
# 6. Dictionary Types
# 7. Boolean Types
# 8. None Type


# let's see each type with examples and which methods can be applied to them
# 1. Numeric Types
a = 10          # int
b = 10.5        # float
c = 2 + 3j     # complex
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>

# what are the operations that can be performed on numeric types
print(a + 5)    # Addition
print(b * 2)    # Multiplication
print(c.real)   # Real part of complex number
print(c.imag)   # Imaginary part of complex number
print(abs(c))    # Magnitude of complex number
print(pow(a, 2)) # Power
print(round(b))  # Rounding float
print(int(b))    # Convert float to int
print(float(a))  # Convert int to float
print(complex(a, b)) # Convert int and float to complex



# 1. string data types
s = "Hello, World!"
print(type(s))  # <class 'str'>
# string methods
print(s.upper())        # Convert to uppercase
print(s.lower())        # Convert to lowercase
print(s.replace("World", "Python"))  # Replace substring
print(s.split(", "))    # Split string into list