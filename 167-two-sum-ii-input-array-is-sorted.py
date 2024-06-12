from typing import List

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1
    result = []
    while left < right:
      left_num = numbers[left]
      right_num = numbers[right]
      sum = left_num + right_num
      if sum == target:
        result.append(left + 1)
        result.append(right + 1)
        return result
      if sum < target:
        left += 1
      else:
        right -= 1
  
sol = Solution()
numbers = []
target = 0
output = sol.twoSum(numbers, target)
print(f'Numbers: {numbers}\nTarget: {target}\nOutput: {output}')