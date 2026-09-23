public class Solution {
    private void DFS(int i, int total, int target, int[] nums, List<int> curr, List<List<int>> res){
        if (total == target){
            res.Add(new List<int>(curr));
            return;
        }

        for (int j = i; j < nums.Length; j++){
            if (total + nums[j] > target) return;

            curr.Add(nums[j]);
            DFS(j, total+nums[j], target, nums, curr, res);
            curr.RemoveAt(curr.Count-1);
        }
    }

    public List<List<int>> CombinationSum(int[] nums, int target) {
        var res = new List<List<int>>();
        var curr = new List<int>();

        Array.Sort(nums);
        DFS(0, 0, target, nums, curr, res);
        return res; 
    }
}
