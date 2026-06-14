public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        var freq = new Dictionary<int, int>();
        var buckets = new List<int>[nums.Length+1];
        var res = new List<int>();

        foreach (int num in nums){
            freq[num] = freq.GetValueOrDefault(num, 0) + 1;
        }

        foreach (var (num, count) in freq){
            if (buckets[count] == null){
                buckets[count] = new List<int>();
            }
            buckets[count].Add(num);
        }

        for (int ct = nums.Length; ct > 0 && res.Count < k; ct--){
            if (buckets[ct] == null) continue;

            foreach (int num in buckets[ct]){
                res.Add(num);
                if (res.Count == k) return res.ToArray();
            }
        }

        return res.ToArray();
    }
}
