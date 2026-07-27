class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        i = 0
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            current_start = intervals[i][0]
            current_end = intervals[i][1]
            
            if current_start < prev_end:
                count += 1
                prev_end = min(prev_end, current_end)
            else:
                prev_end = current_end
                
        return count