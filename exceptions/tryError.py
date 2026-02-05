# Try error exception handling in python

try:
    def divide(a, b):
        return a / b
    divide(10, 0)
except ZeroDivisionError:
    print("Cannot divide by zero")


# try except else finally
try:
    result = 100 / 4
except ZeroDivisionError:
    print('You cannot divide by zero!') # This will not run
else:  # to run if try does not raise an exception
    print(f'Result is {result}') # Result is 25.0
finally:  # to run no matter what
    print('Execution complete!') # Execution complete!







# Exception signaling: using raise
try:
    raise ValueError("Invalid value")
except ValueError as e:
    print(e)
