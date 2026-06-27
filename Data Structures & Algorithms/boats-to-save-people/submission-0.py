class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people)-1
        boats = 0
        while l<=r:
            s = people[l]+people[r]
            if s <= limit:
                l = l+1
                r = r-1
            else:
                r = r-1
            boats = boats+1

        return boats