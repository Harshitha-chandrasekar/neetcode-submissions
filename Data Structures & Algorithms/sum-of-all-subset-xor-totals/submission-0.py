class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def bt(i,subset):
            nonlocal res
            xorr = 0
            for num in subset:
                xorr^=num
            res+=xorr

            for j in range(i,len(nums)):
                subset.append(nums[j])
                bt(j+1,subset)
                subset.pop()

        bt(0,[])
        return res