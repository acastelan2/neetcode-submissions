class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        current = intervals[0]
        for next in intervals[1:]:
            if next[0] <= current[1]:
                current[0] = min(current[0], next[0])
                current[1] = max(current[1], next[1])
            else:
                res.append(current)
                current = next

        res.append(current)
        return res