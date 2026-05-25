class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dfs(i, total):
            if total == amount:
                return 1
            if i >= len(coins) or total > amount:
                return 0
            if (i,total) in memo:
                return memo[(i,total)]
            
            times = dfs(i, total+coins[i]) + dfs(i+1, total)
            memo[(i,total)] = times
            return times

        memo = {}
        return dfs(0,0)
