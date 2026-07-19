class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heapq.heappush(maxHeap, [count, char])
        s = ""
        while maxHeap:
            count, letter = heapq.heappop(maxHeap)
            if len(s) >= 2 and s[-1] == letter and s[-2] == letter:
                if not maxHeap:
                    return s
                else:
                    c2,l2 = heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap,[count,letter])
                    count,letter = c2,l2
            if count != 0:
                count+=1
                s+=letter

                heapq.heappush(maxHeap,[count,letter])

        return s           