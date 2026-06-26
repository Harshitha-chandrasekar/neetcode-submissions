class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i]
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i]
        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(suffix[i+1])
            elif i == len(nums)-1:
                ans.append(prefix[i-1])
            else:
                ans.append(prefix[i-1]*suffix[i+1])
        return ans