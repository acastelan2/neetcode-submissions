class Solution {
private:
    int climb(int i, const vector<int>& cost, vector<int>& cache){
        if (i >= cost.size()) return 0;
        if (cache[i] != -1) return cache[i];  

        cache[i] = cost[i] + min(climb(i+1, cost, cache), climb(i+2, cost, cache));

        return cache[i];
    }
public:
    int minCostClimbingStairs(const vector<int>& cost) {
        vector<int> cache(cost.size(), -1);

        return min(climb(0, cost, cache), climb(1, cost, cache));
    }
};
