from typing import List
from collections import deque, defaultdict

class Solution:
  def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    # using bfs and queue
    # loop through each cell and add all gates to the queue
    # we will also need to store visited state for each cell
    # then we pop all the cells from the queue and get the distance from gate to that cell
    ROWS, COLS = len(grid), len(grid[0])
    visited = set()
    queue = deque()
    
    def addCell(r, c):
      cell = (r, c)
      if (r not in range(ROWS)
          or c not in range(COLS)
          or cell in visited
          or grid[r][c] == -1):
        return

      visited.add(cell)
      queue.append(cell)
    
    def bfs(r, c):
      dist = 0
      while queue:
        for _ in range(len(queue)):
          row, col = queue.popleft()
          grid[row][col] = min(grid[row][col], dist)
          directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
          for dr, dc in directions:
            r, c = row + dr, col + dc
            addCell(r, c)

        dist += 1
    
    for r in range(ROWS):
      for c in range(COLS):
        if grid[r][c] == 0:
          cell = (r, c)
          visited.add(cell)
          queue.append(cell)
          
    bfs(r, c)

sol = Solution()
grid = [[2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]]
print(f'grid: {grid}')
sol.islandsAndTreasure(grid)
print(f'grid: {grid}')