from typing import List
from collections import deque

class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    '''
    BFS - put all currently rotting oranges into queue
    while queue is not empty, we pop all from the queue and process them.
    Process: mark each of the oranges that are fresh(1) at the top,left,right,bottom as visited and rotten, then add them into the queue
    '''
    queue = deque()
    visited = set()
    ROWS, COLS = len(grid), len(grid[0])
    res = 0
    fresh = 0

    for r in range(ROWS):
      for c in range(COLS):
        if grid[r][c] == 1:
          fresh += 1
        elif grid[r][c] == 2:
          queue.append((r, c))
          
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while fresh > 0 and queue:
      res += 1
      for _ in range(len(queue)):
        row, col = queue.popleft()
        for dr, dc in directions:
          r, c = row + dr, col + dc
          if (r not in range(ROWS)
              or c not in range(COLS)
              or (r, c) in visited
              or not grid[r][c] == 1):
            continue
          
          grid[r][c] = 2
          visited.add((r, c))
          queue.append((r, c))
          fresh -= 1
          
    return res if fresh == 0 else -1
  
sol = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(f'output: {sol.orangesRotting(grid)}')