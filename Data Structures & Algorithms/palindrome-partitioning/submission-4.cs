public class Solution {
    private bool IsPalindrome(string s, int l, int r){
        while (l < r){
            if (s[l] != s[r]) return false;
            l++;
            r--;
        }

        return true;
    }
    private void DFS(int i, string s, List<string> pali, List<List<string>> res){
        if (i == s.Length){
            res.Add(new List<string>(pali));
            return;
        }

        for (int j = i; j < s.Length; j++){
            if (IsPalindrome(s, i, j)){
                pali.Add(s.Substring(i, j-i+1));
                DFS(j+1, s, pali, res);
                pali.RemoveAt(pali.Count-1);
            }
        }
    }
    public List<List<string>> Partition(string s) {
        var res = new List<List<string>>();
        var palindrome = new List<string>();

        DFS(0, s, palindrome, res);

        return res;
    }
}
