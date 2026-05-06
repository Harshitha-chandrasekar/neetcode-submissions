class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        time = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh = fresh+1
                elif grid[i][j] == 2:
                    q.append((i,j))

        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while fresh>0 and q:
            l = len(q)
            for i in range(l):
                row,col = q.popleft()
                for dr,dc in directions:
                    nr,nc = row+dr,col+dc
                    if (nr>=0 and nr<rows and nc>=0 and nc<cols):
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh = fresh-1
                            q.append((nr,nc))
            
            time = time + 1

        return time if fresh == 0 else -1
