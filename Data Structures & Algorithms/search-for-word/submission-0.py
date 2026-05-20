class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, i):
            if i == len(word):
                return True
            
            if row < 0 or col < 0 or row == rows or col == cols:
                return False
            if board[row][col] != word[i]:
                return False

            temp = board[row][col]
            board[row][col] = '.'
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]

                if backtrack(new_row, new_col, i+1):
                    return True
            
            board[row][col] = temp
            return False

        rows = len(board)
        cols = len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if backtrack(r,c,0):
                        return True

        return False
            