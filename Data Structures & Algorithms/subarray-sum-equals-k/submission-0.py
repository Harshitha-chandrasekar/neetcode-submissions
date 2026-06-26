class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}

        currsum = 0
        res = 0
        for n in nums:
            currsum = currsum+n
            if currsum-k in prefix:
                res = res + prefix[currsum-k]

            if currsum in prefix:
                prefix[currsum] = prefix[currsum]+1
            else:
                prefix[currsum] = 1

        return res
        