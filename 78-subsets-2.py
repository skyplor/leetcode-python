from typing import List

class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    def backtrack(start, subset):
      res.append(subset)
      for i in range(start, len(nums)):
        backtrack(i + 1, subset + [nums[i]])
      
    backtrack(0, [])
    return res
    
sol = Solution()
nums = [1,2,3]
output = sol.subsets(nums)
print(f'nums: {nums}\noutput: {output}')