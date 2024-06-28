from typing import List

class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])
    DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    def backtracking(visited, i, r, c):
      if ((r,c) in visited
          or not r in range(ROWS)
          or not c in range(COLS)
          or not i in range(len(word))
          or board[r][c] != word[i]):
        return False

      if i == len(word) - 1:
        return True

      visited.add((r,c))
      backtrackingResult = []
      for dr, dc in DIRECTIONS:
        row, col = r + dr, c + dc
        backtrackingResult.append(backtracking(visited, i + 1, row, col))

      visited.remove((r,c))
      return any(backtrackingResult)
      
    for r in range(ROWS):
      for c in range(COLS):
        visited = set()
        res = backtracking(visited, 0, r, c)
        if res:
          return True
    
    return False
  
sol = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = 'ABCCED'
word = 'SEE'
print(f'output: {sol.exist(board, word)}')