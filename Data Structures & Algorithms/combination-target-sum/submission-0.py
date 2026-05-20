class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(target, start, currCombi, res):
            if target == 0:
                res.append(currCombi.copy())
                return
            
            for i in range(start, len(nums)):
                if nums[i] > target:
                    continue
                
                currCombi.append(nums[i])
                backtrack(target-nums[i], i, currCombi, res)
                currCombi.pop()

        currCombi, res = [], []
        nums.sort()
        backtrack(target, 0, currCombi, res)
        return res