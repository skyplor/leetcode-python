from typing import List

class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    
    def backtracking(current, subset):
      if current >= len(candidates):
        return
      for i in range(current, len(candidates)):
        new_subset = subset + [candidates[i]]
        total_sum = sum(new_subset)
        if total_sum == target:
          res.append(new_subset)
        elif total_sum < target:
          backtracking(i, new_subset)
          
    backtracking(0, [])
    return res

sol = Solution()
candidates = [2,3,5]
target = 8
# candidates = [2,3,6,7]
# target = 7
output = sol.combinationSum(candidates, target)
print(f'candidates: {candidates}\ntarget: {target}\noutput: {output}')