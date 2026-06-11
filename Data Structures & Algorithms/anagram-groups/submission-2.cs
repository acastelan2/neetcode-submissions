public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var dict = new Dictionary<string, List<string>>();

        foreach (string str in strs){
            int[] counts = new int[26];
            foreach (char c in str){
                counts[c-'a'] += 1;                
            }

            string dictKey = string.Join(",", counts);
            if (!dict.TryGetValue(dictKey, out var list))
            {
                list = new List<string>();
                dict[dictKey] = list;
            }
            list.Add(str);
        }

        return dict.Values.ToList<List<string>>();;
    }
}
