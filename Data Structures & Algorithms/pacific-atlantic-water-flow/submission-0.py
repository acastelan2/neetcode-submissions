class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        neighbors = [[-1,0],[1,0],[0,-1],[0,1]]
        res = []
        
        for r in range(ROWS):
            for c in range(COLS):
                visit = set((r,c))
                queue = deque([(r,c)])
                in_Pacific, in_Atlantic = False, False                
                while queue:
                    for _ in range(len(queue)):
                        qr, qc = queue.popleft()
                        for dr, dc in neighbors:
                            if in_Pacific and in_Atlantic:
                                break
                            nr, nc = qr+dr, qc+dc
                            if min(nr, nc) < 0:
                                in_Pacific = True
                                continue
                            if nr == ROWS or nc == COLS:
                                in_Atlantic = True
                                continue
                            if (nr, nc) in visit or heights[nr][nc] > heights[qr][qc]:
                                continue
                            queue.append((nr, nc))
                            visit.add((nr,nc))

                if in_Pacific and in_Atlantic:
                    res.append([r,c])

        return res