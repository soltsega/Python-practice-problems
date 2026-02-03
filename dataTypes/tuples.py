# tuples in python
# tuples are ordered collections of elements that are immutable
# tuples are defined using parentheses ()
# tuples are immutable, meaning they cannot be modified once created
# tuples are faster than lists because they are immutable

# creating a tuple
t = (1, 2, 3, "hello", 4.5)
print(t)  # (1, 2, 3, 'hello', 4.5)

# accessing elements in a tuple
print(t[0])  # 1
print(t[-1])  # 4.5
print(t[1:4])  # (2, 3, 'hello')
# tuples are immutable, so we cannot modify them
# t[0] = 10  # This will raise a TypeError

# tuple unpacking
t = (1, 2, 3)
a, b, c = t
print(a)  # 1
print(b)  # 2
print(c)  # 3

# the operations done on tuples 

# concatenation
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)  # (1, 2, 3, 4, 5, 6)

# repetition
t4 = t1 * 3
print(t4)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)


# membership
t = (1, 2, 3, "hello", 4.5)
print(2 in t)  # True
print("hello" in t)  # True
print(6 in t)  # False

# tuple methods
t = (1, 2, 3, 2, 4, 2)
print(t.count(2))  # 3
print(t.index(2))  # 1

# nested tuples
nt = (1, 2, (3, 4), (5, 6))
print(nt[2])  # (3, 4)