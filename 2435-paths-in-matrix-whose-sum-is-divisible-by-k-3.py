class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        '''
        We can use a 3D DP for this
        '''
        MOD = 10**9 + 7
        ROWS = len(grid)
        COLS = len(grid[0])
        cache = [[[0] * k for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
        
        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                for remainder in range(k):
                    if row == ROWS - 1 and col == COLS - 1:
                        cache[row][col][remainder] = 1 if (remainder + grid[row][col]) % k == 0 else 0
                        continue
                    new_remainder = (remainder + grid[row][col]) % k
                    cache[row][col][remainder] = (cache[row+1][col][new_remainder] % MOD +
                                          cache[row][col+1][new_remainder] % MOD) % MOD
            
        return cache[0][0][0]

sol = Solution()
print(f'output: {sol.numberOfPaths(grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3)}, expected: 2')
print(f'output: {sol.numberOfPaths(grid = [[0,0]], k = 5)}, expected: 1')
print(f'output: {sol.numberOfPaths(grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1)}, expected: 10')