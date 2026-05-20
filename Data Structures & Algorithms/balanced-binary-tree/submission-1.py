# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.balanced = True
    def _get_height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left = self._get_height(node.left)
        right = self._get_height(node.right)
        if self.balanced:
            self.balanced = abs(left-right) <= 1
        return 1 + max(left, right)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self._get_height(root)
        return self.balanced