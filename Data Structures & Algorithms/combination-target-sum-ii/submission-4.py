class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def bt(i,s,sub):
            if s == target:
                res.append(sub.copy())
                return

            for j in range(i,len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if s+candidates[j]>target:
                    return

                sub.append(candidates[j])
                bt(j+1,s+candidates[j],sub)
                sub.pop()


        bt(0,0,[])
        return res