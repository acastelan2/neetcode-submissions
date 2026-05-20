# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        ancestor = TreeNode(float('inf'))
        if q.val < p.val:
            p,q = q,p
        while stack:
            node = stack.pop()
            if p.val <= node.val <= q.val and node.val <= ancestor.val and (node.right or node.left):
                ancestor = node
                return ancestor
                # if not stack:
                #     return ancestor
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return ancestor