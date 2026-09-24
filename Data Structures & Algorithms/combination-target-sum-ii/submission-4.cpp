class Solution {
private:
    void dfs(int i, int total, int target, const vector<int>& candidates, vector<int>& curr, vector<vector<int>>& res){
        if (total == target){
            res.push_back(curr);
            return;
        }        

        for (size_t j = i; j < candidates.size(); ++j){   
            if (j > i && candidates[j] == candidates[j-1]) continue;
            if (total + candidates[i] > target) break;

            curr.push_back(candidates[j]);
            dfs(j+1, total+candidates[j], target, candidates, curr, res);
            curr.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> curr;

        sort(candidates.begin(), candidates.end());
        dfs(0, 0, target, candidates, curr, res);

        return res;
    }
};
