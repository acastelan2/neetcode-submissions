class Solution {
private:
    bool isPalindrome(const string& s, int l, int r){
        while (l < r){
            if (s[l] != s[r]) return false;
            l++;
            r--;
        }
        return true;
    }
    void dfs(int i, const string& s, vector<string>& pali, vector<vector<string>>& res){
        if (i == s.length()){
            res.push_back(pali);
            return;
        }

        for (int j = i; j < s.length(); ++j){
            if (isPalindrome(s, i, j)){
                pali.push_back(s.substr(i, j-i+1));
                dfs(j+1, s, pali, res);
                pali.pop_back();
            }
        }
    }
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> palindrome;
        
        dfs(0, s, palindrome, res);
        return res;
    }
};
