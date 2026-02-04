# enumerate function in python
# Notes: 
# enumerate() function adds a counter to an iterable and returns it in a form of enumerate object.
# This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() function. 
# enumerate() function is very useful when we want to loop through a list and have an automatic counter for each element. 
# enumerate() function can also take a start parameter which is used to specify the starting index of the counter. 

# use cases
# 1. to loop through a list and have an automatic counter for each element
listsEnum = enumerate([1, 2, 3])
print(listsEnum)
# output: [(0, 1), (1, 2), (2, 3)]

# 2. to convert an iterable into a list of tuples
listsEnum = enumerate([1, 2, 3])
print(list(listsEnum))
# output: [(0, 1), (1, 2), (2, 3)]  

# 3. to loop through a list and have an automatic counter for each element starting from a specific index
listsEnum = enumerate([1, 2, 3], start=1)
print(list(listsEnum))
# output: [(1, 1), (2, 2), (3, 3)]

# 4. for loop: to iterate over an iterable

tuples = (1, 2, 3)
for index, value in enumerate(tuples):
    print(index, value)
# output: 0 1
#         1 2
#         2 3

sets = set([1, 2, 3])
for index, value in enumerate(sets):
    print(index, value)
# output: 0 1
#         1 2
#         2 3
