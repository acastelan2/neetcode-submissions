public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) return false;

        Dictionary<char, int> dictS = new(), dictT = new();
        for (int i = 0; i < s.Length; i++){
            dictS[s[i]] = dictS.GetValueOrDefault(s[i], 0) + 1;
            dictT[t[i]] = dictT.GetValueOrDefault(t[i], 0) + 1;
        }

        return dictS.Count == dictT.Count && !dictS.Except(dictT).Any();
    }
}
