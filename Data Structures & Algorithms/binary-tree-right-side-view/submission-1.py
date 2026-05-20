# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = []
        q.append(root)
        level = 0
        while q:
            res.extend([0])
            for _ in range(len(q)):
                node = q.pop(0)
                last_seen = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                res[level] = last_seen
            level += 1
        return res