class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(index, path, summ):
            if summ == target:
                result.append(path.copy())
                return
            if summ > target or index == len(candidates):
                return

           
            path.append(candidates[index])
            backtrack(index+1,path,summ + candidates[index])
            path.pop()

            #get to next unique element
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index = index+1

            backtrack(index+1, path, summ)


        backtrack(0,[],0)
        return result