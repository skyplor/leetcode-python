from typing import List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        We can use BFS for this.
        First, using BFS, we check for each cell that is at the boundary as well as all adjacent neighbours of the cell and if they are 'O', we mark all of them as a temporary letter e.g 'T'
        Next, we go through each cell and if it's 'T', we mark as 'O', if it's 'O', we mark as 'X'
        '''
        TMP = 'T'
        n = len(board)
        m = len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(row, col):
            queue = deque([(row, col)])
            board[row][col] = TMP
            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    new_row, new_col = r + dr, c + dc
                    if new_row in range(n) and new_col in range(m) and board[new_row][new_col] == 'O':
                        board[new_row][new_col] = TMP
                        queue.append((new_row, new_col))

        for i in range(n):
            if board[i][0] == 'O':
                bfs(i, 0)
            if board[i][m-1] == 'O':
                bfs(i, m-1)
        for j in range(m):
            if board[0][j] == 'O':
                bfs(0, j)
            if board[n-1][j] == 'O':
                bfs(n-1, j)
            
        for i in range(n):
            for j in range(m):
                if board[i][j] == TMP:
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


sol = Solution()
board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
         ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
sol.solve(board)
print(f'output: {board}')
board = [["O", "X", "X", "O", "X"], ["X", "O", "O", "X", "O"], [
    "X", "O", "X", "O", "X"], ["O", "X", "O", "O", "O"], ["X", "X", "O", "X", "O"]]
sol.solve(board)
print(f'output: {board}')
board = [["O", "X", "O", "O", "X", "X"], ["O", "X", "X", "X", "O", "X"], ["X", "O", "O", "X", "O", "O"], [
    "X", "O", "X", "X", "X", "X"], ["O", "O", "X", "O", "X", "X"], ["X", "X", "O", "O", "O", "O"]]
sol.solve(board)
print(f'output: {board}')
