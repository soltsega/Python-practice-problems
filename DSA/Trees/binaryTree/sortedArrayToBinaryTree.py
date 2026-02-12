# Changing sorted array to bianry tree
# The time complexity of this algorithm is O(n) because we are visiting each element of the array exactly once to create the nodes of the binary tree. The space complexity is also O(n) because we are creating a new node for each element in the array, and in the worst case, the binary tree can have n nodes. Additionally, the recursive call stack can also take up to O(log n) space in the case of a balanced binary tree, but this is negligible compared to the O(n) space used for the nodes. Therefore, the overall space complexity is O(n).
class TreeNode:
    def __init__(self, value): 
        self.value = value
        self.left = None
        self.right = None