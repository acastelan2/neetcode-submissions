class Solution {
private:
    using Directions = array<pair<int, int>, 4>;
    static constexpr char water = '0';

    void dfs(int r, int c, const Directions& directions, vector<vector<char>>& grid){
        
        if (r < 0 || c < 0 || r == grid.size() || c == grid[0].size()) return;
        if (grid[r][c] == water) return;

        grid[r][c] = water;

        for (const auto& [dr,dc] : directions){
            dfs(r+dr, c+dc, directions, grid);
        }
    }
    
public:
    int numIslands(vector<vector<char>>& grid) {
        int res = 0;
        const Directions directions = {{
            {-1,0},{1,0},{0,-1},{0,1}
        }};

        for (int i = 0; i < grid.size(); ++i){
            for (int j = 0; j < grid[0].size(); ++j){
                if (grid[i][j] != water){
                    dfs(i, j, directions, grid);
                    res++;
                }
            }
        }

        return res;
    }
};
