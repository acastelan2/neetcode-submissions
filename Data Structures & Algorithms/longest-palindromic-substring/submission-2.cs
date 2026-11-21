public class Solution {
    private int CheckPali(int l, int r, string s){
        while (l >= 0 && r < s.Length && s[l] == s[r]){
            l--;
            r++;
        }

        return r-l-1;
    }
    public string LongestPalindrome(string s) {
        int start = 0;
        int maxLen = 0;

        for (int i = 0; i < s.Length; i++){
            int len = Math.Max( 
                CheckPali(i, i, s),
                CheckPali(i, i+1, s)
                );

            if (len > maxLen){
                maxLen = len;
                start = i - (len-1) / 2;
            }
        }

        return s.Substring(start, maxLen);
    }
}