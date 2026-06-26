class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if sorted(nums) == sorted(list(set(nums))):
            return False
        else:
            return True