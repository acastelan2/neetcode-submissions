public class Solution {  
    private void Backtrack(int n, int open, int close, StringBuilder pattern, List<string> res){
        if (pattern.Length == 2*n){
            res.Add(pattern.ToString());
            return;
        }

        if (open < n){
            pattern.Append('(');
            Backtrack(n, open+1, close, pattern, res);
            pattern.Length--;
        }
        
        if (close < open){
            pattern.Append(')');
            Backtrack(n, open, close+1, pattern, res);
            pattern.Length--;
        }
    }
    public List<string> GenerateParenthesis(int n) {
        var res = new List<string>();
        var pattern = new StringBuilder(2*n); 

        Backtrack(n, 0, 0, pattern, res);

        return res;
    }
}
