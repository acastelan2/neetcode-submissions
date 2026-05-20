# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val < p.val:
            p,q = q,p

        while root:
            if p.val <= root.val <= q.val:
                return root
            
            if root.val < p.val <= q.val and root.right:
                root = root.right
            elif p.val <= q.val < root.val and root.left:                    
                root = root.left 

        return root