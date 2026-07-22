class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        res = []

        def bt(i,sub):
            if len(sub) == k:
                res.append(sub.copy())
                return
                

            for j in range(i,len(nums)):
                sub.append(nums[j])
                bt(j+1,sub)
                sub.pop()

        bt(0,[])
        return res