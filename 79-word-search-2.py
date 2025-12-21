from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        Visited set
        reset for each iteration
        DFS, recursion, backtracking
        for loop that go through each cell as the starting character
        if cell matches the starting character, we proceed to neighbours, and add 1 to the index
        if index >= len(word) then we have found the word and can return true
        using the word[index], get the character and match it against the current board[i][j]
        we also need to ensure i and j are within the range of the board
        '''
        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def backtracking(i: int, j: int, idx: int, visited: set) -> bool:
            if (
                i not in range(ROWS)
                or j not in range(COLS)
                or (i, j) in visited
                or board[i][j] != word[idx]
            ):
                return False

            if idx == len(word) - 1:
                return True

            visited.add((i, j))

            for dr, dc in DIRECTIONS:
                new_row, new_col = dr + i, dc + j
                if backtracking(
                        new_row, new_col, idx + 1, visited):
                    return True

            visited.remove((i, j))

            return False

        for i in range(ROWS):
            for j in range(COLS):
                if backtracking(i, j, 0, set()):
                    return True

        return False


sol = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = 'ABCCED'
word = 'ABBBB'
print(f'output: {sol.exist(board, word)}')
