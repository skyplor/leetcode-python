from typing import List
from collections import deque

class Solution:
  def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[int]:
    # '''
    # backtracking
    # maintain set of numbers?
    # store a hashmap of existing numbers that were set and their row & col
    # '''
    # matrix = [[0] * k for _ in range(k)]
    # def backtracking(r, c, val, existing_hash, cur_matrix):
    #   if val > k:
    #     return True
      
    #   # check the rules
    #   for up_cond, down_cond in rowConditions:
    #     if up_cond == val:
    #       # find down_cond and if not set, allow value. if set, then check if we set the value in this cell, does it qualify
    #       if down_cond in existing_hash:
    #         down_value_row, _ = existing_hash[down_cond]
    #         if down_value_row < r:
    #           return False
    #     elif down_cond == val:
    #       if up_cond in existing_hash:
    #         up_value_row, _ = existing_hash[up_cond]
    #         if up_value_row > r:
    #           return False
            
    #   for left_cond, right_cond in colConditions:
    #     if left_cond == val:
    #       # find right_cond and if not set, allow value. if set, then check if we set the value in this cell, does it qualify
    #       if right_cond in existing_hash:
    #         _, right_value_col = existing_hash[right_cond]
    #         if right_value_col < c:
    #           return False
    #     elif right_cond == val:
    #       if left_cond in existing_hash:
    #         _, left_value_col = existing_hash[left_cond]
    #         if left_value_col > c:
    #           return False

    #   existing_hash[val] = (r, c)
    #   cur_matrix[r][c] = val
    #   res = backtracking(r, c+1, val + 1, existing_hash, cur_matrix) or backtracking(r + 1, c, val + 1, existing_hash, cur_matrix)
    #   # cur_matrix[r][c] = 0
    #   return res
    
    
    # res = backtracking(0, 0, 1, {}, matrix)
    # # if no result, return empty matrix
    # # else matrix
    # return matrix if res else []

    '''
    Using topological sort + kahn's algo
    '''
    def topo_sort(edges, n):
      adj = [[] for _ in range(n + 1)]
      deg = [0] * (n + 1)
      order = []
      for x in edges:
        adj[x[0]].append(x[1])
        deg[x[1]] += 1
        
      q = deque()
      for i in range(1, n+1):
        if deg[i] == 0:
          q.append(i)
      while q:
        f = q.popleft()
        order.append(f)
        n -= 1
        for v in adj[f]:
          deg[v] -= 1
          if deg[v] == 0:
            q.append(v)
            
      if n != 0:
        return []
      return order
    order_rows = topo_sort(rowConditions, k)
    order_cols = topo_sort(colConditions, k)
    
    if not order_rows or not order_cols:
      return []
    
    matrix = [[0] * k for _ in range(k)]
    
    for i in range(k):
      for j in range(k):
        if order_rows[i] == order_cols[j]:
          matrix[i][j] = order_rows[i]
          
    return matrix
  
sol = Solution()
k = 3
rowConditions = [[1,2],[3,2]]
colConditions = [[2,1],[3,2]]
print(f'output: {sol.buildMatrix(k, rowConditions, colConditions)}')