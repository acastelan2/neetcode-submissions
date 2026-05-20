class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = largest = nums[0]
        
        for num in nums[1:]:
            largest = max(num, num+largest)
            res = max(res, largest)

        return res