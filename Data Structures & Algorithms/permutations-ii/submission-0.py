class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def bt(idx,sub):
            if len(sub) == len(nums):
                res.append(sub.copy())
                return

            for j in range(len(nums)):
                if j > 0 and nums[j] == nums[j - 1] and (j - 1) not in idx:
                    continue
                if j not in idx:
                    idx.add(j)
                    sub.append(nums[j])
                    bt(idx,sub)
                    idx.remove(j)
                    sub.pop()


        bt(set(),[])
        return res