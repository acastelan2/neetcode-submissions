class Solution {
private:
    int dfs(int i, const vector<int>& nums, vector<int>& cache){
        if (cache[i] != -1) return cache[i];

        int length = 1;
        for (int j = i+1; j < nums.size(); ++j){
            if (nums[j] > nums[i]){
                length = max(length, 1 + dfs(j, nums, cache));
            }
        }

        cache[i] = length;
        return length;        
    }
public:
    int lengthOfLIS(vector<int>& nums) {
        int res = 0;
        vector<int> cache(nums.size(), -1);

        for (int i = 0; i < nums.size(); ++i){
            res = max(res, dfs(i, nums, cache));
        }

        return res;
    }
};
