class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        inf = 2147483647
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r,c):
            q = deque([(r,c)])
            visit = [[False for _ in range(cols)] for _ in range(rows)]

            visit[r][c] = True
            dist = 0
            while q:
                for i in range(len(q)):
                    row,col = q.popleft()
                    if grid[row][col] == 0:
                        return dist
                    for dr,dc in directions:
                        nr, nc = row +dr, col + dc
                        if (nr>= 0 and nr < rows and nc>=0 and nc<cols and not visit[nr][nc] and grid[nr][nc] != -1):
                            visit[nr][nc] = True
                            q.append((nr,nc))
                dist = dist + 1
            return inf

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == inf:
                    grid[r][c] = bfs(r,c)