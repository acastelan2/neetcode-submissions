class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0

        l_max, r_max = height[0], height[len(height)-1]
        l, r =  1, len(height)-2
        area = 0
        while l <= r:
            if r_max <= l_max:
                area += max(0, r_max - height[r]) 
                r_max = max(r_max, height[r])
                r -= 1
            else:
                area += max(0, l_max - height[l]) 
                l_max = max(l_max, height[l])
                l += 1
        return area