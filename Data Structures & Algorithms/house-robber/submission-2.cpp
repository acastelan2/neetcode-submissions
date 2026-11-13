class Solution {
private:
    int memo(int i, const vector<int>& nums, vector<int>& cache){
        if (i >= nums.size()) return 0;
        if (cache[i] != -1) return cache[i];

        cache[i] = nums[i] + max(memo(i+2, nums, cache), memo(i+3, nums, cache));

        return cache[i];
    }
public:
    int rob(const vector<int>& nums) {
        vector<int> cache(nums.size(), -1);

        return max(memo(0, nums, cache), memo(1, nums, cache));
    }
};
