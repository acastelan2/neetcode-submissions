class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> words(wordDict.begin(), wordDict.end());

        vector<bool> cache(s.length() + 1);
        cache[0] = true;

        for (size_t i = 1; i <= s.length(); ++i){
            for (size_t j = 0; j < i; ++j){
                if (cache[j] && words.contains(s.substr(j, i-j))){
                    cache[i] = true;
                    break;
                }
            }
        }

        return cache[s.length()];
    }
};
