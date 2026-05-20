class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        fruits = set()
        queue = deque()
        neighbors = [[-1,0],[1,0],[0,-1],[0,1]]

        minutes = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visit.add((r,c))
                if grid[r][c] == 1:
                    fruits.add((r,c))

        while queue:
            for _ in range(len(queue)):
                qr, qc = queue.popleft()
                fruits.discard((qr, qc))
                for dr, dc in neighbors:
                    nr, nc = qr+dr, qc+dc
                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS:
                        continue
                    if (nr, nc) in visit or grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue
                    queue.append((nr, nc))
                    visit.add((nr,nc))
            if queue:
                minutes += 1
                
        if fruits:
            return -1
        else:
            return minutes


                