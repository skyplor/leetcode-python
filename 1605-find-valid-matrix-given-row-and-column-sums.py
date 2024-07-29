from typing import List

class Solution:
  def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
    ROW_LENGTH = len(rowSum)
    COL_LENGTH = len(colSum)
    cur_row_sum = [0] * ROW_LENGTH
    cur_col_sum = [0] * COL_LENGTH
    res = [[0] * COL_LENGTH for _ in range(ROW_LENGTH)]
    for row in range(ROW_LENGTH):
      for col in range(COL_LENGTH):
        res[row][col] = min(rowSum[row] - cur_row_sum[row], colSum[col] - cur_col_sum[col])
        cur_row_sum[row] += res[row][col]
        cur_col_sum[col] += res[row][col]
    
    return res

sol = Solution()
rowSum = [3,8]
colSum = [4,7]
print(f'output: {sol.restoreMatrix(rowSum, colSum)}')