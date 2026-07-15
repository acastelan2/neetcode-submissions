class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char,int> uMap1 = {}, uMap2 = {};
        int l = 0;

        for (char c : s1){
            uMap1[c]++;
        }

        for (int r = 0; r < s2.size(); ++r){            
            if (!uMap1.contains(s2[l])) l++;
            if (uMap1.contains(s2[r])) uMap2[s2[r]]++;
            
            if (r-l+1 == s1.size()){
                if (uMap1 == uMap2) return true;
                else{
                    uMap2[s2[l]]--;
                    l++;
                }
            }
        }

        return false;
    }
};
