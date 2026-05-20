class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(i,total):
            if total == half:
                return True
            if total > half or i == len(nums)-1:
                return False
            
            for j in range(i+1, len(nums)):
                if dfs(j, total+nums[j]):
                    return True

            return False            

        half = sum(nums)/2 
        if half % 1 != 0:
            return False

        return dfs(0,nums[0])
        