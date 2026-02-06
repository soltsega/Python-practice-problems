# Regular expressions in python
# This library is used to search for patterns in strings
# We need to import a dedicated library for it.
import re

# Basic patterns:
# re.match() - matches a pattern at the beginning of a string and returns a match object
# re.search() - searches for a pattern anywhere in a string and returns a match object
# re.findall() - finds all occurrences of a pattern in a string and returns a list
# re.finditer() - finds all occurrences of a pattern in a string and returns an iterator
# re.sub() - replaces a pattern with another string
# re.split() - splits a string by a pattern

# let's each one by one
# 1. re.match()
pattern = r"hello"  # The 'r' prefix is used to define a raw string, which means that backslashes are treated as literal characters, not escape characters.
text = "hello world"
match = re.match(pattern, text)
print(match)  # <re.Match object; span=(0, 5), match='hello'>

# 2. re.search()
pattern = r"world"
text = "hello world"
match = re.search(pattern, text)
print(match)  # <re.Match object; span=(6, 11), match='world'>

# 3. re.findall()
pattern = r"\d{2,5}" # finds numbers with 2 to 5 digits
text = "hello 123 world 456"
matches = re.findall(pattern, text)
print('matches/findall:', matches)  # ['123', '456']

# 4. re.finditer()
pattern = r"\d+" # finds all digits
text = "hello 123 world 456"
matches = re.finditer(pattern, text)
for match in matches:
    print('matches/finditer:', match)  # <re.Match object; span=(6, 9), match='123'>, <re.Match object; span=(16, 19), match='456'>

# 5. re.sub()
pattern = r"\d+"
text = "hello 123 world 456"
new_text = re.sub(pattern, "789", text)
print('re/sub:', new_text)  # hello 789 world 789

# 6. re.split()
pattern = r"\s+"  # splits by whitespace
text = "hello world 123"
parts = re.split(pattern, text)
print('re/split:', parts)  # ['hello', 'world', '123']


# Other keywords like \d, \w, \s, etc.
# \d - matches any digit (0-9)
# \w - matches any word character (a-z, A-Z, 0-9, _)
# \s - matches any whitespace character (space, tab, newline, etc.)
# \D - matches any non-digit character
# \W - matches any non-word character
# \S - matches any non-whitespace character
# 

# other modifiers in python
# re.IGNORECASE - ignores case
# re.MULTILINE - matches multiline strings
# re.DOTALL - matches any character including newline
# re.VERBOSE - allows comments in regex


# Let's see them in code snippets
patient_id = "p1001"
pattern = r"p\d{4}"  # matches p followed by exactly 4 digits
match = re.match(pattern, patient_id)
print('patient_id:', match)  # <re.Match object; span=(0, 5), match='p1001'>

# re.IGNORECASE
text = "Hello World"
pattern = r"hello"
match = re.search(pattern, text, re.IGNORECASE)
print('ignorecase:', match)  # <re.Match object; span=(0, 5), match='Hello'>

# re.MULTILINE
text = "hello\nworld"
pattern = r"^world"
match = re.search(pattern, text, re.MULTILINE)
print('multiline:', match)  # <re.Match object; span=(6, 11), match='world'>

# re.DOTALL
text = "hello\nworld"
pattern = r"hello.world"
match = re.search(pattern, text, re.DOTALL)
print('dotall:', match)  # <re.Match object; span=(0, 11), match='hello\nworld'>

# re.VERBOSE
pattern = r"""
    \d+  # one or more digits
    \s+  # one or more whitespace characters
    \w+  # one or more word characters
"""
text = "123 hello"
match = re.search(pattern, text, re.VERBOSE)
print('verbose:', match)  # <re.Match object; span=(0, 11), match='123 hello'>



# what I have learnt so far?
# search
# findall
# sub
# finditer
# split
# 
# 
# IGNORECASE
# DOTALL
# VERBOSE
# MULTILINE.