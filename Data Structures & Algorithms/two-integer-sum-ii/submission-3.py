class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        
        def check(l,r):
            s = numbers[l]+numbers[r]
            if s == target:
                return [l+1,r+1]
            elif s<target:
                return check(l+1,r)
            else:
                return check(l,r-1)

        return check(l,r)