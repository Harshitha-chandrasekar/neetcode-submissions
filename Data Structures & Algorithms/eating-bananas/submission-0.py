class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        small = 1
        big = max(piles) # she eats the biggest pile in an hour
        mid = 0
        while small<=big:
            mid = small + ((big-small)//2)
    
            eaten = 0
            for pile in piles:
                eaten = eaten + ((pile + mid - 1) // mid)

            if eaten <= h:
                    big = mid - 1 
            else:
                small = mid + 1

        return small
