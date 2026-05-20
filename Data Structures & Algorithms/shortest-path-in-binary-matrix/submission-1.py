class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0,0))
        visit.add((0,0))
        neighbors = [[-1,0],[1,0],[0,-1],[0,1],[-1,1],[1,1],[1,-1],[-1,-1]]

        length = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if grid[r][c] == 1:
                    return -1
                if r == ROWS-1 and c == COLS-1:
                    return length+1
                
                for dr, dc in neighbors:
                    if min(r+dr,c+dc) < 0 or r+dr == ROWS or c+dc == COLS:
                        continue
                    if (r+dr,c+dc) in visit or grid[r+dr][c+dc] == 1:
                        continue
                    queue.append((r+dr,c+dc))
                    visit.add((r+dr, c+dc))
            length += 1

        return -1