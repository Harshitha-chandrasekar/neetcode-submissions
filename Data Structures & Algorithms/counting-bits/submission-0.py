class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for number in range(n+1):
            count = 0
            while number>0:
                number = number&(number-1)
                count = count+1
            ans.append(count)
        return ans