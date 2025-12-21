import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        We will have 3 lists (col, row, square), each list will have 9 sets. Each set represent the values filled for that index.
        Each time we process a cell, we check if the value exists in the col index, row index and square index. if yes, return False. If no, add into each of those index sets.

        To determine which square a cell belongs to:
        0: (0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)
        1: (0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4),(2,5)
        2: (0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)
        3: (3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)
        '''
        col_list = [set() for _ in range(9)]
        row_list = [set() for _ in range(9)]
        square_list = [set() for _ in range(9)]

        def get_square_idx(row, col):
            temp = row // 3
            temp2 = col // 3
            return temp * 3 + temp2

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue

                square = get_square_idx(row, col)
                if val in row_list[row] or val in col_list[col] or val in square_list[square]:
                    return False
                row_list[row].add(val)
                col_list[col].add(val)
                square_list[square].add(val)

        return True


sol = Solution()
input = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(f'Input: {input}\nOutput: {sol.isValidSudoku(input)}')
