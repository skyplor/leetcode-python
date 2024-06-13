from typing import List

class Solution:
  def findMin(self, nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    res = nums[0]

    while l <= r:
      if nums[l] < nums[r]:
        res = min(res, nums[l])
        break

      m = l + (r-l) // 2
      res = min(res, nums[m])
      if nums[m] >= nums[l]:
        l = m + 1
      else:
        r = m - 1

    return res
  
sol = Solution()
nums = [3, 4, 5, 1, 2]
output = sol.findMin(nums)
print(f'nums: {nums}\noutput: {output}')