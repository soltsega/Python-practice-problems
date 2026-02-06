# setdefault method in python dictionaries
# They are used to get the value of a key, and if the key does not exist, it creates the key with the specified value

# Let's see with sample code snippets
# 1. To set a default value for a key that doesn't exist
words = {'apple': 5, 'banana': 3, 'orange': 2}
print(words.setdefault('apple', 10))  # Output: 5
print(words.setdefault('grape', 7))  # Output: 7
print(words)  # Output: {'apple': 5, 'banana': 3, 'orange': 2, 'grape': 7}

# 2. To get the value of a key that exists
words = {'apple': 5, 'banana': 3, 'orange': 2}
print(words.setdefault('apple', 10))  # Output: 5
print(words)  # Output: {'apple': 5, 'banana': 3, 'orange': 2}

# 3. 
animals = ['cat', 'dog', 'cat', 'bird']
for animal in animals:
    words.setdefault(animal, 0)
    words[animal] += 1
print(words)  # Output: {'cat': 2, 'dog': 1, 'bird': 1}

