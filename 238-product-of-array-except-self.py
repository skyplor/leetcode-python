from typing import List

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    total_length = len(nums)
    prefix = 1
    suffix = 1
    result = [1] * total_length
    for i in range(0, total_length):
      result[i] *= prefix
      prefix *= nums[i]
      
    for i in reversed(range(0, total_length)):
      result[i] *= suffix
      suffix *= nums[i]
    
    return result
  
sol = Solution()
input = [1, 2, 3, 4]
print(f'Input: {input}\nOutput: {sol.productExceptSelf(input)}')