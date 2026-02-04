# filter metod in python


# notes:
# it accepts a function and an iterable
# it returns a new iterable

# use cases
# 1. to filter out elements from an iterable
lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def isEven(x):
    return x % 2 == 0
print(list(filter(isEven, lists)))

# 2. to filter out elements from an iterable using lambda
print(list(filter(lambda x: x % 2 == 0, lists)))


# 3. to filter out elements from an iterable using lambda and list comprehension
print([x for x in lists if x % 2 == 0])


