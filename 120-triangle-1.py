class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        '''
        We can use 2D DP for this
        We can go from bottom-up, from left to right
        for the bottom most layer, the minimum will be those values themselves.
        Next layer up, we can then get the minimum of row+1 and column i and column i+1
        '''
        ROWS = COLS = len(triangle)
        
        dp = [[float('inf')] * ROWS for _ in range(COLS)]
        for col in range(COLS):
            dp[ROWS - 1][col] = triangle[ROWS - 1][col]
        
        for i in range(ROWS - 2, -1, -1):
            for j in range(i+1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        
        return dp[0][0]


sol = Solution()
print(
    f'output: {sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])}, expected: 11')
