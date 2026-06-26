class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        biggest = 0
        for n in nums:
            if n-1 not in nums:
                curr = 0
                x = n
                while x in nums:
                    x = x+1
                    curr = curr+1
                biggest = max(biggest,curr)
        return biggest