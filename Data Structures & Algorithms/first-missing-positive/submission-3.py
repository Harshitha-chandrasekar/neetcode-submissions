class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        exists = [False] * len(nums)
        for n in nums:
            if 0 < n <= len(nums):
                exists[n-1] = True

        for i, e in enumerate(exists):
            if not e:
                return i + 1
        return len(nums) + 1