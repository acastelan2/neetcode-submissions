class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() < 3) return 0;
        
        int leftMax = height[0], rightMax = height[height.size()-1];
        int left = 1, right = height.size()-2;
        int res = 0;

        while (left <= right){
            if (rightMax <= leftMax){
                res += max(0, rightMax - height[right]);
                rightMax = max(rightMax, height[right]);
                right--;
            }
            else{
                res += max(0, leftMax - height[left]);
                leftMax = max(leftMax, height[left]);
                left++;
            }
        }

        return res;
    }
};
