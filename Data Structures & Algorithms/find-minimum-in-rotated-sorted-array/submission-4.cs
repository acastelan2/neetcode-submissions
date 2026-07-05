public class Solution {
    public int FindMin(int[] nums) {
        int res = nums[0];
        int low = 0, high = nums.Length-1;

        while (low <= high){
            int mid = low + (high-low) / 2;
            res = Math.Min(res, nums[mid]);

            if (nums[mid] < nums[high]) high = mid-1;
            else low = mid+1;
        }

        return res;
    }
}
