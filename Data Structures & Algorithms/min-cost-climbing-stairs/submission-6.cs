public class Solution {
    private int Climb(int i, int[] cost, int[] cache){
        if (i >= cost.Length) return 0;
        if (cache[i] != -1) return cache[i];  

        cache[i] = cost[i] + Math.Min(Climb(i+1, cost, cache), Climb(i+2, cost, cache));

        return cache[i];        
    }
    public int MinCostClimbingStairs(int[] cost) {
        var cache = new int[cost.Length];
        Array.Fill(cache, -1);

        return Math.Min(Climb(0, cost, cache), Climb(1, cost, cache));
    }
}
