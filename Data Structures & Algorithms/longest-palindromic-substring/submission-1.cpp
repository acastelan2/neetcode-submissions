class Solution {
private:
    void checkPali(int l, int r, int& len, const string& s, string& res){
        while (l >= 0 && r < s.length() && s[l] == s[r]){
            if (r-l+1 > len){
                len = r-l+1;
                res = s.substr(l, r-l+1);
            }

            l--;
            r++;
        }
    }
public:
    string longestPalindrome(string s) {
        string res = "";
        int len = 0;

        for (int i = 0; i < s.length(); ++i){
            checkPali(i, i, len, s, res);
            checkPali(i, i+1, len, s, res);
        }

        return res;
    }
};
