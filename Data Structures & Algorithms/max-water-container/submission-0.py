class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        vol = 0
        while (l<r):
            curr = (r-l) * min(heights[r],heights[l])
            vol = max(curr,vol)
            if heights[l] < heights[r]:
                l = l+1
            else:
                r = r-1
        
        return vol