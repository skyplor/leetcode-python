from typing import List

class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    res = []
    
    def backtracking(current):
      if len(current) == len(nums):
        res.append(current)
        return
      for i in range(len(nums)):
        current_num = nums[i]
        if current_num in current: continue

        current.append(current_num)
        backtracking(current.copy())
        current.pop()
        
    backtracking([])
      
    return res
sol = Solution()
nums = [1,2,3]
output = sol.permutations(nums)
print(f'nums: {nums}\noutput: {output}')