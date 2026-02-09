# Generators in python
# A generator is a special type of iterator that generates values on the fly and does not store them in memory.
# Generators are defined using a function that contains one or more yield statements.
# The yield statement is used to return a value from the function and pause the function's execution.
# The function can then be resumed from where it left off the next time it is called.


# usecases of generators
# 1. to generate a sequence of numbers
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
counter = count_up_to(5)
print(next(counter))  # Output: 1

# 2. to return values without storing them in memory. 
# They are useful when working with large datasets or infinite sequences, as they allow you to generate values on the fly without consuming a lot of memory.
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
    

# 3. to create iterators that can be used in a for loop or with other iterator tools like map, filter, and reduce.
fib_gen = fibonacci()
for num in fib_gen:
    print(num)
# samples
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
counter = count_up_to(5)
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2

# 2. Fibonacci sequence generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fib_gen = fibonacci()
print(next(fib_gen))  # Output: 0
print(next(fib_gen))  # Output: 1