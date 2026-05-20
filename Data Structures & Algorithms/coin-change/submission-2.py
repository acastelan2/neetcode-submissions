class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        res = -1
        memo = {}
        for i in range(len(coins)):
            num = coins[i]
            memo[num] = 1
            for j in range(num+1,amount+1):
                if (j-num) in memo:
                    total = memo[num] + memo[j-num]
                    memo[j] = min(memo.get(j,amount), total)
            res = memo.get(amount, res)
        
        return res