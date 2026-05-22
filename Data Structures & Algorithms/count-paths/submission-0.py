class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(r,c):
            if min(r,c) < 0 or r == m or c == n:
                return 0
            if r == m-1 and c == n-1:
                return 1
            if (r,c) in memo:
                return memo[(r,c)]

            paths = dfs(r+1, c) + dfs(r, c+1)
            memo[(r,c)] = paths

            return paths

        memo = {}
        return dfs(0,0)