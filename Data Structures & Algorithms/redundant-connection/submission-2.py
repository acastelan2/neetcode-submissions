class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(node):
            if node == a:
                return True
            rec_nodes[node] = True
            
            for edge in graph[node]:
                if not rec_nodes[edge]:
                    if dfs(edge):
                        return True

            return False

        graph = {i: [] for i in range(len(edges)+1)}
        res = [0,0]
        for a,b in edges:
            rec_nodes = [False] * (len(edges)+1)
            graph[a].append(b)
            if dfs(b):
                res[0], res[1] = a,b
            graph[b].append(a)

        return res
