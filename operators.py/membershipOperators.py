# membership operators in python
# notes:
# in - returns True if a value is present in a sequence
# not in - returns True if a value is not present in a sequence


# use cases
# 1. to check if a value is present in a sequence
sequence = [1, 2, 3, 4, 5]
print(3 in sequence)
print(6 in sequence)
print(3 not in sequence)
print(6 not in sequence)

# 2. to check if a value is not present in a sequence
sequence = [1, 2, 3, 4, 5]
print(3 in sequence)
print(6 in sequence)
print(3 not in sequence)
print(6 not in sequence)


# 3. for in loop
for i in [1, 2, 3, 4, 5]:
    print(i in [1, 2, 3, 4, 5])


# 4. string membership
string = "Hello World"
print("Hello" in string)
print("World" in string)
print("Hello" not in string)
print("World" not in string)


# 5. dictionary membership
dictionary = {"a": 1, "b": 2, "c": 3}
print("a" in dictionary)
print("d" in dictionary)
print("a" not in dictionary)
print("d" not in dictionary)

# 6. value memberhsip in python dictionaries
dictionary = {"a": 1, "b": 2, "c": 3}
print(1 in dictionary.values())
print(4 in dictionary.values())
print(1 not in dictionary.values())
print(4 not in dictionary.values())

# 7. item membership
dictionary = {"a": 1, "b": 2, "c": 3}
print(("a", 1) in dictionary.items())
print(("d", 4) in dictionary.items())
print(("a", 1) not in dictionary.items())
print(("d", 4) not in dictionary.items())



