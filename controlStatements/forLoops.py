# for loops in python

# for i in range formats: it takes three arguments but yoiu can only pass any one of them as it has builtin defaults 
# The arguments are: start, stop, step
for i in range (5):  # prints the numbers from 0 to 4
    print(i)

for i in range (2, 10):  # prints the numbers from 2 to 9
    print(i)


for i in range (1, 10, 2):  # prints the odd numbers from 1 to 9
    print(i)

# iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# iterating over a sttring
for char in "solomon":
    print(char)

# iterating over a dictionary
person = {"name":"solomon", "age":25, "city":"None"}

# this will print the keys and values
for key in person:
    print(key, ":", person[key])

for item in person.items():
    print(item)

# This will print the keys only
for key in person.keys():
    print(person[key])

# This will print the values only
for value in person.values():
    print(value)


#2. iterating over a set
# sets are unordered collections of unique elements
# we can iterate over a set using for loop
colors = {"red", "green", "blue"} 
for color in colors:
    print(color)

# but there are alos other methods to iterate over a set depending on the situation and the requirements of our code
# using enumerate to get index and value
for index, color in enumerate(colors):  #index is the position of an element in the set
    print(index, color)


# using sorted to iterate in a sorted order
for color in sorted(colors):
    print(color)


# using reversed to iterate in reverse order
for color in reversed(colors):
    print(color)


# 3. iterating over a tuple
# tuples are ordered collections of elements that are immutable
# we can iterate over a tuple using for loop
points = (1, 2, 3, 4, 5)
for point in points:
    print(point)


# using enumerate to get index and value
for index, point in enumerate(points):
    print(index, point)


# using sorted to iterate in a sorted order
for point in sorted(points):
    print(point)