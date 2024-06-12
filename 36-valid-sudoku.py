import collections
from typing import List

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(0, 9):
      for c in range(0, 9):
        val = board[r][c]
        if val == '.':
          continue
        if (val in rows[r] or val in cols[c] or val in squares[(r//3, c//3)]):
          return False
        rows[r].add(val)
        cols[c].add(val)
        squares[(r//3, c//3)].add(val)

    return True
  
sol = Solution()
input = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(f'Input: {input}\nOutput: {sol.isValidSudoku(input)}')