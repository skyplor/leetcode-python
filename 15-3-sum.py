from typing import List

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    sorted_nums = sorted(nums)
    result = []

    for i in range(0, len(sorted_nums)):
      if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
        continue
      current = sorted_nums[i]
      l = i + 1
      r = len(sorted_nums) - 1

      while l < r:
        total = sorted_nums[l] + sorted_nums[r] + current

        if total == 0:
          result.append([current, sorted_nums[l], sorted_nums[r]])
          while l < r and sorted_nums[l+1] == sorted_nums[l]:
            l += 1
          while l < r and sorted_nums[r-1] == sorted_nums[r]:
            r -= 1
          l += 1
          r -= 1
        elif total < 0:
          l += 1
        else:
          r -= 1

    return result

sol = Solution()
input = [-1,0,1,2,-1,-4]
# input = [0, 1, 1]
# input = [0, 0, 0]
output = sol.threeSum(input)
print(f'Input: {input}\nOutput: {output}')