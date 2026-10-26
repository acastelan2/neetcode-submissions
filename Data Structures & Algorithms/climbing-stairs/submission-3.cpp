class Solution {
private:
    int climb(int n, vector<int>& cache){
        if (n <= 2) return n;
        if (cache[n] != 0) return cache[n];        

        cache[n] = climb(n-1, cache) + climb(n-2, cache);
        return cache[n];
    }
public:
    int climbStairs(int n) {
        vector<int> cache(n+1, 0);
        return climb(n, cache);
    }
};
