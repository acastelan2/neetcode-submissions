class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 0
        end = -50000
        for x,y in intervals:
            if x >= end:
                end = y
            else:
                res += 1

        return res 
        