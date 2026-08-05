class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        def per(i,j):
            if (i,j) in visited:
                return 0
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return 1
            if grid[i][j] == 0:
                return 1

            visited.add((i,j))
            return per(i+1,j) + per(i-1,j) + per(i,j+1) + per(i,j-1)
            
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = per(i,j)
                    return ans

        return ans