class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = [math.sqrt((x1 - 0)**2 + (y1 - 0)**2) for [x1,y1] in points]
        dist = []
        for i in range(len(d)):
            dist.append([d[i],points[i]])
        ans = []
        heapq.heapify(dist)
        while k>0:
            d,poi = heapq.heappop(dist)
            ans.append(poi)
            k-=1

        return ans