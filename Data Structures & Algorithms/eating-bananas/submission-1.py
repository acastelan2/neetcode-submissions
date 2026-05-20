class Solution:
    def ceil(self, numerator: int, denominator: int) -> int:
        return -(-numerator // denominator)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        highest = max(piles)
        k = 0

        low = 1
        high = highest
        while low <= high:
            mid = low + ((high-low) // 2)
            time = sum([self.ceil(pile,mid) for pile in piles])
            if time > h:
                low = mid+1
            else:
                k = mid
                high = mid-1
        return k