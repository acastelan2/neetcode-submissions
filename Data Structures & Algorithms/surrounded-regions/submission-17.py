class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        processed = set()
        queue = deque()
        neighbors = [[-1,0],[1,0],[0,-1],[0,1]]

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in processed:
                    processed.add((r,c))
                    queue.append((r,c))
                    visit = set()
                    visit.add((r,c))
                    surrounded = True
                    while queue:
                        for _ in range(len(queue)):
                            qr, qc = queue.popleft()
                            for dr, dc in neighbors:
                                nr, nc = qr+dr, qc+dc
                                if min(nr, nc) < 0 or nr == ROWS or nc == COLS:
                                    surrounded = False
                                    break
                                if (nr,nc) in visit:
                                    continue
                                if board[nr][nc] == "O":
                                    queue.append((nr, nc))
                                    visit.add((nr,nc))
                            if not surrounded:
                                queue.clear()
                                break
                    if surrounded:
                        for (nr,nc) in visit:
                            board[nr][nc] = "X"
