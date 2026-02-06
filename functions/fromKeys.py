# fromkeys in python dictonaries
# It takes two parameters
# 1. keys - the keys for the new dictionary
# 2. values - the value for all keys (optional, defaults to None)
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict_from_keys = dict.fromkeys(keys, values)
print(dict_from_keys)


# gotchas
# if you use an iterable as the second parameter, all keys will reference the same object
data =  dict.fromkeys(['a', 'b', 'c'], [1, 2, 3])
print(data) # {'a': [1, 2, 3], 'b': [1, 2, 3], 'c': [1, 2, 3]}
data['a'].append(4)
print(data) # {'a': [1, 2, 3, 4], 'b': [1, 2, 3, 4], 'c': [1, 2, 3, 4]}

