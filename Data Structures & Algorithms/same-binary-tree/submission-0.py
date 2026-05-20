# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return not p and not q
        
        stack_p = [p]
        stack_q = [q]
        
        while stack_p or stack_q:
            node_p = stack_p.pop()
            node_q = stack_q.pop()
            p_child = bool(node_p.right)
            q_child = bool(node_q.right)

            if node_p.val != node_q.val or p_child != q_child:
                return False
            if p_child:
                stack_p.append(node_p.right)
            if q_child:                
                stack_q.append(node_q.right) 
                          
            p_child = bool(node_p.left)
            q_child = bool(node_q.left)
            if p_child != q_child:
                return False
            if p_child:
                stack_p.append(node_p.left)
            if q_child:                
                stack_q.append(node_q.left) 

        return True 