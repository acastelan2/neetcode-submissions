public class Solution {
    public int Trap(int[] height) {
        if (height.Length < 3) return 0;

        int leftMax = height[0], rightMax = height[^1];
        int left = 1, right = height.Length-2;
        int res = 0;

        while (left <= right){
            if (rightMax <= leftMax){
                res += Math.Max(0, rightMax - height[right]);
                rightMax = Math.Max(rightMax, height[right]);
                right--;
            }
            else{
                res += Math.Max(0, leftMax - height[left]);
                leftMax = Math.Max(leftMax, height[left]);
                left++;
            }
        }

        return res;
    }
}
