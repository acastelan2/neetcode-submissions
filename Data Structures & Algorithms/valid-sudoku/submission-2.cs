public class Solution {
    public bool IsValidSudoku(char[][] board) {
        var rows = new HashSet<char>[9];
        var cols = new HashSet<char>[9]; 
        var sqrs = new HashSet<char>[9];

        for (int i = 0; i < 9; i++)
        {
            rows[i] = new();
            cols[i] = new();
            sqrs[i] = new();
        }

        for (int i = 0; i < 9; i++){
            for (int j = 0; j < 9; j++){
                char num = board[i][j];
                if (num == '.') continue;
                
                int sqrIdx = (i / 3) * 3 + (j / 3);
                if (rows[i].Contains(num) || cols[j].Contains(num) || sqrs[sqrIdx].Contains(num)){
                    return false;
                }

                rows[i].Add(num);
                cols[j].Add(num);
                sqrs[sqrIdx].Add(num);
            }
        }

        return true;
    }
}
