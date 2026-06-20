class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); ++i){
            int num = nums[i];
            if (num > 0) break;
            if (i > 0 && nums[i] == nums[i-1]) continue;

            int left = i+1, right = nums.size()-1;
            while (left < right){
                int sum = num + nums[left] + nums[right];
                if (sum < 0) left++;
                else if (sum > 0) right--;
                else{
                    res.push_back({num, nums[left], nums[right]});
                    left++;
                    right--;

                    while (nums[left] == nums[left-1] && left < right){
                        left++;
                    } 
                }
            }
        }

        return res;
    }
};
