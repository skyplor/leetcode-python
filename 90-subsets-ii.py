from typing import List
import functools

class Solution:
  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    sorted_nums = sorted(nums)
    res = []
    
    def backtracking(start, temp):
      if start == len(sorted_nums):
        res.append(temp)
        return
      backtracking(start + 1, temp + [sorted_nums[start]])

      while start + 1 < len(sorted_nums) and sorted_nums[start+1] == sorted_nums[start]:
        start += 1

      backtracking(start + 1, temp)
        
    backtracking(0, [])
    return res

sol = Solution()
# nums = [1,2,2]
nums = [4,4,4,1,4]
output = sol.subsetsWithDup(nums)
print(f'nums: {nums}\noutput: {output}')