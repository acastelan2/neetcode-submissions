class Solution {
private:
    using Directions = array<pair<int, int>, 4>;
    static constexpr int water = 0;
    int dfs(vector<vector<int>>& grid, const Directions& directions, int r, int c){
        if (r < 0 || c < 0 || r == grid.size() || c == grid[0].size()) return 0;
        if (grid[r][c] == water) return 0;

        grid[r][c] = water;
        int area = 1;
        for (const auto& [dr,dc] : directions){
            area += dfs(grid, directions, r+dr, c+dc);
        }

        return area;
    }
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int res = 0;
        const Directions directions = {{
            {-1,0},{1,0},{0,-1},{0,1}
        }};

        for (int i = 0; i < grid.size(); ++i){
            for (int j = 0; j < grid[0].size(); ++j){
                if (grid[i][j] != water){
                    res = max(res, dfs(grid, directions, i, j));
                }
            }
        }

        return res;
    }
};
