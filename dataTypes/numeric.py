# Numeric data types in python
# in this document, we will cover the numbric data types in python and the operations that are done in those data types
import math
# integer, float, complex
i = 10
f = 10.7
c = 3 + 4j

print(type(i)) # <class 'int'>
print(type(f)) # <class 'float'>
print(type(c)) # <class 'complex'>
print(c.real) # 3.0
print(c.imag) # 4.0
# operations on numeric data types
# addition
print("Addition:", i + f)  # 20.7
# subtraction
print("Subtraction:", f - i)  # 0.7
# multiplication
print("Multiplication:", i * f)  # 107.0


# converting between numeric data types
print("Int to Float:", float(i))  # 10.0
print("Float to Int:", int(f))  # 10
print("Int to Complex:", complex(i))  # (10+0j)

def numeric_operations():
    a = 15
    b = 4

    print("Addition:", a + b)  # 19
    print("Subtraction:", a - b)  # 11
    print("Multiplication:", a * b)  # 60
    print("Division:", a / b)  # 3.75
    print("Floor Division:", a // b)  # 3
    print("Modulus:", a % b)  # 3
    print("Exponentiation:", a ** b)  # 50625


    # using math module for advanced operations
    print("Square Root of a:", math.sqrt(a))  # 3.872983346207417
    print("Logarithm of a (base 10):", math.log10(a))  # 1.1760912590556813
    print("Logarithm of a (base e):", math.log(a))  # 2.70805020110221
    print("Sine of 30 degrees:", math.sin(math.radians(30)))  # 0.49999999999999994
    print("Cosine of 60 degrees:", math.cos(math.radians(60)))  # 0.5000000000000001
    print("Factorial of b:", math.factorial(b))  # 24