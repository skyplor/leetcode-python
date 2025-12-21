class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        '''
        Using DFS and cache, top-down
        '''
        MOD = 10**9 + 7
        ROWS = len(grid)
        COLS = len(grid[0])

        cache = [[[-1] * k for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(row, col, remainder):
            if row == ROWS - 1 and col == COLS - 1:
                remainder = (remainder + grid[row][col]) % k
                return 1 if remainder == 0 else 0

            if row == ROWS or col == COLS:
                return 0

            if cache[row][col][remainder] > -1:
                return cache[row][col][remainder]
            
            new_remainder = (remainder + grid[row][col]) % k

            cache[row][col][remainder] = (dfs(row+1, col, new_remainder) % MOD +
                                          dfs(row, col+1, new_remainder) % MOD) % MOD

            return cache[row][col][remainder]

        return dfs(0, 0, 0)


sol = Solution()
print(
    f'output: {sol.numberOfPaths(grid=[[5, 2, 4], [3, 0, 5], [0, 7, 2]], k=3)}, expected: 2')
print(f'output: {sol.numberOfPaths(grid=[[0, 0]], k=5)}, expected: 1')
print(
    f'output: {sol.numberOfPaths(grid=[[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], k=1)}, expected: 10')
