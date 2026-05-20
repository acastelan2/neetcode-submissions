class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(current_string, open, close, res):
            if len(current_string) == 2*n:
                res.append(current_string)
                return
            
            if open < n:
                backtrack(current_string+"(", open+1, close, res)
            
            if close < open:
                backtrack(current_string+")", open, close+1, res)

        res = []
        backtrack("", 0, 0, res)
        return res