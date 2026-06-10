class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> uMap;
        for (int i = 0; i < nums.size(); ++i) {
            const int num = nums[i];
            
            auto it = uMap.find(target-num);
            if (it != uMap.end()){
                return {it->second, i};
            } 

            uMap[num] = i;         
        }
    }
};
