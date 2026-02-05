# translator and maketrans in python

# translator is a dictionary that maps characters to characters
# maketrans is a function that returns a translator dictionary

# let's see with an example

# translator
translator = str.maketrans("aeiou", "AEIOU")
print("Hello World".translate(translator))  # Hello WOrld
