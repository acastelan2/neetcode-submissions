class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<int>> rows(9), cols(9), sqrs(9);

        for (int i = 0; i < 9; ++i){
            for (int j = 0; j < 9; ++j){
                char num = board[i][j];
                if (num == '.') continue;

                int sqrIdx = (i / 3) * 3 + (j / 3);
                if (rows[i].contains(num) || cols[j].contains(num) || sqrs[sqrIdx].contains(num)){
                    return false;
                }

                rows[i].insert(num);
                cols[j].insert(num);
                sqrs[sqrIdx].insert(num);
            }
        }
        return true;
    }
};
