class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def memoization(n):
            if n > len(cost)-1:
                return 0
            if cache[n] != -1:
                return cache[n]

            cache[n] = cost[n] + min(memoization(n+1), memoization(n+2))
            return cache[n]

        cache = [-1] * len(cost)
        memoization(0)
        return min(cache[0], cache[1])