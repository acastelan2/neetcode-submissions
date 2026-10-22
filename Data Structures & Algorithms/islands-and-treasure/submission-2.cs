public class Solution {
    public void islandsAndTreasure(int[][] grid) {
        var directions = new ValueTuple<int, int>[] {
            (-1, 0), (1, 0), (0, -1), (0, 1)   
        }; 

        var q = new Queue<ValueTuple<int,int>>();

        for (int i = 0; i < grid.Length; i++){
            for (int j = 0; j < grid[0].Length; j++){
                if (grid[i][j] == 0){
                    q.Enqueue((i,j));
                }
            }
        }

        while (q.Count > 0){
            (int r, int c) = q.Dequeue();

            foreach ((int dr, int dc) in directions){
                int nr = r + dr;
                int nc = c + dc;

                if (nr < 0 || nc < 0 || nr >= grid.Length || nc >= grid[0].Length){
                    continue;
                }

                if (grid[nr][nc] != int.MaxValue){
                    continue;
                }

                grid[nr][nc] = grid[r][c] + 1;
                q.Enqueue((nr, nc));
            }
        }
    }
}
