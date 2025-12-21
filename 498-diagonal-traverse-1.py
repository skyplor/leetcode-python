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
        UP_DIRECTION = 1
        DOWN_DIRECTION = -1
        NEXT_INBOUNDARY_CELL = [-1, 1]
        NEXT_OUTBOUNDARY_CELL = [[0, 1], [1, 0]]
        res = []

        ROWS = len(mat)
        COLS = len(mat[0])

        def get_next_cell(i, j, delta_i, delta_j) -> List[int]:
            next_i, next_j = delta_i + i, delta_j + j
            if next_i not in range(ROWS) or next_j not in range(COLS):
                return [-1, -1]
            return [next_i, next_j]

        current_direction = UP_DIRECTION

        i, j = 0, 0
        counter = 0
        while counter < ROWS * COLS:
            counter += 1
            cell_val = mat[i][j]
            res.append(cell_val)

            # next cell (update i and j)
            delta_i, delta_j = NEXT_INBOUNDARY_CELL
            next_i, next_j = get_next_cell(
                i, j, current_direction * delta_i, current_direction * delta_j)
            if next_i == -1 or next_j == -1:
                if current_direction == UP_DIRECTION:
                    delta_i, delta_j = NEXT_OUTBOUNDARY_CELL[0]
                    next_i, next_j = get_next_cell(i, j, delta_i, delta_j)
                    if next_i == -1 or next_j == -1:
                        delta_i, delta_j = NEXT_OUTBOUNDARY_CELL[1]
                        next_i, next_j = get_next_cell(i, j, delta_i, delta_j)
                else:
                    delta_i, delta_j = NEXT_OUTBOUNDARY_CELL[1]
                    next_i, next_j = get_next_cell(i, j, delta_i, delta_j)
                    if next_i == -1 or next_j == -1:
                        delta_i, delta_j = NEXT_OUTBOUNDARY_CELL[0]
                        next_i, next_j = get_next_cell(i, j, delta_i, delta_j)

                current_direction *= DOWN_DIRECTION

            if next_i == -1 or next_j == -1:
                break

            i, j = next_i, next_j

        return res


sol = Solution()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'output: {sol.findDiagonalOrder(mat)}')
mat = [[1, 2], [3, 4]]
print(f'output: {sol.findDiagonalOrder(mat)}')
