class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))

        while q:
            r,c = q.popleft()

            for rr,cc in directions:
                nr,nc = r+rr,c+cc

                if nr not in range(rows) or nc not in range(cols) or grid[nr][nc]!=2147483647:
                    continue

                grid[nr][nc] = grid[r][c] +1
                q.append((nr,nc))