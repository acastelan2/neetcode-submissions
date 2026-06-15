public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int n = nums.Length;
        var res = new int[n];
        Array.Fill(res, 1);

        for (int i = 1; i < n; i++){
            res[i] = nums[i-1] * res[i-1];
        }

        int suffix = 1;
        for (int i = n-1; i >= 0; i--){
            res[i] *= suffix;
            suffix *= nums[i];
        }

        return res;
    }
}
