# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
     
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def preOrder(node: TreeNode, low: int, high: int) -> bool:
            if not node:
                return True
            
            if not (low < node.val < high):
                return False

            return preOrder(node.left, low, node.val) and preOrder(node.right, node.val, high)
   
        return preOrder(root, float('-inf'), float('inf'))