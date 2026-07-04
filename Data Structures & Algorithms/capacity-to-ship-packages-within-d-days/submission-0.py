class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def d(n):
            days = 1
            curr = 0
            for w in weights:
                if curr + w > n:
                    days += 1
                    curr = w
                else:
                    curr += w
                    
            return days

        l = max(weights)
        r = sum(weights)
        ans = r

        while l<=r:
            m = (l+r)//2
            if d(m)<=days:
                ans = m
                r = m-1
            else:
                l = m+1

        return ans