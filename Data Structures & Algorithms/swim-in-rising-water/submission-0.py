class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        heap = [(grid[0][0], (0, 0))]
        neighbors = [[-1,0],[1,0],[0,-1],[0,1]]
        visited = set()
        res = 0
        
        while heap:
            level, pos = heapq.heappop(heap)
            if pos in visited:
                continue
            visited.add(pos)

            res = max(res, level)
            if pos == (N-1,N-1):
                break

            for r, c in neighbors:
                nr, nc = pos[0] + r, pos[1] + c
                if min(nr, nc) < 0 or (nr, nc) in visited or nr == N or nc == N:
                    continue
                heapq.heappush(heap, (grid[nr][nc], (nr, nc)))
        
        return res