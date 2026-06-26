class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newnums = nums.copy()
        for n in nums:
            newnums.append(n)
        return newnums