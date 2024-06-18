from typing import List
from collections import deque

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
      return 0
    
    ROWS, COLS = len(grid), len(grid[0])
    
    visited = set()
    islands = 0
    
    def bfs(r, c):
      queue = deque()
      cell = (r, c)
      visited.add(cell)
      queue.append(cell)
      
      while queue:
        row, col = queue.popleft()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        for dr, dc in directions:
          r, c = row + dr, col + dc
          cell = (r, c)
          if (r in range(ROWS)
              and c in range(COLS)
              and grid[r][c] == '1'
              and cell not in visited):
            queue.append(cell)
            visited.add(cell)
    
    for r in range(ROWS):
      for c in range(COLS):
        if grid[r][c] == '1' and (r, c) not in visited:
          bfs(r, c)
          islands += 1
          
    return islands
    
sol = Solution()
# grid = [["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]]
grid = [["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]
output = sol.numIslands(grid)
print(f'grid: {grid}\noutput: {output}')