# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max = float('-inf')
        self.count = 0
    def _preOrder(self, node: TreeNode):
        if not node:
            return
        if node.val >= self.max:
            self.max = node.val
            val = node.val
            self.count += 1
        else:
            val = self.max

        self._preOrder(node.left)
        self.max = val
        self._preOrder(node.right)
        
    def goodNodes(self, root: TreeNode) -> int:
        self._preOrder(root)
        return self.count