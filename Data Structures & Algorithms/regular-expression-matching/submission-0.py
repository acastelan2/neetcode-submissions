class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if j == len(p):
                return i == len(s)

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            res = False           
            if j+1 < len(p) and p[j+1] == "*":
                res = dfs(i,j+2) or (match and dfs(i+1, j))           
            else:
                res = match and dfs(i+1, j+1)
                
            memo[(i,j)] = res
            return res

        memo = {}
        return dfs(0,0)