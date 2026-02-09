# deque or double ended queue is a  data structure that allows you to add and remove elements from both ends of the queue.
# they are used to implement a queue that can be used to add and remove elements from both ends of the queue.
# they are imported from the collections module in python and they provide a convenient way to implement a

# the parameters they take can be any iterable like list, tuple, string, etc. and the data types of the values they return can be any data type like int, float, etc.

# the operations they supprt can be used to add and remove elements from both ends of the queue, to rotate the elements in the queue, to reverse the elements in the queue, and many more.
# parctical examples of the deque

from collections import deque
de = deque([1, 2, 3, 4, 5])
print(de)  # will output deque([1, 2, 3, 4, 5])

# the operations they support can be:
# 1. popleft()
de.popleft()  # will remove the first element of the deque which is 1
print(de)  # will output deque([2, 3, 4, 5

# 2. append()
de.append(6)  # will add the element 6 to the end of the deque
print(de)  # will output deque([2, 3, 4, 5, 6])

# 3. appendLeft()
de.appendleft(0)  # will add the element 0 to the beginning of the deque
print(de)  # will output deque([0, 2, 3, 4, 5, 6])

# 4. pop()
de.pop()  # will remove the last element of the deque which is 6
print(de)  # will output deque([0, 2, 3, 4, 5])

# 5. rotate()
de.rotate(-1)  # will rotate the elements in the deque to the left by one position
print(de)  # will output deque([2, 3, 4, 5, 0])
de.rotate(2)  # will rotate the elements in the deque to the right by two positions
print(de)  # will output deque([5, 0, 2, 3, 4])

# 6. reverse()
de.reverse()  # will reverse the elements in the deque
print(de)