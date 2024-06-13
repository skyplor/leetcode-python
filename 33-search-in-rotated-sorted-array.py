from typing import List

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    res = -1
    l, r = 0, len(nums) - 1
    while l <= r:
      m = l + (r - l) // 2
      if nums[m] == target:
        return m

      if nums[m] >= nums[l]:
        if target > nums[m] or target < nums[l]:
          l = m + 1
        else:
          r = m - 1
      else:
        if target < nums[m] or target > nums[r]:
          r = m - 1
        else:
          l = m + 1

    return res
sol = Solution()
nums = [1, 3]
target = 3
output = sol.search(nums, target)
print(f'nums: {nums}\ntarget: {target}\noutput: {output}')