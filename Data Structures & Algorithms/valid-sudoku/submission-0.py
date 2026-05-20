class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqrs = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
        
                if num == '.':
                    continue
                
                if num in rows[i]:
                    return False
                rows[i].add(num)
                
                if num in cols[j]:
                    return False
                cols[j].add(num)
                
                sqr_idx = (i // 3) * 3 + (j // 3)
                
                if num in sqrs[sqr_idx]:
                    return False
                sqrs[sqr_idx].add(num)

        return True