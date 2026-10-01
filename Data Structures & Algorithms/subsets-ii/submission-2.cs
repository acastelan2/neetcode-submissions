public class Solution {
    private void Backtrack(int i, int[] nums, List<int> subset, List<List<int>> res){
        res.Add(new List<int>(subset));

        for (int j = i; j < nums.Length; j++){
            if (j > i && nums[j] == nums[j-1]) continue;

            subset.Add(nums[j]);
            Backtrack(j+1, nums, subset, res);
            subset.RemoveAt(subset.Count-1);
        }
    }
    public List<List<int>> SubsetsWithDup(int[] nums) {
        var res = new List<List<int>>();
        var subset = new List<int>();
        Array.Sort(nums);

        Backtrack(0, nums, subset, res);

        return res;
    }
}
