class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        neighbors = [[-1,0],[1,0],[0,-1],[0,1]]

        length = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visit.add((r,c))

        distance = 1
        while queue:
            for _ in range(len(queue)):
                qr, qc = queue.popleft()
                for dr, dc in neighbors:
                    nr, nc = qr+dr, qc+dc
                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS:
                        continue
                    if (nr, nc) in visit or grid[nr][nc] != 2147483647:
                        continue
                    grid[nr][nc] = distance
                    queue.append((nr, nc))
                    visit.add((nr,nc))
            distance += 1
        