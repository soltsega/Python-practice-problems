# Avl tree in python
# AVL tree is a tree which is balanced, which means that the difference between the heights of the left and right subtrees cannot be more than one for any node in the tree. This property ensures that the tree remains balanced and provides efficient search, insertion, and deletion operations.
# The time complexity of search, insertion, and deletion operations in an AVL tree is O(log n) in the average and worst cases, and O(1) in the best case (when the tree is perfectly balanced). The space complexity of an AVL tree is O(n) in the worst case, as it requires additional space for storing the balance factor of each node.


# let's see with an example
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # height of the node

    def __str__(self):
        return str(self.key)
    

    