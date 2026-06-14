class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        vector<vector<int>> buckets(nums.size()+1);
        vector<int> res;

        for (int num : nums){
            freq[num]++;
        }

        for (const auto& [num,count] : freq){
            buckets[count].push_back(num);
        }

        for (int ct = nums.size(); ct > 0 && res.size() < k; --ct){
            for (int num : buckets[ct]){
                res.push_back(num);
                if (res.size() == k) return res;
            }
        }

        return res;
    }
};
