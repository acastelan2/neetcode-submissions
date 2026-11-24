class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int currMax = nums[0];
        int currMin = nums[0];
        int res = nums[0];

        for (int i = 1; i < nums.size(); ++i) {
            int n = nums[i];

            if (n < 0) {
                swap(currMax, currMin);
            }

            currMax = max(n, currMax * n);
            currMin = min(n, currMin * n);

            res = max(res, currMax);
        }

        return res;        
    }
};
