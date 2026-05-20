class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(node, res):
            visited.add(node)
            rec_stack.add(node)
            
            if len(graph[node]) == 0:
                rec_stack.remove(node)
                res.append(node)
                return
            
            for prq in graph[node]:
                if prq not in visited:
                    dfs(prq, res)
                if prq in rec_stack:
                    return
                    
            rec_stack.remove(node)       
            res.append(node)
            return

        graph = {i: [] for i in range(numCourses)}

        for course, prq in prerequisites:  
            graph[course].append(prq)

        visited, rec_stack = set(), set()
        res = []
        for node in graph:
            if node not in visited:
                dfs(node, res)

        return res if len(res) == numCourses else []