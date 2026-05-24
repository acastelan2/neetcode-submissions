class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(day,holding):
            if day >= len(prices):
                return 0
            if (day,holding) in memo:
                return memo[(day,holding)]

            max_profit = 0
            if holding:
                max_profit = max(dfs(day+1, True), prices[day] + dfs(day+2, False))
            else:
                max_profit = max(dfs(day+1, False), -prices[day] + dfs(day+1, True))
            
            memo[(day,holding)] = max_profit
            return max_profit

        memo = {}
        return dfs(0,False)