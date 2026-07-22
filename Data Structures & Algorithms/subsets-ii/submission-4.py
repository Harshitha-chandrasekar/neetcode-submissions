class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def bt(i,sub):
            res.append(sub.copy())

            for j in range(i,len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                sub.append(nums[j])
                bt(j+1,sub)
                sub.pop()

            
        bt(0,[])
        return res