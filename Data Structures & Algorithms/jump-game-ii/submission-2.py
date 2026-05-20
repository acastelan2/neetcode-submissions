class Solution:
    def jump(self, nums: List[int]) -> int:
        res = end = farthest = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])
            if farthest >= len(nums)-1:
                return res+1

            if i == end:
                res += 1
                end = farthest

        return res