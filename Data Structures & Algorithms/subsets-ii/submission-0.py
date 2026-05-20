class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, curSet, subsets):
            if i == len(nums):
                subsets.append(curSet.copy())
                return
            
            curSet.append(nums[i])
            backtrack(i+1, curSet, subsets)
            curSet.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1, curSet, subsets)

        nums.sort()
        curSet, subsets = [], []
        backtrack(0, curSet, subsets)

        return subsets
        