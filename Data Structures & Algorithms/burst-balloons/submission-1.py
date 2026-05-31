class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def dfs(l,r):
            if r - l <= 1:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]

            coins = 0
            for k in range(l+1, r):
                #assume the kth balloon is the last one popped
                #then either of the balloons to the left or right of the kth must have been the 2nd to last popped, and so on
                coins = max(coins, dfs(l,k) + dfs(k,r) + (nums[l]*nums[k]*nums[r]))

            memo[(l,r)] = coins
            return coins

        nums = [1] + nums + [1]
        memo = {}
        return dfs(0, len(nums)-1)