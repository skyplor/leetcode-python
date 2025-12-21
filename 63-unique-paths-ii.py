class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        '''
        The number of paths for each cell will depend on the next cell on the right and the next cell below. It will also depend on whether there's an obstacle on this cell
        We will use a dp 2-d hash to store all the unique paths
        We will initialise the cell at [m-1][n-1] to be 1
        '''
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        dp[ROWS - 1][COLS - 1] = 1

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                    continue

                if r < ROWS - 1 and c < COLS - 1:
                    dp[r][c] = dp[r][c + 1] + dp[r + 1][c]
                    continue
                if r == ROWS - 1 and c < COLS - 1:
                    dp[r][c] += dp[r][c + 1]
                elif c == COLS - 1 and r < ROWS - 1:
                    dp[r][c] += dp[r + 1][c]

        print(dp)

        return dp[0][0]


sol = Solution()
# obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
obstacleGrid = [[0,1],[0,0]]
# obstacleGrid = [[0, 0], [0, 1]]
output = sol.uniquePathsWithObstacles(obstacleGrid)
print(f'output: {output}')
