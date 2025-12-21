from typing import List


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        '''
        We will need to take note to only have at most 1 90deg clockwise turn for each path
        We will need to check the maximum length we would have gotten from sub-paths (with turn and without turn)
        For each sub-child, we need to pass the current value and only consider the child IF the child has the value in the next sequence (2: 0, 0: 2)
        We will need to go through each cell and consider the cell as the starting cell if it is a '1'
            - We will then need to consider all 4 diagonal cells
        '''
        ROWS = len(grid)
        COLS = len(grid[0])
        NEXT_CHILD = {1: 2, 2: 0, 0: 2}
        DIRECTIONS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        NEXT_ROTATED_DIRECTION = {(-1, -1): (-1, 1),
                                  (-1, 1): (1, 1),
                                  (1, 1): (1, -1),
                                  (1, -1): (-1, -1)}

        def get_next_cell(row: int, col: int, rotate: bool, direction: tuple[int, int]) -> tuple[int, int, tuple[int, int]]:
            dr, dc = direction
            if not rotate:
                return row + dr, col + dc, direction

            '''
            Cases:
                (-1, -1): (-1, 1)
                (-1, 1): (1, 1)
                (1, 1): (1, -1)
                (1, -1): (-1, -1)
            '''
            next_rotated_dr, next_rotated_dc = NEXT_ROTATED_DIRECTION[direction]
            return row + next_rotated_dr, col + next_rotated_dc, (next_rotated_dr, next_rotated_dc)

        def get_max_length(row: int, col: int, can_turn: bool, required_val: int, direction: tuple[int, int]) -> int:
            if row not in range(ROWS) or col not in range(COLS) or grid[row][col] != required_val:
                return 0

            child_len_after_turn = 0
            next_required_val = NEXT_CHILD[required_val]
            if can_turn:
                next_rotated_row, next_rotated_col, next_direction = get_next_cell(row, col, True, direction)
                child_len_after_turn = get_max_length(next_rotated_row, next_rotated_col, False, next_required_val, next_direction)
            next_row, next_col, next_direction = get_next_cell(row, col, False, direction)
            child_len_without_turn = get_max_length(next_row, next_col, True, next_required_val, next_direction)
            return max(child_len_after_turn, child_len_without_turn) + 1

        max_length = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    for dr, dc in DIRECTIONS:
                        max_length = max(
                            max_length, get_max_length(i+dr, j+dc, True, NEXT_CHILD[1], (dr, dc))+1)

        return max_length


sol = Solution()
grid = [[2, 2, 1, 2, 2], [2, 0, 2, 2, 0], [2, 0, 1, 1, 0], [1, 0, 2, 2, 2], [2, 0, 0, 2, 2]]
print(f'output: {sol.lenOfVDiagonal(grid)}, expected: 5')
grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
print(f'output: {sol.lenOfVDiagonal(grid)}, expected: 4')
grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
print(f'output: {sol.lenOfVDiagonal(grid)}, expected: 5')
grid = [[1]]
print(f'output: {sol.lenOfVDiagonal(grid)}, expected: 1')
