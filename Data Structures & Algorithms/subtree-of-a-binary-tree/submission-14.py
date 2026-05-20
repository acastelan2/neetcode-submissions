# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, m: Optional[TreeNode], n: Optional[TreeNode]) -> bool:
        if not m or not n:
            return m is n

        return m.val == n.val and self.isSameTree(m.left, n.left) and self.isSameTree(m.right, n.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return not root and not subRoot
        
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
