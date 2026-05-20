"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node, hash):
            if node in hash:
                return hash[node]
            
            clone = Node(node.val)
            hash[node] = clone

            for n in node.neighbors:
                clone.neighbors.append(dfs(n, hash))

            return clone

        if not node:
            return None
        hash = {}
        return dfs(node, hash)

        