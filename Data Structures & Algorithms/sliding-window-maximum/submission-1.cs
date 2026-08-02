public class Solution {
    public int[] MaxSlidingWindow(int[] nums, int k) {
        var res = new List<int>();
        var dq = new LinkedList<int>();

        for (int i = 0; i < nums.Length; i++){
            while (dq.Count != 0 && dq.First.Value < i-k+1){
                dq.RemoveFirst();
            }

            while (dq.Count != 0 && nums[dq.Last.Value] <= nums[i]){
                dq.RemoveLast();
            }

            dq.AddLast(i);

            if (i >= k-1){
                res.Add(nums[dq.First.Value]);
            }
        }

        return res.ToArray();
    }
}
