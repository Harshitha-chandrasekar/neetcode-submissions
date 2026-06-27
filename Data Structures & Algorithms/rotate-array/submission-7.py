class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k%len(nums)
        if k == 0 or k == len(nums):
            return
        temp = nums[-k:]
        for i in range(len(nums)-k-1,-1,-1):
            nums[i+k] = nums[i]
        nums[:k] = temp