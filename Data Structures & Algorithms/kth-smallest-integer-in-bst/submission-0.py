# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.k_seen = 0
        self.found = False
        self.res = -1

    def _inorder(self, root, k):
        if not root or self.found:
            return
        else:
            self._inorder(root.left,k)
            self.k_seen += 1
            if self.k_seen == k:
                self.found = True
                self.res = root.val
                return
            self._inorder(root.right,k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self._inorder(root,k)
        return self.res

       