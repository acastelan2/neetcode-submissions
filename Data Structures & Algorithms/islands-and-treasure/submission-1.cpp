class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        const array<pair<int, int>, 4> directions = {{
            {-1,0},{1,0},{0,-1},{0,1}
        }};

        queue<pair<int, int>> q;

        for (int i = 0; i < grid.size(); ++i){
            for (int j = 0; j < grid[0].size(); ++j){
                if (grid[i][j] == 0){
                    q.push({i,j});
                }
            }
        }

        while (!q.empty()){
            auto [r,c] = q.front();
            q.pop();

            for (const auto& [dr,dc] : directions){
                int nr = r + dr;
                int nc = c + dc;

                if (nr < 0 || nc < 0 || nr >= grid.size() || nc >= grid[0].size()){
                    continue;
                }

                if (grid[nr][nc] != INT_MAX){
                    continue;
                }

                grid[nr][nc] = grid[r][c] + 1;
                q.push({nr, nc});
            }
        }
    }
};
