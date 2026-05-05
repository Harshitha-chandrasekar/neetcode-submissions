class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        
        if nums is None:
            return []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] > 0:
                break

            l = i+1
            r = len(nums) - 1
            while l<r:
                s = nums[l] + nums[r] + nums[i]

                if s < 0:
                    l = l + 1
                if s > 0 :
                    r = r - 1
                if s == 0:
                    li = [nums[l],nums[r],nums[i]]
                    li.sort()
                    if li not in ans:
                        ans.append(li)
                    l = l+1
                    r = r-1

        return ans    
        

