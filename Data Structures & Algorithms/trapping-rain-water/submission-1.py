class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n

        maximum = 0
        for i in range(n):
            maximum = max(maximum,height[i])
            prefix[i] = maximum

        maximum = 0
        for i in range(n-1,-1,-1):
            maximum = max(maximum,height[i])
            suffix[i] = maximum

        capacity = 0
        
        for i in range(n):
            capacity = capacity + min(prefix[i], suffix[i]) - height[i]

        return capacity
