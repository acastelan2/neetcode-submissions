"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda i: i.start)
        meetings = [intervals[0].end]

        for i in intervals[1:]:
            if meetings and i.start >= meetings[0]:
                heapq.heappop(meetings)
            heapq.heappush(meetings, i.end)
        return len(meetings)