# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 1
        l_level = 0
        r_level = 0
        l_level += self.maxDepth(root.left)
        r_level += self.maxDepth(root.right)
        return level + max(l_level,r_level)