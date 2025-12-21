from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        '''
        We will need a way to know whether we are at the bottom-left triangle or top-right triangle
        diagonal (0,0), (1,1)... are part of bottom-left
        For each diagonal, we get all the values, sort them, then populate the values.

        To get all available diagonals
            1. we will loop through all ROWS (0 to n-1) for col = 0. The cells will be the starting cell of each bottom-left diagonal
            2. next, we loop through all COLS (1 to n-1) for row = 0. The cells will be the starting cell of each top-right diagonal

        Next cell of each diagonal has delta: (1, 1)

        Time: O(n² log n)
        Space: O(n)
        '''

        n = len(grid)

        def sort_diagonal(start_row: int, start_col: int, decreasing: bool) -> None:
            temp = []
            row, col = start_row, start_col
            while row < n and col < n:
                temp.append(grid[row][col])
                row, col = row + 1, col + 1

            temp.sort(reverse=decreasing)
            row, col = start_row, start_col
            for val in temp:
                grid[row][col] = val
                row, col = row + 1, col + 1

        for row in range(n):
            sort_diagonal(row, 0, True)
        for col in range(1, n):
            sort_diagonal(0, col, False)

        return grid

sol = Solution()
grid = [[1, 7, 3], [9, 8, 2], [4, 5, 6]]
print(f'output: {sol.sortMatrix(grid)}')
