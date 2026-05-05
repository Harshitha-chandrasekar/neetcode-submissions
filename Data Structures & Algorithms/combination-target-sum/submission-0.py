class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def backtrack(index,path,total):
            if total == target:
                result.append(path.copy())
                return
            if total > target or index == len(nums):
                return

            #with current number
            path.append(nums[index])
            backtrack(index,path,total+nums[index])
            #without current number
            path.pop()
            backtrack(index+1,path,total)

        backtrack(0,[],0)

        return result