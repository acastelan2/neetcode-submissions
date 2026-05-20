class Solution:
    def minCostConnectPoints(self, points) -> int:
        def getDist(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])

        n = len(points)
        heap = [(0,0)]
        visited = set()
        min_distances = [float('inf')] * n
        min_distances[0] = 0

        while len(visited) < n:
            dist, idx = heapq.heappop(heap)
            if idx in visited:
                continue

            visited.add(idx)
            for i in range(n):
                if i not in visited:
                    manh_dist = getDist(points[idx], points[i])
                    if manh_dist < min_distances[i]:
                        min_distances[i] = manh_dist
                        heapq.heappush(heap, (manh_dist,i))

        return sum(min_distances)