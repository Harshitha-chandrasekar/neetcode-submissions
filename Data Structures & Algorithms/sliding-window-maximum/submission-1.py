class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        i = 0
        while i+k<len(nums)+1:
            ans.append(max(nums[i:i+k]))
            i = i+1
        return ans