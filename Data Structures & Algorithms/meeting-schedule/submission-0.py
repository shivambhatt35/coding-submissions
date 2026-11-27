"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda x: x.start)

        for i in range(1,len(intervals)):

            prev_time = intervals[i-1].end
            curr_time = intervals[i].start

            if prev_time > curr_time:
                return False
        
        return True

