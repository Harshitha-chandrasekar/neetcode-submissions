class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph ={i:[] for i in range(n)}
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                graph[i].append([dist,j])
                graph[j].append([dist,i])


        res = 0
        visited = set()
        heap = [[0,0]]
        while len(visited) < n:
            cost, i = heapq.heappop(heap)
            if i in visited:
                continue
            res = res +cost
            visited.add(i)
            for newc, newi in graph[i]:
                if newi not in visited:
                    heapq.heappush(heap,[newc,newi])

        return res