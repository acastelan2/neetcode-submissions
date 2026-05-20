class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        processed = set()
        o_chars = []
        neighbors = [[-1,0],[1,0],[0,-1],[0,1]]

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in processed:
                    processed.add((r,c))
                    o_chars.append((r,c))
                    visit = set()
                    visit.add((r,c))
                    surrounded = True
                    while o_chars:
                        for _ in range(len(o_chars)):
                            qr, qc = o_chars.pop()
                            for dr, dc in neighbors:
                                nr, nc = qr+dr, qc+dc
                                if min(nr, nc) < 0 or nr == ROWS or nc == COLS:
                                    surrounded = False
                                    break
                                if (nr,nc) in visit:
                                    continue
                                if board[nr][nc] == "O":
                                    o_chars.append((nr, nc))
                                    visit.add((nr,nc))
                            if not surrounded:
                                o_chars.clear()
                                break
                    if surrounded:
                        for (nr,nc) in visit:
                            board[nr][nc] = "X"
