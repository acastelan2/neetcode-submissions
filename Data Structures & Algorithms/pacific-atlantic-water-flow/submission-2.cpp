class Solution {
private:
    using Directions = array<pair<int, int>, 4>;
    static constexpr int pacific = 1;
    static constexpr int atlantic = 2;
    static constexpr int both = 3;

    void dfs(int r, int c, int previous, bool pacificConnected, const Directions& directions, const vector<vector<int>>& heights, vector<vector<int>>& connected){
        if (r < 0 || c < 0 || r == heights.size() || c == heights[0].size()) return;
        if (heights[r][c] < previous) return;

        const int ocean = pacificConnected ? pacific : atlantic;
        //already connected to curr ocean
        if (connected[r][c] & ocean) return;
        //connect to curr ocean
        connected[r][c] |= ocean;

        for (const auto& [dr,dc] : directions){
            dfs(r+dr, c+dc, heights[r][c], pacificConnected, directions, heights, connected);
        }
        
    }
public:
    vector<vector<int>> pacificAtlantic(const vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();

        vector<vector<int>> res;
        vector<vector<int>> connected(m, vector<int>(n));

        const Directions directions = {{
            {-1,0},{1,0},{0,-1},{0,1}
        }};

        for (int r = 0; r < m; ++r){
            dfs(r, 0, 0, true, directions, heights, connected);
            dfs(r, n-1, 0, false, directions, heights, connected);
        }

        for (int c = 0; c < n; ++c){
            dfs(0, c, 0, true, directions, heights, connected);
            dfs(m-1, c, 0, false, directions, heights, connected);
        }

        for (int i = 0; i < m; ++i){
            for (int j = 0; j < n; ++j){
                if (connected[i][j] == both){
                    res.push_back({i,j});
                }
            }
        }

        return res;
    }
};
