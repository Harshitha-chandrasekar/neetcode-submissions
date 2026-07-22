class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(used,sub):
            if len(sub) == len(nums):
                res.append(sub.copy())
                return

            for j in range(0,len(nums)):
                if nums[j] not in used:
                    used.add(nums[j])
                    sub.append(nums[j])
                    bt(used,sub)
                    sub.pop()
                    used.remove(nums[j])

        bt(set(),[])
        return res