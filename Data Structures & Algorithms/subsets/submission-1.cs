public class Solution {
    private void Backtrack(int i, int[] nums, List<int> currSet, List<List<int>> subsets){
        if (i >= nums.Length){
            subsets.Add(new List<int>(currSet));
            return;
        }

        currSet.Add(nums[i]);
        Backtrack(i+1, nums, currSet, subsets);
        currSet.RemoveAt(currSet.Count-1);

        Backtrack(i+1, nums, currSet, subsets);
    }
    public List<List<int>> Subsets(int[] nums) {
        var res = new List<List<int>>();
        var currSet = new List<int>();
        Backtrack(0, nums, currSet, res);
        return res;
    }
}
