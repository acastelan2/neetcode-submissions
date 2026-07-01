class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n = matrix.size(), m = matrix[0].size();
        int low = 0, high = n*m-1;

        while (low <= high){
            int middle = low + (high-low) / 2;
            int value = matrix[middle / m][middle % m];
            
            if (value == target) return true;
            if (value < target) low = middle+1;
            else high = middle-1;
        }

        return false;
    }
};
