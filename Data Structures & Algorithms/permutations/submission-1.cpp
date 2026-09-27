class Solution {
private:
    void backtrack(const vector<int>& nums, vector<int>& perm, vector<bool>& choose, vector<vector<int>>& res){
        if (perm.size() == nums.size()){
            res.push_back(perm);
            return;
        }

        for (size_t i = 0; i < nums.size(); ++i){
            if (!choose[i]){
                perm.push_back(nums[i]);
                choose[i] = true;
                backtrack(nums, perm, choose, res);
                perm.pop_back();
                choose[i] = false;
            }
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> perm;
        vector<bool> choose(nums.size(), false);

        backtrack(nums, perm, choose, res);
        
        return res;
    }
};
