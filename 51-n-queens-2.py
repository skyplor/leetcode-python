from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        One queen per row, so we will have a loop that go through each row
        For each row, we will have n different ways to place the queen (1 for each col)
        we need to keep track of which cells are taken up. Because each queen will cover a number of cells
        so we need to keep track of the following:
            - col
            - positive diagonal
            - negative diagonal

        Positive diagonal: cells where from bottom-left of queen to top-right of queen e.g if queen is placed at (3, 3), then positive diagonals: (5, 1), (4, 2), (2, 4), (1, 5)
        Negative diagonal: cells where from top-left of queen to bottom-right of queen e.g if queen is placed at (3, 3), then negative diagonals: (1, 1), (2, 2), (4, 4), (5, 5)

        So positive diagonals = (r + c), negative diagonals = (r - c)

        We can use backtracking way to find ALL possible solutions
        We will only need to call it once at the first row since we must have at least 1 queen in the first row so it would have considered ALL possibilities for each col of the first row
        '''

        board = [['.'] * n for _ in range(n)]
        col = set()
        posDiag = set()
        negDiag = set()
        res = []

        def backtracking(r):
            if r == n:
                copy = [''.join(board[row]) for row in range(n)]
                res.append(copy)
                return

            for c in range(n):
                if (c in col
                    or (r + c) in posDiag
                        or (r - c) in negDiag):
                    continue

                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = 'Q'

                backtracking(r+1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = '.'

        backtracking(0)

        return res


sol = Solution()
n = 4
output = sol.solveNQueens(n)
print(f'n: {n}\noutput: {output}')
