class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i):
            if i in memo:
                return memo[i]
            
            length = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    length = max(length, 1+dfs(j))
            memo[i] = length

            return length

        memo = {}
        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i))
        return res