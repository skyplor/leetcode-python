from typing import List

class Solution:
  def rob(self, nums: List[int]) -> int:
    '''
    need to check if the last index then cannot rob first index also
    we just have to call 2 sub-arrays each time.
      array 1 includes first element, excludes last element
      array 2 includes last element, excludes first element
    '''
    if len(nums) <= 3: return max(nums)


    return max(self.helper(nums[1:]), self.helper(nums[:-1]))
  
  def helper(self, nums):
    if len(nums) <= 2: return max(nums)
    nums[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
      nums[i] = max(nums[i - 2] + nums[i], nums[i-1])
    return nums[-1]
  
sol = Solution()
nums = [1,2,3,1]
print(f'nums: {nums}')
output = sol.rob(nums)
print(f'output: {output}')