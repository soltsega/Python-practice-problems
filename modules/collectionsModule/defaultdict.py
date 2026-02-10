# defaultdict in python
# it is used to provide keys for dictionaries not haivng keys


# practical use cases
# 1. to count the number of occurrences of each element in a list
# it takes parameter as a function that returns the default values for the keys that are not present in the dictionary
# it 
from collections import defaultdict

from polars import count
from itertools import count
def count_occurrences(lst):
    counts = defaultdict(int) # it will assign a default value of 0 to any key that is not present in the dictionary
    for item in lst:
        counts[item] += 1
    print(counts) # it will print the defaultdict with the counts of each element in the list
    # return dict(counts) # it will convert the defaultdict to a regular dictionary
# print(count_occurrences(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))
count_occurrences(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])


# the default_factory can be list, set, int, str, etc. depending on the use case
# 1. list: it will return a list as the default value for the keys that are not present in the dictionary
def group_by_length_list(words):
    groups = defaultdict(list) # it will assign a default value of an empty list to any key that is not present in the dictionary
    for word in words:
        groups[len(word)].append(word)
    print(groups) # it will print the defaultdict with the groups of words by their lengths
    # return dict(groups) # it will convert the defaultdict to a regular dictionary
print(group_by_length_list(['apple', 'banana', 'orange', 'pear', 'grape']))


# 2. set: it will return a set as the default value for the keys that are not present in the dictionary
def group_by_length_set(words):
    groups = defaultdict(set) # it will assign a default value of an empty set to any key that is not present in the dictionary
    for word in words:
        groups[len(word)].add(word)
    return groups # it will return the defaultdict with the groups of words by their lengths
print(group_by_length_set(('apple', 'banana', 'orange', 'pear', 'grape')))

# 3. int: it will return an integer as the default value for the keys that are not present in the dictionary
def count_by_length_int(words):
    counts = defaultdict(int) # it will assign a default value of 0 to any key that is not present in the dictionary
    for word in words:
        counts[len(word)] += 1
    print(counts) # it will print the defaultdict with the counts of each word by their lengths

print(count_by_length_int(['apple', 'banana', 'orange', 'pear', 'grape']))  



# handiling missing keys in a dictionary using the lambda function as the default_factory
def handle_missing_keys_lambda():
    words = {'apple': 5, 'banana': 3, 'orange': 2}
    print(words.get('grape', lambda: 0)()) # it will print 0 if the key is not present in the dictionary
handle_missing_keys_lambda()

d = defaultdict(lambda: 'default value')
d['a'] = 1
d['b'] = 2

print(d['a'])  # Output: 1
print(d['b'])  # Output: 2
print(d['missing_key'])  # Output: 'default value'



# missing keys: what will they return if we don't pass any parameter to the defaultdict function
print(""")
Factory   Default Value    Description
int        0              The integer zero.
str       """""""         An empty string.
list        []            An empty list.
set         set()           An empty set.
dict        {}             An empty standard dictionary.
tuple,(),An empty tuple.
float,0.0,The float version of zero.
bool,False,               The default boolean state.
""")