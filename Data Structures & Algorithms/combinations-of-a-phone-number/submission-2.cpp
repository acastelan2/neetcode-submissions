class Solution {
private:
    using Mapping = array<string, 10>;

    void backtrack(const string& digits, const Mapping& mappings, string& currStr, vector<string>& res, int index) const{
        if (index == digits.size()){
            res.push_back(currStr);
            return;
        }

        const string& letters = mappings[digits[index] - '0'];
        for (char c : letters){
            currStr.push_back(c);
            backtrack(digits, mappings, currStr, res, index+1);
            currStr.pop_back();
        }
        
    }
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        vector<string> res;
        string currStr;
        currStr.reserve(digits.size());

        const Mapping mappings = {
            "", "", "abc", "def", "ghi",
            "jkl", "mno", "pqrs", "tuv", "wxyz"
        };
      

        backtrack(digits, mappings, currStr, res, 0);    

        return res;
    }
};
