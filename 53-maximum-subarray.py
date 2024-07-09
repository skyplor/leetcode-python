from typing import List

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    res = nums[0]
    curSum = 0
    for n in nums:
      if curSum < 0:
        curSum = 0
      curSum += n
      res = max(res, curSum)
      
    return res
  
sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(f'output: {sol.maxSubArray(nums)}')