class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(node):
            visited.add(node)            
            for edge in graph[node]:
                if edge not in visited:
                    dfs(edge)                    
            return

        if len(edges) != n-1:
            return False
            
        graph = {i: [] for i in range(n)}
        for e1, e2 in edges:            
            graph[e1].append(e2)
            graph[e2].append(e1)

        if len(graph) != n:
            return False

        visited = set()
        dfs(n-1) #if all edges are connected, all nodes should be visited from any arbitrary starting node (that exists)
        return len(visited) == n

        