class Solution {
private:
    void backtrack(int i, const vector<int>& nums, vector<int>& subset, vector<vector<int>>& res){
        res.push_back(subset);

        for (int j = i; j < nums.size(); ++j){
            if (j > i && nums[j] == nums[j-1]) continue;

            subset.push_back(nums[j]);
            backtrack(j+1, nums, subset, res);
            subset.pop_back();
        }
        
    }
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> subset;

        backtrack(0, nums, subset, res);

        return res;
    }
};
