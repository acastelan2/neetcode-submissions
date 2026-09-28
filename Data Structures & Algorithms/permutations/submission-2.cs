public class Solution {
    private void Backtrack(int[] nums, List<int> perm, bool[] choose, List<List<int>> res){
        if (perm.Count == nums.Length){
            res.Add(new List<int>(perm));
            return;
        }

        for (int i = 0; i < nums.Length; i++){
            if (!choose[i]){
                perm.Add(nums[i]);
                choose[i] = true;
                Backtrack(nums, perm, choose, res);
                perm.RemoveAt(perm.Count-1);
                choose[i] = false;
            }
        }
    }
    public List<List<int>> Permute(int[] nums) {
        var res = new List<List<int>>();
        var perm = new List<int>();
        var choose = new bool[nums.Length];

        Backtrack(nums, perm, choose, res);

        return res; 
    }
}
