public class Solution {
    public bool WordBreak(string s, List<string> wordDict) {
        var words = new HashSet<string>(wordDict);
        var cache = new bool[s.Length+1];
        cache[0] = true;

        for (int i = 1; i <= s.Length; i++){
            for (int j = 0; j < i; j++){
                if (cache[j] && words.Contains(s.Substring(j, i-j))){
                    cache[i] = true;
                    break;
                }
            }
        }

        return cache[s.Length];
    }
}
