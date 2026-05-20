class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        in_degree = {}
        for word in words:
            for char in word:
                graph[char] = set()
                in_degree[char] = 0

        for i in range(len(words)-1):
            a = words[i]
            b = words[i+1]
            for j in range(min(len(a), len(b))):
                if a[j] != b[j]:
                    if b[j] not in graph[a[j]]:
                        graph[a[j]].add(b[j])
                        in_degree[b[j]] += 1
                    break
            if len(a) > len(b) and a.startswith(b):
                return ""

        queue = deque([k for k,v in in_degree.items() if v == 0])
        top_sort = []

        while queue:
            char = queue.popleft()
            top_sort.append(char)
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return "".join(top_sort) if len(top_sort) == len(graph) else ""
        