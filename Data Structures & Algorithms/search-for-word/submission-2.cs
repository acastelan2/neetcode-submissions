public class Solution {
    private const char Temp = '-'; 
    private bool Backtrack(char[][] board, ValueTuple<int, int>[] directions, string word, int index, int r, int c, int ROWS, int COLS){
        if (index == word.Length) return true;

        if (r < 0 || c < 0 || r == ROWS || c == COLS) return false;
        if (board[r][c] == Temp || board[r][c] != word[index]) return false;

        char origChar = board[r][c];
        board[r][c] = Temp;

        foreach ((int dr, int dc) in directions){
            if (Backtrack(board, directions, word, index+1, r+dr, c+dc, ROWS, COLS)){
                return true;
            }
        }

        board[r][c] = origChar;
        return false;
    }
    public bool Exist(char[][] board, string word) {
        var directions = new ValueTuple<int, int>[] {
            (-1, 0), (1, 0), (0, -1), (0, 1)   
        };

        int ROWS = board.Length;
        int COLS = board[0].Length;

        for (int i = 0; i < ROWS; i++){
            for (int j = 0; j < COLS; j++){
                if (Backtrack(board, directions, word, 0, i, j, ROWS, COLS)){
                    return true;
            }
            }
        }

        return false;
    }
}
