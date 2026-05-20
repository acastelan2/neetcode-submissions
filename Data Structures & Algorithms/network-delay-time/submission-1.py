class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(n+1)}
        for u,v,t in times:
            graph[u].append((v,t))

        heap = []
        heapq.heappush(heap, (0,k))
        smallestDist = {}

        while heap:
            dist, node = heapq.heappop(heap)
            if node in smallestDist:
                continue
            
            smallestDist[node] = dist
            for target,time in graph[node]:
                if target not in smallestDist:
                    newDist = dist + time
                    heapq.heappush(heap, (newDist, target))
                
        if len(smallestDist) != n:
            return -1
        else:
            return max(smallestDist.values())