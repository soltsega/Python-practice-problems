# zip functions or methods in python

# zip() function in Python is used to combine two or more iterables into a single iterable of tuples.
# The items are returned in a tuple where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
# The returned list is only as long as the shortest input iterable.
# The tuples are generated in a lazy fashion, meaning that the tuples are not actually created until they are needed.
# The zip() function takes any number of iterables as arguments and returns an iterator of tuples.
# The elements are consumed from each iterable as we loop through the zip object.
# If the input iterables are of uneven length, the resulting zip object will stop iteration as soon as the shortest iterable is exhausted.
# The zip() function can be used with any number of iterables of equal or unequal length.
# The elements from each iterable are grouped together.
# The zip() function can be used with any type of iterable, including lists, tuples, and strings.
# The zip() function can be used with any number of arguments.
# The zip() function is a versatile function that can be used in a variety of applications, including data processing and data analysis.
# The zip() function can be used with other iterable functions, such as list(), tuple(), and map().

# now: let's move on to the code implementation of zip() function

#1. To transpose a matrix: using the asterisk operator (*)
lists = [[1,2,3], [4,5,6], [7,8,9]]
print(list(zip(*lists)))
# output: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

#2. To merge two lists into a dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
print(dict(zip(keys, values)))
# output: {'a': 1, 'b': 2, 'c': 3}

# 3. To create a list of tuples from two lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(list(zip(list1, list2)))
# output: [(1, 'a'), (2, 'b'), (3, 'c')]

# 4. To unzip a list of tuples
list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
print(list(zip(*list_of_tuples)))
# output: [(1, 2, 3), ('a', 'b', 'c')]

# 5. To create a dictionary from two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
print(dict(zip(keys, values)))
# output: {'a': 1, 'b': 2, 'c': 3}

# 6. for loop
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for i, j in zip(list1, list2):
    print(i, j)
# output: 1 a
#         2 b
#         3 c


