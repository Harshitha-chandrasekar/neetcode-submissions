class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        s = []

        leftmost = [-1]*n
        rightmost = [n]*n

        for i in range(n):
            while s and heights[s[-1]] >= heights[i]:
                s.pop()
            if s:
                leftmost[i] = s[-1]
            s.append(i)

        s = []

        for i in range(n-1,-1,-1):
            while s and heights[s[-1]] >= heights[i]:
                s.pop()
            if s:
                rightmost[i] = s[-1]
            s.append(i)

        area = 0

        for i in range(n):
            leftmost[i] = leftmost[i] + 1
            rightmost[i] = rightmost[i] - 1
            area = max(area, heights[i] * (rightmost[i] - leftmost[i] + 1))
        return area
        
                
