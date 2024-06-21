from typing import List

class Solution:
  def maxProduct(self, nums: List[int]) -> List[int]:
    '''
    at index n, the result will be either n*max(n-1) or max(n-1)
    base case:
      index 0:
        result = nums[0]
      index 1:
        result = max(nums[0] * nums[1], nums[0])
    '''
    if not nums: return 0
    if len(nums) == 1:
      return nums[0]

    res = max(nums)
    curMin, curMax = 1, 1 # multiplying by 1 allows it to be neutral
    for num in nums:
      tmp = num * curMax
      curMax = max(num * curMin, tmp, num)
      curMin = min(num * curMin, tmp, num)
      res = max(curMax, res)

    return res
  
sol = Solution()
nums = [2, 3, -2, 4]
# nums = [-2, 0, 1]
# nums = [-2, 0, -1]
# nums = [0, 2]
# nums = [-2,3,-4]
# nums = [2,-1,1,1]
output = sol.maxProduct(nums)
print(f'output: {output}')