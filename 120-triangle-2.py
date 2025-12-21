class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        '''
        Improving from the previous solution, we now modify the solution to use only O(n) space where n is total number of rows
        '''
        ROWS = COLS = len(triangle)
        
        dp = [float('inf')] * COLS
        for i in range(COLS):
            dp[i] = triangle[ROWS - 1][i]
        
        for i in range(ROWS - 2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        
        return dp[0]


sol = Solution()
print(
    f'output: {sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])}, expected: 11')
