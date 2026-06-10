public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var dict = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++){
            int num = nums[i];

            if (dict.TryGetValue((target-num), out int idx)){
                return new[] {idx, i};
            }

            dict[num] = i;
        }

        return Array.Empty<int>();
    }
}
