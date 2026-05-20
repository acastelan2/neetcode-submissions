class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 1
        n = len(nums)
        high = n
        smallest = float("inf")

        while low <= high:
            #assume the original nums was rotated 'mid' times
            #then the smallest element would be in idx'th position
            mid = low + (high - low) // 2
            idx = mid%n
            
            #if this potential element is greater than the first element, then the smallest number must have been rotated more than 'mid' times
            if nums[0] <= nums[idx]:
                low = mid+1
            #the inverse of the above is true
            else:
                high = mid-1
                
            #will eventually converge to the smallest
            smallest = min(smallest,nums[idx])

        return smallest