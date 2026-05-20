class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(source):
            while graph[source]:
                next = heapq.heappop(graph[source])
                dfs(next)
            res.append(source)

        graph = defaultdict(list)

        for src,dst in tickets:
            heapq.heappush(graph[src], dst)

        res = []
        dfs("JFK")
        return res[::-1]