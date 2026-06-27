class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        quad = []

        def ksum(k,start,target):
            if k!=2:
                for i in range(start,len(nums)-k+1):
                    if i>start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    ksum(k-1,i+1,target-nums[i])
                    quad.pop()
                return
            l = start
            r = len(nums)-1
            while l<r:
                if nums[l]+nums[r] == target:
                    ans.append(quad+[nums[l],nums[r]])
                    l = l+1
                    r = r-1
                    while l<r and nums[l] == nums[l-1]:
                        l = l+1
                    while l<r and nums[r] == nums[r+1]:
                        r = r-1
                    
                elif nums[l]+nums[r] < target:
                    l = l+1
                else:
                    r = r-1

        ksum(4,0,target)
        return ans
