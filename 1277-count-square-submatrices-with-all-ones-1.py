from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        '''
        We can break this into sub-problems by checking for cell at (row, col) what's the maxima square that can be created for the cells at (row+1, col), (row, col+1), (row+1, col+1)
        Using recursion + cache, we can get the number with the base case as 0
        then we get the minimum of those 3 subproblems, and add 1 to it if my current cell's value is '1'. Otherwise just return the min
        '''
        ROWS = len(matrix)
        COLS = len(matrix[0])
        res = 0
        dp = [[-1] * COLS for _ in range(ROWS)]

        def recursion(row, col) -> int:
            nonlocal res
            if row >= ROWS or col >= COLS or matrix[row][col] == 0:
                return 0

            if dp[row][col] != -1:
                return dp[row][col]

            right = recursion(row, col+1)
            down = recursion(row+1, col)
            diagonal = recursion(row+1, col+1)
            maxima_square = min(right, down, diagonal) + 1

            dp[row][col] = maxima_square
            res += maxima_square
            return maxima_square

        for r in range(ROWS):
            for c in range(COLS):
                recursion(r, c)
        return res


sol = Solution()
matrix = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]

print(f'output: {sol.countSquares(matrix)}')
