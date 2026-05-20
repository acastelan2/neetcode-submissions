# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack1 = [root]
        stack2 = []

        while stack1:
            current = stack1.pop()
            stack2.append(current)

            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        
        while stack2:
            res.append(stack2.pop().val)

        return res