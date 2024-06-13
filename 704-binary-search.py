from typing import List

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1
    while start <= end:
      mid = ((end - start) // 2) + start
      if target < nums[mid]:
        end = mid - 1
      elif target > nums[mid]:
        start = mid + 1
      else:
        return mid
      
    return -1

sol = Solution()
nums = [-1,0,3,5,9,12]
target = 9
output = sol.search(nums, target)
print(f'nums: {nums}\ntarget: {target}\noutput: {output}')