from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        We can use Union-find for this.
        We will include a dummy cell (-1, -1) to act as the parent for all cells with "O" that is at the boundary.
        So if an internal cell is "O" and is connected to a boundary cell, its parent will ultimately become (-1, -1) as well.
        We will then have a loop that goes through each cell, and if cell has value "O", then we check through all 4 adjacent cells for "O". If exist, union them together
        At the end, we go through each cell again and use the `find` function to get the parent of the cell. If cell is "O" and parent is NOT (-1, -1), this means the cell is an internal cell and can be converted to "X"
        '''
        parents = {}
        score = {}
        n = len(board)
        m = len(board[0])
        dummy = (-1, -1)
        parents[dummy] = dummy
        score[dummy] = 1
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i == 0 or i == n-1 or j == 0 or j == m-1):
                    parents[(i, j)] = dummy
                else:
                    parents[(i, j)] = (i, j)
                score[(i, j)] = 1

        def find(row: int, col: int) -> tuple[int, int]:
            cell = (row, col)
            while parents[cell] != cell:
                parents[cell] = parents[parents[cell]]
                cell = parents[cell]

            return cell

        def union(r1: int, c1: int, r2: int, c2: int):
            p1, p2 = find(r1, c1), find(r2, c2)
            if p1 == p2:
                return

            if p1 == dummy:
                parents[p2] = p1
                score[p1] += score[p2]
            elif p2 == dummy:
                parents[p1] = p2
                score[p2] += score[p1]
            elif score[p1] < score[p2]:
                parents[p1] = p2
                score[p2] += score[p1]
            else:
                parents[p2] = p1
                score[p1] += score[p2]

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    for dr, dc in directions:
                        new_row, new_col = i + dr, j + dc
                        if new_row in range(n) and new_col in range(m) and board[new_row][new_col] == "O":
                            union(i, j, new_row, new_col)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and find(i, j) != dummy:
                    board[i][j] = "X"


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
