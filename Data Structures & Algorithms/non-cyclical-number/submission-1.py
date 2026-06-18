class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        summ = 0
        while summ not in seen:
            while n>0:
                summ = summ + math.pow(n%10,2)
                n = n//10
            if summ == 1:
                return True
            if summ in seen:
                return False
            seen.append(summ)
            n = summ
            summ = 0

        return False
        
        