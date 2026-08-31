class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        COLS = len(obstacleGrid[0])
        ROWS = len(obstacleGrid)

        dp = [[0]*(COLS) for _ in range(ROWS)]

        for i in range(ROWS):
            if obstacleGrid[i][0] == 1:
                for k in range(i, ROWS):
                    dp[k][0] = -1
                break
            else:
                dp[i][0] = 1
        for i in range(COLS):
            if obstacleGrid[0][i] == 1:
                for k in range(i, COLS):
                    dp[0][k] = -1
                break
            else:
                dp[0][i] = 1

        for i in range(1,ROWS):
            for j in range(1,COLS):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = -1
                    continue
                if dp[i-1][j] == -1 and dp[i][j-1] == -1:
                    dp[i][j] = -1
                elif dp[i-1][j] == -1 or dp[i][j-1] == -1:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[ROWS-1][COLS-1] if dp[ROWS-1][COLS-1] != -1 else 0