class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        ans.append(math.prod(nums[1:]))
        for i in range(1,len(nums)):
            if nums[i] == 0:
                x = 1
                for j in range(len(nums)):
                    if i != j:
                        x = x*nums[j]
            else:
                x = int(ans[i-1]*nums[i-1]/nums[i])
            ans.append(x)
        return ans