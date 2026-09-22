class Solution {
private:
    void dfs(int i, int total, int target, const vector<int>& nums, vector<int>& curr, vector<vector<int>>& res){
        if (total == target){
            res.push_back(curr);
            return;
        }

        for (size_t j = i; j < nums.size(); ++j){
            if (total + nums[j] > target) return;
            
            curr.push_back(nums[j]);
            dfs(j, total+nums[j], target, nums, curr, res);
            curr.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        vector<int> curr;

        sort(nums.begin(), nums.end());
        dfs(0, 0, target, nums, curr, res);
        return res;
    }
};
