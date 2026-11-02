public class Solution {
    private const int Pacific = 1;
    private const int Atlantic = 2;
    private const int Both = 3;

    private void DFS(int r, int c, int prev, bool pacificConnected, ValueTuple<int,int>[] directions, int[][] heights, int[][] connected){
        if (r < 0 || c < 0 || r == heights.Length || c == heights[0].Length) return;
        if (heights[r][c] < prev) return;

        int ocean = pacificConnected ? Pacific : Atlantic;
        if ((connected[r][c] & ocean) != 0) return;
        connected[r][c] |= ocean;

        foreach ((int dr, int dc) in directions){
            DFS(r+dr, c+dc, heights[r][c], pacificConnected, directions, heights, connected);
        }
    }
    public List<List<int>> PacificAtlantic(int[][] heights) {
        int m = heights.Length;
        int n = heights[0].Length;

        var directions = new ValueTuple<int, int>[] {
            (-1, 0), (1, 0), (0, -1), (0, 1)   
        }; 

        var res = new List<List<int>>();
        var connected = new int[m][];
        for (int i = 0; i < m; i++){
            connected[i] = new int[n]; 
        }

        for (int r = 0; r < m; r++){
            DFS(r, 0, 0, true, directions, heights, connected);
            DFS(r, n-1, 0, false, directions, heights, connected);
        }

        for (int c = 0; c < n; c++){
            DFS(0, c, 0, true, directions, heights, connected);
            DFS(m-1, c, 0, false, directions, heights, connected);
        }

        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if (connected[i][j] == Both){
                    res.Add(new List<int>{i,j});
                }
            }
        }

        return res;
    }
}
