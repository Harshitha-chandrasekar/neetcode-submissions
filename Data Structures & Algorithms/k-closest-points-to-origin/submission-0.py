class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        squares = []
        for i in points:
            dist = math.sqrt((i[0]*i[0])+(i[1]*i[1]))
            squares.append([dist,i[0],i[1]])

        heapq.heapify(squares)
        output = []
        while k>0:
            dist, x, y = heapq.heappop(squares)
            output.append([x,y])
            k = k-1
        
        return output
