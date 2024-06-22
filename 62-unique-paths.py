class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    # grid[2][5] or grid[1][6] = 1
    # grid[m-1][n-2] = 1, grid[m-2][n-1] = 1
    # once we hit col boundary, all grid[0][n-1], grid[1][n-1]... = 1
    # once we hit row boundary, all grid[m-1][0], grid[m-1][0]... = 1
    # when we didn't hit boundary, there are 2 choices, either move right or move down
    dp = [[0] * (n+1) for _ in range(m+1)]
    dp[m-1][n-1] = 1

    for row in range(m - 1, -1, -1):
      for col in range(n - 1, -1, -1):
        if row == m-1 and col == n-1:
          continue
        dp[row][col] = dp[row+1][col] + dp[row][col + 1]

    return dp[0][0]

sol = Solution()
m = 3
n = 7
output = sol.uniquePaths(m, n)
print(f'output: {output}')