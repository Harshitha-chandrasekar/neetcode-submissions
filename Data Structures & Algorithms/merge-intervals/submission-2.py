class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        intervals.sort()
        while i+1<len(intervals):
            if intervals[i][1]<intervals[i+1][0]:
                i = i+1
            else:
                intervals[i][0] = min(intervals[i][0],intervals[i+1][0])
                intervals[i][1] = max(intervals[i][1],intervals[i+1][1])
                intervals.pop(i+1)

        return intervals