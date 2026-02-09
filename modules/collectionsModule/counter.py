# counters in python
# a counter is a subclass of the dict class that is used to count the number of occurrences of each element in a list or any iterable.
# it is a part of the collections module in python and it provides a convenient way to count the number of occurrences of each element in a list or any iterable.
# it takes an iterable as an argument and returns a dictionary-like object where the keys are the elements of the iterable and the values are the number of occurrences of each element in the iterable.
# it returns a dictionary where the keys are the elements of the iterable and the values are the number of the occurrences of each elements
# the data types of the parameters it take can be any iterable like list, tuple, string, etc. and the data types of the values it returns can be any data type like int, float, etc.
# practical use cases
# 1. to count the number of occurrences of each element in a list
# 2. to count the number of occurrences of each word in a sentence
#  


# lets' see with an example
from collections import Counter
lists = [1,2,3,4,5,5]
print(Counter(lists))  # will output Counter({5: 2, 1: 1, 2: 1, 3: 1, 4: 1}) which means that the number 5 occurs twice in the list and the numbers 1, 2, 3, and 4 occur once in the list.
# 


# Other uses of counters
# 1. to count the number of occurrences of each element in a list
def count_occurrences(lst):
    return Counter(lst) # it will return a dictionary where the keys are the elements of the list and the values are the number of occurrences of each element in the list
print(count_occurrences(['apple', 'banana', 'apple', 'orange', 'banana',]))


# /*************  ✨ 🌟  *************/
# final notes on counter methods in collections module of python
# the counter methods are used to count the number of occurrences of each element in a list or any iterable.
# the counter methods return a dictionary-like object where the keys are the elements of the iterable and the values are the number of occurrences of each element in the iterable.
# the counter methods are useful when we need to count the number of occurrences of each element in a list or any iterable.
# the counter methods can be used to count the number of occurrences of each element in a list, to count the number of occurrences of each word in a sentence, to count the number of occurrences of each character in a string, and many more.
# the counter methods can be used to define the significance of each element in a list or any iterable.
# final notes on counters
# /*******  2c73c967-be9b-44f4-94fb-2f62b6ee9c29  *******/    
# 
