class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0, high = nums.size()-1;

        while (low <= high){
            int middle = low + (high-low);
            if (nums[middle] == target) return middle;
            if (nums[middle] < target) low = middle + 1;
            else high = middle - 1;
        }

        return -1;
    }
};
