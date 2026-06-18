class Solution:
    def hammingWeight(self, n: int) -> int:
        bb = bin(n)[2:]
        count = 0
        for i in bb:
            if i == '1':
                count = count+1
        return count
