from typing import List

class Solution:
  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()

    def backtracking(curArray, pos, target):
      if target == 0:
        res.append(curArray.copy())
        return
      if target <= 0:
        return
      
      prev = -1
      for i in range(pos, len(candidates)):
        if candidates[i] == prev:
          continue
        curArray.append(candidates[i])
        backtracking(curArray, i + 1, target - candidates[i])
        curArray.pop()
        prev = candidates[i]
    
    backtracking([], 0, target)
    return res
  
sol = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(f'output: {sol.combinationSum2(candidates, target)}')