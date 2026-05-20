class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i):
            if i == len(nums)-1:
                return 1
            if i in memo:
                return memo[i]
            
            length = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    length = 1
                    length += dfs(j)
                memo[i] = max(memo.get(i,0), length)

            return memo[i]

        memo = {}
        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i))
        return res