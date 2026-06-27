class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l = 0
        r = len(heights)-1
        while l<r:
            water = (r-l)*min(heights[r],heights[l])
            ans = max(water,ans)
            if heights[l]<heights[r]:
                l = l+1
            else:
                r = r-1
        
        return ans