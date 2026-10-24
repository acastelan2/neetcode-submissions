class Solution {
private:
    using Directions = array<pair<int, int>, 4>;
    static constexpr char edgeConnected = '#';

    void dfs(vector<vector<char>>& board, const Directions& directions, int r, int c){
        if (r < 0 || c < 0 || r == board.size() || c == board[0].size() || board[r][c] != 'O') return;

        board[r][c] = edgeConnected;

        for (const auto& [dr,dc] : directions){
            dfs(board, directions, r + dr, c + dc);
        }
    }

public:
    void solve(vector<vector<char>>& board) {
        int m = board.size();
        int n = board[0].size();

        const Directions directions = {{
            {-1, 0}, {1, 0}, {0, -1}, {0, 1}
        }};

        for (int r = 0; r < m; ++r){
            dfs(board, directions, r, 0);
            dfs(board, directions, r, n - 1);
        }

        for (int c = 0; c < n; ++c){
            dfs(board, directions, 0, c);
            dfs(board, directions, m - 1, c);
        }

        for (auto& row : board){
            for (char& cell : row){
                if (cell == 'O'){
                    cell = 'X';
                } 
                else if (cell == edgeConnected){
                    cell = 'O';
                } 
            }
        }
    }
};
