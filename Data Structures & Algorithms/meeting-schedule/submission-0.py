"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda i: i.end)
        last = 0
        for i in intervals:
            if i.start >= last:
                last = i.end
            else:
                return False
        return True