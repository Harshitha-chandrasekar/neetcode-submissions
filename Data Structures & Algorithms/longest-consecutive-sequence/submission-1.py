class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = list(set(nums))
        longest = 0

        for i in nums:
            if i-1 not in nums:
                length = 0
                curr = i
                while curr in nums:
                    curr = curr + 1
                    length = length + 1
                longest = max(longest,length)

        return longest