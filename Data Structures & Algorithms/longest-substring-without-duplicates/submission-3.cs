public class Solution {
    public int LengthOfLongestSubstring(string s) {
        int res = 0, l = 0;
        var dict = new Dictionary<char,int>();

        for (int r = 0; r < s.Length; r++){
            if (dict.TryGetValue(s[r], out var val)){
                l = Math.Max(l, val + 1);
            }

            dict[s[r]] = r;
            res = Math.Max(res, r-l+1);
        }

        return res;
    }
}
