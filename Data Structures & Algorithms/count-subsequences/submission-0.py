class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def dfs(i,j):       
            if j >= len(t):
                return 1                         
            if i >= len(s):
                return 0     
            if (i,j) in memo:
                return memo[(i,j)]

            num = 0
            if s[i] == t[j]:
                num += dfs(i+1, j+1)
            num += dfs(i+1, j)

            memo[(i,j)] = num
            return num

        memo = {}
        return dfs(0,0)
                