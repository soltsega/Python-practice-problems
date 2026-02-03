# sets in python
"""
Module: sets.py
Demonstrates Python set usage, behaviors, and common patterns through runnable examples.
Contents:
- High-level overview of Python sets: properties (unordered, unique, mutable), use-cases,
    and comparisons to lists/tuples.
- Examples of creating sets from literals, lists, tuples, strings, and frozenset.
- Mutation operations: add, update, remove, discard, pop, clear.
- Set algebra: union, intersection, difference, symmetric difference and their in-place variants.
- Membership testing, length, comprehensions, iteration.
- Copying semantics: shallow copy (.copy()) and deep copy (copy.deepcopy()).
- Practical use-cases: deduplication, fast membership testing, using frozenset as dict keys,
    and a BFS example using adjacency sets.
- Edge cases: immutability requirements for set elements and using frozenset as a hashable wrapper.
Public functions (each prints a self-contained demo):
- demo_creation_and_casting(): show creation and casting from different types, frozenset use.
- demo_mutation(): illustrate add/update/remove/discard/pop/clear and their behaviors.
- demo_algebra(): demonstrate set algebra operators and in-place updates.
- demo_comparisons(): subset/superset/disjoint checks.
- demo_comprehensions_and_iteration(): set comprehensions and iteration patterns.
- demo_copying_and_identity(): show copy vs deepcopy and identity differences.
- demo_use_cases(): practical examples including deduplication, membership performance,
    frozenset-as-key, and BFS on adjacency sets.
- demo_edge_cases(): demonstrates errors for unhashable elements and frozenset as a key.
- main(): runs all demos in sequence when executed as a script.
Usage:
Run the module as a script to print the demonstrations:
        python sets.py
Intended for educational purposes to illustrate idiomatic set usage in Python.
"""
# sets are unordered collections of unique elements
# sets are mutable, meaning we can add or remove elements from a set
# sets are defined using curly braces {} or the set() function


# but let's differentiate between a set and tuples, and lists
# tupes: ordered, immutable, allows duplicate elements
# lists: ordered, mutable, allows duplicate elements
# sets: unordered[no indexing], mutable, no duplicate elements

# key notes about sets
# They are optimal solutions when
# we just need high speed membership testing:the time complesity is O(1) as compared to listsand tuples which is O(n)
# we need to eliminate duplicate entries from a collection
# When we need to operate with mathematical set operations: difference, symmetric difference, intersection, union, etc.

# it is not optimal when
# we need to maintain the order of elements
# we need to access elements by index
# it uses much more memory than lists and tuples due to the underlying 🔥hash table implementation


# On which areas are sets commonly used
# 1. Data deduplication: removing duplicate entries from a collection
# 2. Membership testing: checking if an element exists in a collection
# 3. Mathematical set operations: performing operations like union, intersection, difference, etc.
# 4. Graph algorithms: representing graphs using adjacency sets for efficient traversal and search operations
# example of how it is used for graph algorithms:
# adjacency list representation of a graph using sets
# examples
import copy
import copy as _copy


set1 = {1,2,3,4,5,6}
print(type(set1))  #<class 'set'>
# or by casting a list to a set
set2 = set([4,5,6,7,8,9])

# methods of defining a set
set3 = set() # an empty set
set4 = {1,2,3}
set5 = set([1,2,3,4,5,]) # by casting lists to a set
set6 = set((6,67,8,9))  # by casting tuples to a set
set7 = set("hello")  # by casting strings to a set
set8 = {1,2,"sol", (4,5,6)}  # by mixing data types
set9 = frozenset(4, [1,2,3,4])  # immutable set: this is a set that cannot be modified after its creation
# printing sets
print(set1) # {1, 2, 3, 4, 5, 6}
for item in set2:
    print(item)

# set operations
# adding elements to a set
set1.add(7)
print(set1) # {1, 2, 3, 4, 5, 6, 7}
set1.update([8,9,10])  # adding multiple elements to a set
print(set1) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# removing elements from a set
set1.remove(10)  #can raise an error if not found
print(set1)

set1.discard(9) #won't cause an error if the elements is not cound
print(set1)

set1.pop() # this will remove an arbitrary element as it is not ordered
print(set1)
set1.clear() # this will remove all the elements from a set
print(set1)


# set operations: union, intersection, difference, symmetric difference
A = {1,2,3,4,5}
B = {4,5,6,7,8}
# union
print(A.union(B))  # {1, 2, 3, 4, 5, 6, 7, 8}
# intersection
print(A.intersection(B))  # {4, 5}
# difference
print(A.difference(B))  # {1, 2, 3}
# symmetric difference: elements in either A or B but not in both
print(A.symmetric_difference(B))  # {1, 2, 3, 6, 7, 8}

# set membership test
print(3 in A) # returns true or false
print(6 not in A) # returns true or false


# casting other data types to sets
# can be casted from lists, tuples, strings, dictionaries
# but keep in mind that sets only store unique elements
# it will remove duplicates when casting if there are any
list1 = [1,2,2,3,4,4,5]
set_from_list = set(list1)
print(set_from_list)  # {1, 2, 3, 4, 5}

