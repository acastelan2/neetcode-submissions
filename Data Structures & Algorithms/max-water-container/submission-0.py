class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_area = 0
        while left < right:
            width = right - left
            inner_area = min(heights[left],heights[right]) * width
            if inner_area > max_area:
                max_area = inner_area
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        return max_area