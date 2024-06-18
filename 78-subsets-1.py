from typing import List

class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    subset = []
    def dfs(i):
      if i >= len(nums):
        res.append(subset.copy())
        return
      
      # include element i
      subset.append(nums[i])
      dfs(i + 1)
      
      # don't include element i
      subset.pop()
      dfs(i + 1)
    
    dfs(0)
    return res
    
sol = Solution()
nums = [1,2,3]
output = sol.subsets(nums)
print(f'nums: {nums}\noutput: {output}')