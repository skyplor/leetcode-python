from typing import List

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])
    top, bottom = 0, ROWS - 1
    while top <= bottom:
      row = top + (bottom - top) // 2
      if target > matrix[row][-1]:
        top = row + 1
      elif target < matrix[row][0]:
        bottom = row - 1
      else:
        break

    if not (top <= bottom):
      return False

    row = (top + bottom) // 2
    left, right = 0, COLS - 1

    while left <= right:
      m = left + (right - left) // 2
      if target == matrix[row][m]:
        return True
      elif target < matrix[row][m]:
        right = m - 1
      else:
        left = m + 1

    return False

sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
output = sol.searchMatrix(matrix, target)
print(f'matrix: {matrix}\ntarget: {target}\noutput: {output}')