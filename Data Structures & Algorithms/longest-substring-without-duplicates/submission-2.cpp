class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0, l = 0;
        unordered_map<char,int> uMap;

        for (int r = 0; r < s.size(); ++r){
            auto it = uMap.find(s[r]);
            if (it != uMap.end()){
                l = max(l, it->second + 1);
            }

            uMap[s[r]] = r;
            res = max(res, r-l+1);
        }

        return res;
        
    }
};

