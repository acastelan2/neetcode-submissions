class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def hasCycle(graph):
            for node in graph:
                if node not in visited:
                    if dfs(node):
                        return True
            return False
        
        def dfs(node):
            visited.add(node)
            rec_stack.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True

            rec_stack.remove(node)
            return False

        graph = {}
        for course, pr in prerequisites:
            if pr not in graph:
                graph[pr] = []
            if course not in graph:
                graph[course] = []            
            graph[pr].append(course)

        visited = set()
        rec_stack = set()
        return not hasCycle(graph)
        
