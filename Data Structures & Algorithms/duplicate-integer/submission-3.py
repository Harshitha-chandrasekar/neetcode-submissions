class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = list(set(nums))
        if sorted(s) == sorted(nums):
            return False
        return True
        