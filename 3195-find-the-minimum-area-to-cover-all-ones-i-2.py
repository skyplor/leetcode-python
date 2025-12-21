from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        '''
        We need to find the minimum col, maximum col, minimum row and maximum row to cover the '1's.
        We iterate through each cell, so as long as there's a '1', we update all the 4 values using min and max
        Next, we just need to calculate the result by this formula: (max_col - min_col + 1) * (max_row - min_row + 1)
        Time: O(n.m)
        Space: O(1)
        
        NOTE: This will be slower as we need to do more work of comparing min, max in each iteration of the cell
        '''
        ROWS = len(grid)
        COLS = len(grid[0])

        min_col = float('inf')
        max_col = -1
        min_row = float('inf')
        max_row = -1
        for i in range(ROWS):
            for j in range(COLS):
                cell = grid[i][j]
                if cell == 1:
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)

        return (max_col - min_col + 1) * (max_row - min_row + 1)


sol = Solution()
grid = [[0, 1, 0], [1, 0, 1]]
print(f'output: {sol.minimumArea(grid)}')
