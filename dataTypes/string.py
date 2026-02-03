# String data types and the operations that can be done on them
s = "Hello, World!"
print(type(s))  # <class 'str'>
# string methods
print(s.upper())        # Convert to uppercase
print(s.lower())        # Convert to lowercase
print(s.isupper())     # Check if all characters are uppercase
print(s.islower())     # Check if all characters are lowercase
print(s.replace("World", "Python"))  # Replace substring
print(s.split(", "))    # Split string into list
print(s.find("World"))  # Find substring (case-sensitive, returns -1 if not found)

print(s.startswith("Hello"))  # Check if string starts with a substring
print(s.endswith("!"))        # Check if string ends with a substring

print(s.strip())        # Remove leading and trailing whitespace
print(s.capitalize())   # Capitalize first character
print(s.title())        # Title case
print(s.upper())       # Convert to uppercase
print(s.lower())      # Convert to lowercase

print(s.count("or"))   # Count occurrences of a substring
print(len(s))          # Length of the string
print(s[0])           # Accessing first character
print(s[-1])          # Accessing last character
print(s[0:5])        # Slicing substring
print(s[5:])       # Slicing from 5th index to end
print(s * 2)            # Repetition: it will output the string two times
print(s + " Welcome!")  # Concatenation
print("Hello" in s)     # Membership test: checks if "Hello" is in s
print("Python" not in s) # Membership test: checks if "Python" is not in s

# formatted string in python
print(f"Hey man, {s}")  # Using f-strings for formatting
name = "Alice"

# to reverse a string using slicing
reversed = s[::-1]

# to check if a string is palindrome
def is_palindrome(string):
    return string == string[::-1]

# slicing strings using the indexing operator and the slicing operators
# indexing operator
first_char = s[0]
last_char = s[-1]
substring = s[0:5]


# slicing operator
firstFive = slice(0, 5)
first_five_chars = s[firstFive]
print(first_five_chars)  # Output: Hello

# Summary of string data types and operations:
summary = """
- Strings are sequences of characters, defined with quotes.
- Common operations:
    * Case conversion: upper(), lower(), capitalize(), title()
    * Searching: find(), count(), startswith(), endswith()
    * Modification: replace(), strip(), split()
    * Slicing and indexing: s[0], s[-1], s[0:5], s[::-1]
    * Concatenation and repetition: +, *
    * Membership tests: 'sub' in s, 'sub' not in s
    * Formatting: f-strings
    * Palindrome check: s == s[::-1]
    * Length: len(s)
"""
print(summary)