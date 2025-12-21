from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        '''
        We can use backtracking to solve this
        '''
        row_list = [set() for _ in range(9)]
        col_list = [set() for _ in range(9)]
        square_list = [set() for _ in range(9)]

        def get_square_idx(row, col):
            temp = row // 3
            temp2 = col // 3
            return temp * 3 + temp2

        def check_valid(row, col, val):
            square = get_square_idx(row, col)
            if val in row_list[row] or val in col_list[col] or val in square_list[square]:
                return False

            return True

        def populate_lists():
            for row in range(9):
                for col in range(9):
                    val = board[row][col]
                    if val == '.':
                        continue
                    row_list[row].add(val)
                    col_list[col].add(val)
                    square_list[get_square_idx(row, col)].add(val)

        populate_lists()

        def solve():
            # Find all empty cells once
            empty_cells = []
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        empty_cells.append((row, col))

            def backtrack(index):
                if index == len(empty_cells):
                    return True

                row, col = empty_cells[index]
                for i in range(1, 10):
                    val_str = str(i)
                    if check_valid(row, col, val_str):
                        # Place value
                        board[row][col] = val_str
                        row_list[row].add(val_str)
                        col_list[col].add(val_str)
                        square_list[get_square_idx(row, col)].add(val_str)

                        if backtrack(index + 1):
                            return True

                        # Backtrack
                        board[row][col] = '.'
                        row_list[row].remove(val_str)
                        col_list[col].remove(val_str)
                        square_list[get_square_idx(row, col)].remove(val_str)

                return False

            return backtrack(0)

        solve()


sol = Solution()
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
sol.solveSudoku(board)
print(f'output: {board}')
