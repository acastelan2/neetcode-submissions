class Solution:
    def rob(self, nums: List[int]) -> int:
        def memo(n):
            if n >= len(nums):
                return 0
            if cache[n] != -1:
                return cache[n]

            cache[n] = nums[n] + max(memo(n+2), memo(n+3))
            return cache[n]

        cache = [-1] * len(nums)
        return max(memo(0), memo(1))