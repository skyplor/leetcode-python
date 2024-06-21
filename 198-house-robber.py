from typing import List

class Solution:
  def rob(self, nums: List[int]) -> int:
    '''
    if i = 0,
      indices: (0)

    if i = 1,
      indices: [1] or [0]
      
    if i = 2,
      indices: [2 + (0)] or [1]

    if i = 3,
      indices: [3 + (0 to 1)] or [(0 to 2)]
      
    if n = 4,
      indices: [4 + (0 to 2)] or [(0 to 3)]
    '''
    if len(nums) <= 2: return max(nums)

    nums[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
      nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])

    return nums[-1]
sol = Solution()
# nums = [1,2,3,1]
nums = [2, 1, 1, 2]
print(f'nums: {nums}')
output = sol.rob(nums)

print(f'output: {output}')