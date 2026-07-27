"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        
        active = 0
        maxr = 0
        s, e = 0, 0
        while s < len(intervals):
            if starts[s] < ends[e]:
                active = active + 1
                s = s + 1
            else:
                active = active - 1
                e = e + 1
            
            maxr = max(maxr, active)

        return maxr