class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            for edge in graph[node]:
                if edge not in visited:
                    dfs(edge)
            return
        
        graph = {i: [] for i in range(n)}
        for e1, e2 in edges:            
            graph[e1].append(e2)
            graph[e2].append(e1)

        visited = set()
        count = 0
        for node in graph:
            if node not in visited:
                dfs(node)
                count += 1

        return count