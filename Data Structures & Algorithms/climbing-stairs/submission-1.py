class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n):
            if cache[n] != 0:
                return cache[n]
            if n <= 2:
                return n
            
            cache[n] = climb(n-1) + climb(n-2)
            return climb(n)

        cache = [0] * (n+1)
        return climb(n)