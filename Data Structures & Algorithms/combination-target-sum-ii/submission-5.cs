public class Solution {
    private void DFS(int i, int total, int target, int[] candidates, List<int> curr, List<List<int>> res){
        if (total == target){
            res.Add(new List<int>(curr));
            return;
        }

        for (int j = i; j < candidates.Length; j++){
            if (total + candidates[j] > target) break;
            if (j != i && candidates[j] == candidates[j-1]) continue;

            curr.Add(candidates[j]);
            DFS(j+1, total+candidates[j], target, candidates, curr, res);
            curr.RemoveAt(curr.Count-1);
        }
    }
    public List<List<int>> CombinationSum2(int[] candidates, int target) {
        var res = new List<List<int>>();
        var curr = new List<int>();

        Array.Sort(candidates);
        DFS(0, 0, target, candidates, curr, res);

        return res;
    }
}
