class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0

        graph = {i: [] for i in range(n)}
        for s,d,c in flights:
            graph[s].append((d,c))

        heap = [(0,src,0)]
        costs = [float('inf')] * n
        stops = [float('inf')] * n

        while heap:
            cost, node, num_stops = heapq.heappop(heap)
            if node == dst:
                return cost
            if num_stops > k:
                continue

            for dest, price in graph[node]:
                accum_cost = cost + price
                if accum_cost < costs[dest] or num_stops < stops[dest]:
                    heapq.heappush(heap, (accum_cost, dest, num_stops+1))
                    costs[dest] = min(costs[dest], accum_cost)
                    stops[dest] = min(stops[dest], num_stops+1)

        return -1