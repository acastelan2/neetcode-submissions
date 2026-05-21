class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(i, curr_sum):
            if i == len(nums)-1:
                return 1 if curr_sum == target else 0
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            times = 0
            times += backtrack(i+1, curr_sum+nums[i+1])
            times += backtrack(i+1, curr_sum-nums[i+1])

            memo[(i, curr_sum)] = times
            return times

        memo = {}
        res = 0
        res += backtrack(0, nums[0])
        res += backtrack(0, -nums[0])

        return res