class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> uSet(nums.begin(), nums.end());
        int res = 0;
        for (int num: uSet){
            if (!uSet.contains(num-1)){
                int currNum = num;
                int length = 1;

                while (uSet.contains(currNum+1)){
                    currNum++;
                    length++;
                }

                res = max(res, length);
            }
        }

        return res;
    }
};
