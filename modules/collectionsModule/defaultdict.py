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
    return dict(counts) # it will convert the defaultdict to a regular dictionary
print(count_occurrences(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))