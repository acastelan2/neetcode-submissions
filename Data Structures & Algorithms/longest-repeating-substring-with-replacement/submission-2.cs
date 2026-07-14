public class Solution {
    public int CharacterReplacement(string s, int k) {
        var dict = new Dictionary<char,int>();
        int maxF = 0, l = 0;

        for (int r = 0; r < s.Length; r++){
            if (dict.TryGetValue(s[r], out int val)){
                dict[s[r]] = val + 1;
            }
            else dict[s[r]] = 1;
            
            maxF = Math.Max(maxF, dict[s[r]]);

            if (r-l+1-maxF > k){
                dict[s[l]]--;
                l++;
            }
        }

        return s.Length-l;
    }
}
