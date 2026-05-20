# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_d = 0
    def _get_height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left = self._get_height(node.left)
        right = self._get_height(node.right)
        self.max_d = max(self.max_d, left+right)
        return 1 + max(left, right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self._get_height(root)
        return self.max_d
        