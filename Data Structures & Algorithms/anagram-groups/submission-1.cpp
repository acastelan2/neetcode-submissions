class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<string, vector<string>> uMap;

        for (const string& str : strs){
            array<int, 26> counts{};
            for (char c: str){
                counts[c - 'a'] += 1;
            }

            string mapKey;
            for (int i : counts){
                mapKey += ("," + to_string(i));
            }

            uMap[mapKey].push_back(str);
        }

        for (const auto& [key,val] : uMap){
            res.push_back(val);
        }
        return res;
        
    }
};
