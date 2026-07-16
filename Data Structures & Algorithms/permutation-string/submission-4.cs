public class Solution {
    public bool CheckInclusion(string s1, string s2) {
        Dictionary<char,int> dict1 = new(), dict2 = new();
        int l = 0;

        foreach (char c in s1){
            if (dict1.TryGetValue(c, out int val)){
                dict1[c] = val + 1;
            }
            else dict1[c] = 1;
        }

        for (int r = 0; r < s2.Length; r++){
            if (!dict1.ContainsKey(s2[l])) l++;
            
            if (dict1.ContainsKey(s2[r])){
                if (dict2.TryGetValue(s2[r], out int val)){
                    dict2[s2[r]] = val + 1;
                }
                else dict2[s2[r]] = 1;
            }
            
            if (r-l+1 == s1.Length){
                if (dict1.Count == dict2.Count && !dict1.Except(dict2).Any()) return true;
                else{
                    dict2[s2[l]]--;
                    l++;
                }
            }
        }

        return false;
    }
}
