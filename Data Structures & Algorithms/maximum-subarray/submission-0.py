class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = largest = smallest = nums[0]
        
        for num in nums[1:]:
            temp = max(num, num+largest, num+smallest)
            smallest = min(num, num+largest, num+smallest)
            largest = temp
            res = max(res, largest)

        return res