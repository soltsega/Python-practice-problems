# collections module in python
# The collections module in python provides alternatives to built-in data types like list, dict, set, and tuple. 
# It includes specialized container datatypes that provide additional functionality and flexibility.
# The collections module is often used in conjunction with other modules like itertools, functools, and operator

# practical use cases
# 1. to create a named tuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
pt = Point(1, 2)
print(pt.x, pt.y)