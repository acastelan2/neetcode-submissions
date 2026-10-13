public class Solution {
    private const char Water = '0';

    private void DFS(int r, int c, ValueTuple<int,int>[] directions, char[][] grid){
        if (r < 0 || c < 0 || r == grid.Length || c == grid[0].Length) return;
        if (grid[r][c] == Water) return;

        grid[r][c] = Water;

        foreach ((int dr, int dc) in directions){
            DFS(r+dr, c+dc, directions, grid);
        }
    }

    public int NumIslands(char[][] grid) {
        int res = 0;
        var directions = new ValueTuple<int, int>[] {
            (-1, 0), (1, 0), (0, -1), (0, 1)   
        };

        for (int i = 0; i < grid.Length; ++i){
            for (int j = 0; j < grid[0].Length; ++j){
                if (grid[i][j] != Water){
                    DFS(i, j, directions, grid);
                    res++;
                }
            }
        }

        return res;
    }
}
