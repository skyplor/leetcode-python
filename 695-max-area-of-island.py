from typing import List
from collections import deque

class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    # max_area
    # visited set to maintain the visited state of each cell
    # have 2 loops, ROWS and COLS to go through each cell
    # bfs, return if cell is out of bound (outside of ROWS and COLS) or already visited or has a 0 as value
    # otherwise,
    # add this cell to visited set, add this cell into queue, increment the area by 1, set max_area if current area is higher
    # while queue isn't empty, we retrieve the cell from queue, add all surrounding cells that qualifies into queue
    max_area = 0
    visited = set()
    ROWS, COLS = len(grid), len(grid[0])
    
    def bfs(r, c):
      nonlocal max_area

      queue = deque()
      cell = (r, c)
      visited.add(cell)
      queue.append(cell)
      current_area = 1
      max_area = max(max_area, current_area)

      while queue:
        row, col = queue.popleft()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
          r = row + dr
          c = col + dc
          cell = (r, c)
          if (r not in range(ROWS)
              or c not in range(COLS)
              or cell in visited
              or not grid[r][c]):
            continue
          visited.add(cell)
          queue.append(cell)
          current_area += 1
          max_area = max(max_area, current_area)

    for r in range(ROWS):
      for c in range(COLS):
        
        if ((r, c) not in visited
          and grid[r][c]):
          bfs(r, c)

    return max_area
    
sol = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
output = sol.maxAreaOfIsland(grid)
print(f'grid: {grid}\noutput: {output}')