from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        '''
        We can break this into sub-problems by checking for cell at (row, col) what's the maxima square that can be created for the cells at (row-1, col), (row, col-1), (row-1, col-1)
        Using dp and cache, we can get the number with the base case as the row == 0 and col == 0
        then we get the minimum of those 3 subproblems, and add 1 to it if my current cell's value is '1'. Otherwise set as 0
        '''
        ROWS = len(matrix)
        COLS = len(matrix[0])
        res = 0
        dp = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    dp[r][c] = matrix[r][c]
                else:
                    if matrix[r][c] == 0:
                        dp[r][c] = 0
                    else:
                        top = dp[r-1][c]
                        left = dp[r][c-1]
                        diagonal = dp[r-1][c-1]
                        dp[r][c] = min(top, left, diagonal) + 1
                res += dp[r][c]
        return res


sol = Solution()
matrix = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]

print(f'output: {sol.countSquares(matrix)}')
