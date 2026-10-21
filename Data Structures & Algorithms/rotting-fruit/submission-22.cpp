class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int res = 0;
        int numFresh = 0;
        const array<pair<int, int>, 4> directions = {{
            {-1,0},{1,0},{0,-1},{0,1}
        }};

        queue<pair<int, int>> q;

        for (int i = 0; i < grid.size(); ++i){
            for (int j = 0; j < grid[0].size(); ++j){
                if (grid[i][j] == 1){
                    numFresh++;
                }
                else if (grid[i][j] == 2){
                    q.push({i,j});
                }
            }
        }

        while (!q.empty()){
            int qSize = q.size();

            for (int i = 0; i < qSize; ++i){
                const auto [r,c] = q.front();
                q.pop();

                for (const auto& [dr,dc] : directions){
                    int nr = r + dr;
                    int nc = c + dc;

                    if (nr < 0 || nc < 0 || nr >= grid.size() || nc >= grid[0].size()){
                        continue;
                    }

                    if (grid[nr][nc] != 1){
                        continue;
                    }

                    grid[nr][nc] = 2;
                    numFresh--;
                    q.push({nr, nc});
                }
            }           

            if (!q.empty()){
                res++;
            }
        }

        return numFresh == 0 ? res : -1;
    }
};
