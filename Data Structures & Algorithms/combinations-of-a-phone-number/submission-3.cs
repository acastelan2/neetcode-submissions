public class Solution {
    private void Backtrack(string digits, string[] mappings, StringBuilder currStr, List<string> res, int index){
        if (index == digits.Length){
            res.Add(currStr.ToString());
            return;
        }

        string letters = mappings[digits[index] - '0'];
        foreach (char c in letters){
            currStr.Append(c);
            Backtrack(digits, mappings, currStr, res, index+1);
            currStr.Length--;
        }
    }
    public List<string> LetterCombinations(string digits) {
        if (string.IsNullOrEmpty(digits)){
            return new List<string>();
        }

        var res = new List<string>();
        var currStr = new StringBuilder(digits.Length); 

        var mappings = new string[]{
            "", "", "abc", "def", "ghi",
            "jkl", "mno", "pqrs", "tuv", "wxyz"
        };

        Backtrack(digits, mappings, currStr, res, 0);

        return res;
    }
}
