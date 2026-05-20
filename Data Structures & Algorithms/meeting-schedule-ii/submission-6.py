"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda i: i.start)
        meetings = [intervals[0].end]
        res = 1

        for i in intervals[1:]:
            if i.start < meetings[0]:
                heapq.heappush(meetings, i.end)
                res = max(res,len(meetings))
            else:
                heapq.heappop(meetings)
                heapq.heappush(meetings, i.end)
        return res