# nesting sets in sets or other data types in sets
# sets cannot be nested within other sets directly as they are unhashable
# but we can use frozensets to achieve this
# frozensets are immubale sets which does not entertain any methods that modify the set
setA = frozenset({1,2,3})

# set comprehensions
squared_set = {x**2 for x in range(1, 6)}
print(squared_set)  # {1, 4, 9, 16, 25}

# length of a set
print(len(squared_set))  #5
# copying a set
set_copy = squared_set.copy()

# deepcopy
set_deepcopy = copy.deepcopy(squared_set)  # this is useful when dealing with nested sets or complex data structures
print(set_deepcopy) # {1, 4, 9, 16, 25}



# 
def demo_creation_and_casting():
    print("\n--- Creation & Casting ---")
    empty = set()
    mixed = {1, "x", (2, 3)}
    from_list = set([1, 2, 2, 3, 4])
    from_tuple = set((10, 20, 20))
    from_string = set("mississippi")
    frozen = frozenset({7, 8, 9})
    nested_via_frozen = {frozenset({1, 2}), frozenset({3, 4})}

    print("empty:", empty)
    print("mixed:", mixed)
    print("from_list (dedup):", from_list)
    print("from_string:", from_string)
    print("frozen:", frozen)
    print("nested via frozenset:", nested_via_frozen)


def demo_mutation():
    print("\n--- Mutation ---")
    s = set([1, 2, 3])
    s.add(4)
    s.update([5, 6, 6])
    print("after add/update:", s)

    # remove vs discard
    try:
        s.remove(100)
    except KeyError:
        print("remove raised KeyError for missing element")
    s.discard(100)  # safe
    print("after discard missing:", s)

    # pop removes an arbitrary element
    popped = s.pop()
    print("popped:", popped, "remaining:", s)

    # clear
    s.clear()
    print("cleared:", s)
    print(dir(s))

def demo_algebra():
    print("\n--- Set Algebra ---")
    X = {1, 2, 3, 4}
    Y = {3, 4, 5, 6}
    print("X:", X)
    print("Y:", Y)

    print("union:", X | Y)
    print("intersection:", X & Y)
    print("difference X - Y:", X - Y)
    print("difference Y - X:", Y - X)
    print("symmetric_difference:", X ^ Y)


    # in-place ops
    a = X.copy()
    a.update(Y)  # union in-place
    b = X.copy()
    b.intersection_update(Y)
    c = X.copy()
    c.difference_update(Y)
    d = X.copy()
    d.symmetric_difference_update(Y)
    print("update (in-place):", a)
    print("intersection_update:", b)
    print("difference_update:", c)
    print("symmetric_difference_update:", d)


def demo_comparisons():
    print("\n--- Subset / Superset / Disjoint ---")
    U = {1, 2}
    V = {1, 2, 3, 4}
    W = {5, 6}
    print("U <= V (subset):", U.issubset(V))
    print("V >= U (superset):", V.issuperset(U))
    print("U is disjoint with W:", U.isdisjoint(W))


def demo_comprehensions_and_iteration():
    print("\n--- Comprehensions & Iteration ---")
    squares = {x * x for x in range(6)}
    evens = {x for x in range(10) if x % 2 == 0}
    print("squares:", squares)
    print("evens:", evens)
    print("iterate over evens:")
    for i in evens:
        print(i, end=" ")
    print()


def demo_copying_and_identity():
    print("\n--- Copying & Identity ---")
    original = {1, 2, 3}
    shallow = original.copy()
    deep = _copy.deepcopy(original)
    print("original id:", id(original))
    print("shallow id:", id(shallow))
    print("deep id:", id(deep))


def demo_use_cases():
    print("\n--- Practical Use Cases ---")
    # 1. Deduplicate a list
    data = [1, 2, 2, 3, 4, 4, 4, 5]
    deduped = list(set(data))
    print("deduped list:", deduped)

    # 2. Membership testing
    pool = set(range(0, 1000000))
    print("500000 in pool?:", 500000 in pool)

    # 3. Using frozenset as dict key
    edge_map = {frozenset({1, 2}): "edge_1_2", frozenset({2, 3}): "edge_2_3"}
    print("edge_map lookup:", edge_map.get(frozenset({2, 1})))

    # 4. Graph adjacency with sets + BFS
    adj = {
        1: {2, 3},
        2: {1, 4},
        3: {1, 5},
        4: {2},
        5: {3},
    }
    print("Graph adjacency:", adj)
    start = 1
    visited = set()
    queue = [start]
    order = []
    while queue:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        # add neighbors that are not visited
        queue.extend([n for n in adj.get(node, set()) if n not in visited])
    print("BFS order:", order)


def demo_edge_cases():
    print("\n--- Edge Cases ---")
    # sets cannot contain mutable types
    try:
        s = set()
        s.add([1, 2])  # list is unhashable
    except TypeError as e:
        print("adding list to set raised TypeError:", e)

    # frozenset is hashable
    fs = frozenset([1, 2])
    mapping = {fs: "value"}
    print("frozenset as key:", mapping[fs])


def main():
    demo_creation_and_casting()
    demo_mutation()
    demo_algebra()
    demo_comparisons()
    demo_comprehensions_and_iteration()
    demo_copying_and_identity()
    demo_use_cases()
    demo_edge_cases()


# the main function to run all demos
if __name__ == "__main__": 
    main()

