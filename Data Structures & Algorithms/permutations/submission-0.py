class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        n = len(nums)
        arr = [0]*n

        def p(index, path, arr):
                if index == len(nums):
                    results.append(path.copy())
                    return
                
                for i in range(len(arr)):
                    if arr[i] == 0:
                        arr[i] = 1
                        path.append(nums[i])
                        p(index+1,path,arr)
                        path.pop()
                        arr[i] = 0

        p(0,[],arr)
        return results