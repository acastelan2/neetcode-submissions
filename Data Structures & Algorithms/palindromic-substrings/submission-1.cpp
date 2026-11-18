class Solution {
private:
    void checkPali(int l, int r, int& res, const string& s){
        while (l >= 0 && r < s.length() && s[l] == s[r]){
            res++;
            l--;
            r++;
        }
    }
public:
    int countSubstrings(string s) {
        int res = 0;
        for (int i = 0; i < s.length(); ++i){
            checkPali(i, i, res, s);
            checkPali(i, i+1, res, s);
        }

        return res;
    }
};
