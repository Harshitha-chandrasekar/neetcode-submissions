class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def bt(i,s,sub):
            if s == target:
                res.append(sub.copy())
                return

            for j in range(i,len(nums)):
                if s+nums[j]<=target:
                    sub.append(nums[j])
                    bt(j,s+nums[j],sub)
                    sub.pop()

        bt(0,0,[])
        return res
            