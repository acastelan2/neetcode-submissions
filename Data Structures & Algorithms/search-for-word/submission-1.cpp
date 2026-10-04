class Solution {
private:
    using Directions = array<pair<int, int>, 4>;
    static constexpr char temp = '-';

    bool backtrack(vector<vector<char>>& board, const Directions& directions, const string& word, int index, int r, int c, int ROWS, int COLS){
        if (index == word.size()) return true;  
           
        if (min(r,c) < 0 || r == ROWS || c == COLS) return false;
        if (board[r][c] == temp || board[r][c] != word[index]) return false;

        char origChar = board[r][c];
        board[r][c] = temp;

        for (const auto& [dr,dc] : directions){
            if (backtrack(board, directions, word, index+1, r+dr, c+dc, ROWS, COLS)){
                return true;
            }
        }

        board[r][c] = origChar;
        return false;
    }

public:
    bool exist(vector<vector<char>>& board, string word) {
        const Directions directions = {{
            {-1,0},{1,0},{0,-1},{0,1}
        }};

        int ROWS = board.size();
        int COLS = board[0].size();

        for (size_t i = 0; i < ROWS; ++i){
            for (size_t j = 0; j < COLS; ++j){
                if (backtrack(board, directions, word, 0, i, j, ROWS, COLS)){
                    return true;
                }
            }
        }

        return false;
    }
};
