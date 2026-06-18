class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i+1<len(nums):
            if nums[i] == nums[i+1]:
                i = i+2
            else:
                return nums[i]
        return nums[-1]