class Solution {
private:
    void backtrack(string& pattern, int open, int close, int n, vector<string>& res){
        if (pattern.size() == 2*n){
            res.push_back(pattern);
            return;
        }

        if (open < n){
            pattern.push_back('(');
            backtrack(pattern, open+1, close, n, res);
            pattern.pop_back();
        }

        if (close < open){
            pattern.push_back(')');
            backtrack(pattern, open, close+1, n, res);
            pattern.pop_back();
        }

    }
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string pattern;

        backtrack(pattern, 0, 0, n, res);

        return res;
    }
};