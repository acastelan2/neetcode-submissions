public class Solution {
    public int OrangesRotting(int[][] grid) {
        int res = 0;
        int numFresh = 0;

        var directions = new ValueTuple<int, int>[] {
            (-1, 0), (1, 0), (0, -1), (0, 1)   
        }; 

        var q = new Queue<ValueTuple<int,int>>();

        for (int i = 0; i < grid.Length; i++){
            for (int j = 0; j < grid[0].Length; j++){
                if (grid[i][j] == 1){
                    numFresh++;
                }
                else if (grid[i][j] == 2){
                    q.Enqueue((i,j));
                }
            }
        }

        while (q.Count > 0){
            int qSize = q.Count;

            for (int i = 0; i < qSize; i++){
                (int r, int c) = q.Dequeue();

                foreach ((int dr, int dc) in directions){
                    int nr = r + dr;
                    int nc = c + dc;

                    if (nr < 0 || nc < 0 || nr >= grid.Length || nc >= grid[0].Length){
                        continue;
                    }

                    if (grid[nr][nc] != 1){
                        continue;
                    }

                    grid[nr][nc] = 2;
                    numFresh--;
                    q.Enqueue((nr, nc));
                }
            }           

            if (q.Count > 0){
                res++;
            }
        }

        return numFresh == 0 ? res : -1;
    }
}
