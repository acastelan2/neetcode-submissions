public class Solution {
    private int Climb(int n, int[] cache){
        if (n <= 2) return n;
        if (cache[n] != 0) return cache[n];

        cache[n] = Climb(n-1, cache) + Climb(n-2, cache);
        return cache[n];
    }
    public int ClimbStairs(int n) {     
        var cache = new int[n+1];
        return Climb(n, cache);
    }
}
