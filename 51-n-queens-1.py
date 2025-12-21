from typing import List

class Solution:
  def solveNQueens(self, n: int) -> List[List[str]]:
    '''
    Using backtracking, each iteration, we check if this new position is available
    available = does not hit any other queen (top)
    '''
    res = []
    cols = set()
    posDiags = set() # left to right, line increases, all r+c are equal (1, 0) and (0, 1) belong to same positive diagonal. (2, 0), (1, 1), (0, 2) belong to same positive diagonal
    negDiags = set() # left to right, line decreases, all r-c are equal (0, 0) and (1, 1), (2, 2) belong to same negative diagonal. (0, 1), (1, 2), (2, 3) belong to same negative diagonal
    board = [['.'] * n for _ in range(n)]
    
    def backtrack(row):
      if row == n:
        res.append(["".join(row) for row in board])
        return
      for col in range(n):
        if col in cols or (row - col) in negDiags or (row + col) in posDiags:
          continue

        cols.add(col)
        posDiags.add(row + col)
        negDiags.add(row - col)
        board[row][col] = 'Q'
        backtrack(row + 1)

        cols.remove(col)
        posDiags.remove(row + col)
        negDiags.remove(row - col)
        board[row][col] = '.'
        
    backtrack(0)
    return res
sol = Solution()
n = 4
output = sol.solveNQueens(n)
print(f'n: {n}\noutput: {output}')