public class Solution {
    private const int Water = 0;

    private int DFS(int[][] grid, ValueTuple<int,int>[] directions, int r, int c){
        if (r < 0 || c < 0 || r == grid.Length || c == grid[0].Length) return 0;
        if (grid[r][c] == Water) return 0;   

        grid[r][c] = Water;
        int area = 1;
        foreach ((int dr, int dc) in directions){
            area += DFS(grid, directions, r+dr, c+dc);
        }     

        return area;
    }

    public int MaxAreaOfIsland(int[][] grid) {
        int res = 0;
        var directions = new ValueTuple<int, int>[] {
            (-1, 0), (1, 0), (0, -1), (0, 1)   
        }; 

        for (int i = 0; i < grid.Length; i++){
            for (int j = 0; j < grid[0].Length; j++){
                if (grid[i][j] != Water){
                    res = Math.Max(res, DFS(grid, directions, i, j));
                }
            }
        }

        return res;
    }
}
