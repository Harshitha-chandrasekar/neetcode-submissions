class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        minheap = [[0,0,0]] #diff,r,c
        visited = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while minheap:
            diff, r, c = heapq.heappop(minheap)
            if (r,c) in visited:
                continue

            visited.add((r,c))
            if (r,c) == (rows-1,cols-1):
                return diff

            for dr,dc in directions:
                nr,nc = r+dr,c+dc

                if nr < 0 or nc < 0 or nr==rows or nc==cols or (nr,nc) in visited:
                    continue
                else:
                    newdiff = max(diff,abs(heights[r][c]-heights[nr][nc]))
                    heapq.heappush(minheap,[newdiff,nr,nc])
            