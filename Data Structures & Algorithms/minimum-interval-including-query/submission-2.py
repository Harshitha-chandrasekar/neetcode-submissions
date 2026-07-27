class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = []
        for q in queries:
            currm = float('inf')
            for inter in intervals:
                if inter[0] <= q <= inter[1]:
                    currm = min(currm,inter[1]-inter[0]+1)
            if currm == float('inf'):
                ans.append(-1)
            else:
                ans.append(currm)

        return ans