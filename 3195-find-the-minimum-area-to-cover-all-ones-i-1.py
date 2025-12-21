from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        '''
        We need to find the minimum col and minimum row to cover the '1's.
        What we can do is to collapse the columns into single row, so as long as there's a '1' in any row for that column, we will set the col as '1'
        Next, we collapse the rows into a single column, so as long as there's a '1' in any column for that row, we will set the row as '1'
        Next, based on the single row and single col, we loop through to find the minimum col and minimum row correspondingly by having 2 pointers and reducing them until we hit the first '1'
        Time: O(n.m)
        Space: O(max(n, m))
        '''
        ROWS = len(grid)
        COLS = len(grid[0])
        single_row = [0] * COLS
        single_col = [0] * ROWS
        for i in range(ROWS):
            for j in range(COLS):
                cell = grid[i][j]
                if cell == 1:
                    single_row[j] = 1
                    single_col[i] = 1

        def calculate_min_len(single_list):
            n = len(single_list)
            min_start, min_end = 0, n - 1
            while min_start < n and single_list[min_start] == 0:
                min_start += 1
            while min_end >= 0 and single_list[min_end] == 0:
                min_end -= 1

            return min_end - min_start + 1

        min_col_len = calculate_min_len(single_row)
        min_row_len = calculate_min_len(single_col)

        return min_col_len * min_row_len


sol = Solution()
grid = [[0, 1, 0], [1, 0, 1]]
print(f'output: {sol.minimumArea(grid)}')
