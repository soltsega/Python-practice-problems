# Map funciton in python

# notes:
# it accepts a function and an iterable
# it returns a new iterable


# use cases
# 1. to apply a function to all items in an iterable
lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square(x):
    return x * x
print(list(map(square, lists)))

# 2. to apply a function to all items in an iterable using lambda
print(list(map(lambda x: x*x, lists)))

# 3. adding two lists
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print(list(map(lambda x, y: x + y, list1, list2)))

# 4. for loop
for i in map(lambda x: x*x, lists):
    print(i)