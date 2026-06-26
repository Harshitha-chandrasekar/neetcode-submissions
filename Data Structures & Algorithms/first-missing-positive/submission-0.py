class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = 1
        while n in nums:
            n = n+1
        return n