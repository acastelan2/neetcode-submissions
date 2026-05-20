class Solution:
    def rob(self, nums: List[int]) -> int:
        def memo(n, end):
            if n >= end:
                return 0
            if cache[n] != -1:
                return cache[n]

            cache[n] = nums[n] + max(memo(n+2, end), memo(n+3, end))
            return cache[n]

        if len(nums) == 1:
            return nums[0]
            
        cache = [-1] * len(nums)
        exclude_last = max(memo(0,len(nums)-1), memo(1,len(nums)-1))

        cache = [-1] * len(nums)
        exclude_first = max(memo(1,len(nums)), memo(2,len(nums)))

        return max(exclude_last, exclude_first)