class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, curSet, subsets):
            if i == len(nums):
                subsets.append(curSet.copy())
                return
            
            curSet.append(nums[i])
            helper(i+1, curSet, subsets)
            curSet.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            helper(i+1, curSet, subsets)

        nums.sort()
        curSet, subsets = [], []
        helper(0, curSet, subsets)

        return subsets
        