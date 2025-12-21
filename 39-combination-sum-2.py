from typing import List

class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def backtracking(current: List[int], index: int, total: int):
        if total > target or index >= len(candidates):
            return

        if total == target:
            res.append(current)
            return

        c_copy = current.copy()
        c_copy.append(candidates[index])
        backtracking(c_copy, index, total + candidates[index])
        backtracking(current, index+1, total)
          
    backtracking([], 0, 0)
    return res

sol = Solution()
candidates = [2,3,5]
target = 8
# candidates = [2,3,6,7]
# target = 7
output = sol.combinationSum(candidates, target)
print(f'candidates: {candidates}\ntarget: {target}\noutput: {output}')