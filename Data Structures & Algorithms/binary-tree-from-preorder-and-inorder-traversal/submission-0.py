# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {v:i for i,v in enumerate(inorder)}        
        self.preorder_idx = 0
        
        def build(left, right):
            if left > right:
                return None

            node = TreeNode()
            node.val = preorder[self.preorder_idx]
            self.preorder_idx += 1
            
            inorder_idx = inorder_map[node.val]
            node.left = build(left, inorder_idx-1)
            node.right = build(inorder_idx+1, right)
            return node

        return build(0, len(preorder)-1)