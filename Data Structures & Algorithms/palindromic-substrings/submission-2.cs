public class Solution {
    private int CheckPali(int l, int r, string s){
        int len = 0;
        while (l >= 0 && r < s.Length && s[l] == s[r]){
            len++;
            l--;
            r++;
        }

        return len;
    }
    public int CountSubstrings(string s) {
        int res = 0;
        for (int i = 0; i < s.Length; i++){
            res += CheckPali(i, i, s);
            res += CheckPali(i, i+1, s);
        }

        return res;
    }
}
