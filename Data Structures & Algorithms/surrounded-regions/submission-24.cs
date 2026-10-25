public class Solution {
    private const char edgeConnected = '#';

    private void DFS(char[][] board, ValueTuple<int,int>[] directions, int r, int c){
        if (r < 0 || c < 0 || r == board.Length || c == board[0].Length || board[r][c] != 'O') return;

        board[r][c] = edgeConnected;

        foreach ((int dr, int dc) in directions){
            DFS(board, directions, r + dr, c + dc);
        }
    }

    public void Solve(char[][] board) {
        int m = board.Length;
        int n = board[0].Length;

        var directions = new ValueTuple<int, int>[] {
            (-1, 0), (1, 0), (0, -1), (0, 1)   
        }; 

        for (int r = 0; r < m; r++){
            DFS(board, directions, r, 0);
            DFS(board, directions, r, n-1);
        }

        for (int c = 0; c < n; c++){
            DFS(board, directions, 0, c);
            DFS(board, directions, m-1, c);
        }

        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if (board[i][j] == 'O'){
                    board[i][j] = 'X';
                }
                else if (board[i][j] == edgeConnected){
                    board[i][j] = 'O';
                }
            }
        }
    }
}

