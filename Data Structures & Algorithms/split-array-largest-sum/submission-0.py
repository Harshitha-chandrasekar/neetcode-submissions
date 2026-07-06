class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        res = r

        while l<=r:
            m = (l+r)//2
            curr_sum = 0 
            splits = 1
            max_sum = 0
            for n in nums:
                if curr_sum+n>m:
                    splits+=1
                    max_sum = max(max_sum,curr_sum)
                    curr_sum = n
                else:
                    curr_sum+=n
            if splits>k:
                l = m+1
            else:
                r = m-1
                res = m

        return res