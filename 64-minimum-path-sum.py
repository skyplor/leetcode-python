class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        '''
        We can use a dp for this to store the least sum from a cell to the bottom right cell
        We initialize the bottom right cell to the grid's value
        we also initialise all the edges of m-1 and n-1
        '''
        ROWS = len(grid)
        COLS = len(grid[0])
        dp = [[-1] * COLS for _ in range(ROWS)]
        dp[ROWS - 1][COLS - 1] = grid[ROWS - 1][COLS - 1]
        for r in range(ROWS - 2, -1, -1):
            dp[r][COLS - 1] = dp[r + 1][COLS - 1] + grid[r][COLS - 1]
        for c in range(COLS - 2, -1, -1):
            dp[ROWS - 1][c] = dp[ROWS - 1][c + 1] + grid[ROWS - 1][c]

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if dp[r][c] != -1:
                    continue
                dp[r][c] = min(dp[r+1][c], dp[r][c+1]) + grid[r][c]

        return dp[0][0]


sol = Solution()
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
# grid = input('Hello, please enter the grid: ')
output = sol.minPathSum(grid)
print(f'output: {output}')
