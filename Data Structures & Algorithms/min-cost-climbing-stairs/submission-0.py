class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def memoization(n):
            if n > len(cost)-1:
                return 0
            if n in cache:
                return cache[n]

            cache[n] = cost[n] + min(memoization(n+1), memoization(n+2))
            return cache[n]

        cache = {}
        return min(memoization(0), memoization(1))