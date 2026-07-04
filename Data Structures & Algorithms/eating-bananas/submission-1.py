class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def hrs(n):
            s = 0
            for i in piles:
                s = s + math.ceil(i/n)
            return s

        l = 1
        r = max(piles)
        ans = r
        while l<=r:
            m = (l+r)//2
            if hrs(m) <= h :
                ans =  m
                r = m-1
            elif hrs(m)>h:
                l = m+1

        return ans