from functools import cache


class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        '''
        Using DFS and cache, top-down
        NOTE: This will give memory limit exceeded error
        '''
        MOD = 10**9 + 7
        ROWS = len(grid)
        COLS = len(grid[0])

        @cache
        def dfs(row, col, remainder):
            if row == ROWS - 1 and col == COLS - 1:
                remainder += grid[row][col]
                remainder %= k
                return 1 if remainder == 0 else 0
            res = 0
            remainder += grid[row][col]
            remainder %= k
            if row+1 < ROWS:
                res += dfs(row+1, col, remainder)
                res %= MOD
            if col+1 < COLS:
                res += dfs(row, col+1, remainder)
                res %= MOD

            return res

        return dfs(0, 0, 0)


sol = Solution()
print(f'output: {sol.numberOfPaths(grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3)}, expected: 2')
print(f'output: {sol.numberOfPaths(grid = [[0,0]], k = 5)}, expected: 1')
print(f'output: {sol.numberOfPaths(grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1)}, expected: 10')
