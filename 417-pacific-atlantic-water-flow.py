from typing import List

class Solution:
  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    '''
    we will pick a few starting points and start traversing from there
    The starting points will be from the edges of the heights
    We will have 2 visited sets, one for each ocean
    during traversing, we can move to the next adjacent cell (inwards) IF height is >= prevHeight because water can only flow from inside to outside if inside is higher
    after marking the visited and qualified cells for each ocean, we then compare the 2 sets and if a cell exists in both sets, then we add them into result list
    '''
    
    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    def dfs(r, c, visited, prevHeight):
      if (r not in range(ROWS)
          or c not in range(COLS)
          or (r, c) in visited
          or heights[r][c] < prevHeight):
        return
      visited.add((r, c))
      for dr, dc in directions:
        row, col = r + dr, c + dc
        dfs(row, col, visited, heights[r][c])
    
    for c in range(COLS):
      dfs(0, c, pac, heights[0][c])
      dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
    
    for r in range(ROWS):
      dfs(r, 0, pac, heights[r][0])
      dfs(r, COLS - 1, atl, heights[r][COLS - 1])
      
    res = []
    for r in range(ROWS):
      for c in range(COLS):
        cell = (r, c)
        if cell in pac and cell in atl:
          res.append(list(cell))
          
    return res
  
sol = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(f'output: {sol.pacificAtlantic(heights)}')