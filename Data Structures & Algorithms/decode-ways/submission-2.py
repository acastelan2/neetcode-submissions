class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0

            res = dfs(i+1)
            if i+1 < len(s) and int(s[i:i+2]) <= 26:
                res += dfs(i+2)

            memo[i] = res
            return res
        
        memo = {}
        return dfs(0)