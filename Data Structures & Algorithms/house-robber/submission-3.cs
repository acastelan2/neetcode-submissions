public class Solution {
    private int Memo(int i, int[] nums, int[] cache){
        if (i >= nums.Length) return 0;
        if (cache[i] != -1) return cache[i];

        cache[i] = nums[i] + Math.Max(Memo(i+2, nums, cache), Memo(i+3, nums, cache));

        return cache[i];
    }
    public int Rob(int[] nums) {
        var cache = new int[nums.Length];
        Array.Fill(cache, -1);

        return Math.Max(Memo(0, nums, cache), Memo(1, nums, cache));
    }
}
