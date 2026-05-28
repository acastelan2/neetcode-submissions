class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]

            longest = 1
            for dr,dc in directions:
                nr, nc = i+dr,j+dc
                if min(nr,nc) < 0 or nr == ROWS or nc == COLS:
                    continue                    
                if matrix[i][j] < matrix[nr][nc]:               
                    longest = max(longest, 1 + dfs(nr, nc))

            memo[(i,j)] = longest
            return longest

        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        memo = {}
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r,c))
                
        return res

