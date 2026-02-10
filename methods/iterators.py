# iterators in python
# an iterator is an object that implements the iterator protocol, which consists of the methods __iter__() and __next__().

fruit_basket = ['apple', 'banana', 'cherry']
iterator = iter(fruit_basket)
print(next(iterator))  # Output: 'apple'
print(next(iterator))  # Output: 'banana'
print(next(iterator))  # Output: 'cherry'
print(next(iterator))  # Raises StopIteration exception

# we can fix this exception by using a for loop to iterate through the iterator
fruit_basket = ['apple', 'banana', 'cherry']
for fruit in fruit_basket:
    print(fruit)

# or using another keyword while True:
    try:
        fruit = next(iterator)
        print(fruit)
    except StopIteration:
        break
# Or using the End keyword in the next() function: as a default value to return when the iterator is exhausted, instead of raising an exception.
fruit_basket = ['apple', 'banana', 'cherry']
iterator = iter(fruit_basket)
print(next(iterator, 'End'))  # Output: 'apple'
print(next(iterator, 'End'))  # Output: 'banana'
print(next(iterator, 'End'))  # Output: 'cherry'
print(next(iterator, 'End'))  # Output: 'End'
# The iter() function is used to create an iterator from an iterable, such as a list, tuple, or string.