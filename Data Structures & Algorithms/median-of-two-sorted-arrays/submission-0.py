class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        count = len(nums1) + len(nums2)
        half = (count + 1) // 2 

        low = 0
        high = len(nums1)
        while (low <= high):
            mid1 = low + (high-low) // 2
            mid2 = half - mid1

            left1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            left2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            right1 = nums1[mid1] if mid1 < len(nums1) else float('inf')
            right2 = nums2[mid2] if mid2 < len(nums2) else float('inf')

            if left1 > right2:
                high = mid1 - 1
                continue
            if left2 > right1:
                low = mid1 + 1
                continue
            break

        if count % 2 == 0:
            return (max(left1, left2) + min(right1, right2)) / 2
        else:
            return max(left1, left2)      

