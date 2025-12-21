from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        '''
        We will use a variable to store the current traverse direction
        In each traversal
            - if it's up direction, we move to cell [-1, 1]
            - else we move to cell [1, -1]
            - if we hit the boundary, then we need to reverse the direction. based on the prev direction, we then need to know which cell is the next cell
                - if up, we will first move to the cell on the right of the last cell. if that is out of boundary, we then move down
                - else, we first move to the cell directly below. If that is out of boundary, then we move to the right
        '''
        res = []

        ROWS = len(mat)
        COLS = len(mat[0])
        going_up = True
        cur_row, cur_col = 0, 0

        for _ in range(ROWS*COLS):
            res.append(mat[cur_row][cur_col])

            # next cell (update cur_row and cur_col)
            if going_up:
                if cur_row > 0 and cur_col < COLS - 1:
                    cur_row, cur_col = cur_row - 1, cur_col + 1
                elif cur_col < COLS - 1:
                    cur_col += 1
                    going_up = False
                else:
                    cur_row += 1
                    going_up = False
            else:
                if cur_row < ROWS - 1 and cur_col > 0:
                    cur_row, cur_col = cur_row + 1, cur_col - 1
                elif cur_row < ROWS - 1:
                    cur_row += 1
                    going_up = True
                else:
                    cur_col += 1
                    going_up = True

        return res


sol = Solution()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'output: {sol.findDiagonalOrder(mat)}')
mat = [[1, 2], [3, 4]]
print(f'output: {sol.findDiagonalOrder(mat)}')
