class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref_arr = [1] * n
        suff_arr = [1] * n
        output_arr = []

        for i in range(1,n):
            pref_arr[i] = nums[i-1] * pref_arr[i-1]    

        for i in range(n-2,-1,-1):
            suff_arr[i] = nums[i+1] * suff_arr[i+1]

        for i in range(n):
            output_arr.append(pref_arr[i] * suff_arr[i])

        return output_arr      
        