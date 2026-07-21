class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(i,subset):
            nonlocal res
            res.append(subset.copy())

            for j in range(i,len(nums)):
                subset.append(nums[j])
                bt(j+1,subset)
                subset.pop()

        bt(0,[])
        return res