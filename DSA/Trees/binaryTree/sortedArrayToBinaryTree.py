# Changing sorted array to bianry tree
# The time complexity of this algorithm is O(n) because we are visiting each element of the array exactly once to create the nodes of the binary tree. The space complexity is also O(n) because we are creating a new node for each element in the array, and in the worst case, the binary tree can have n nodes. Additionally, the recursive call stack can also take up to O(log n) space in the case of a balanced binary tree, but this is negligible compared to the O(n) space used for the nodes. Therefore, the overall space complexity is O(n).
import numbers


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Tecnique used: Recursion
# Time complexity: O(N)
# Space complexity: O(logN)
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def build(l,r):
            if l > r:
                return None
            mid = (l + r)//2
            root = TreeNode(nums[mid])

            root.left = build(l, mid -1)
            root.right = build(mid + 1, r)
            return root
        
        return build(0, len(nums)-1)
nums = [-10,2,3,4,5]
sol = Solution()

print(sol.sortedArrayToBST(nums))