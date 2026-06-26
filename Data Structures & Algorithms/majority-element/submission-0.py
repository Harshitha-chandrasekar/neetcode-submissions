class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sorted(nums)
        for i in range(len(nums)//2):
            if nums[i] == nums[i+len(nums)//2]:
                return nums[i]
        return nums[0]