class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(i, curr_sum):
            if i == len(nums)-1:
                return 1 if curr_sum == target else 0
                
            times = 0
            times += backtrack(i+1, curr_sum+nums[i+1])
            times += backtrack(i+1, curr_sum-nums[i+1])

            return times

        res = 0
        res += backtrack(0, nums[0])
        res += backtrack(0, -nums[0])

        return res