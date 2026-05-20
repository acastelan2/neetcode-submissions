class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            lowest = min(lowest, prices[i])
            profit = max(profit, prices[i] - lowest)

        return profit