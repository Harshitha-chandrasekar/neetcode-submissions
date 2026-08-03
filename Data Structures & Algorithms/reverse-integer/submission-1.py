class Solution:
    def reverse(self, x: int) -> int:
        
        n = abs(x)
        rev = 0
        while n>0:
            rev = rev*10 + n%10
            n = n//10
        if rev>=math.pow(2,31)-1 or rev<-1*math.pow(2,31):
            return 0
        if x<0:
            return -1*rev
        else:
            return rev