class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if min(r,c) < 0 or r == len(grid) or c == len(grid[0]):
                return
            if grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            return

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != "0":
                    dfs(r,c)
                    res += 1
        return res