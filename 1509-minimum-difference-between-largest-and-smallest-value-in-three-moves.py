from typing import List

class Solution:
  def minDifference(self, nums: List[int]) -> int:
    '''
    There are a few scenarios we need to take note of:
    1. we can remove all 3 biggest values and then take the difference between next largest and smallest value
    2. we can remove all 3 smallest values and then take the difference between next smallest and largest value
    3. we can remove 2 biggest values and 1 smallest value then take the difference between next largest and smallest value
    3. we can remove 1 biggest values and 2 smallest value then take the difference between next largest and smallest value
    '''
    n = len(nums)
    if n <= 4:
      return 0
    nums.sort()
    # diff for case 1
    diff1 = nums[n-4] - nums[0]
    # diff for case 2
    diff2 = nums[n-1] - nums[3]
    # diff for case 3
    diff3 = nums[n-3] - nums[1]
    # diff for case 4
    diff4 = nums[n-2] - nums[2]

    return min(diff1, diff2, diff3, diff4)
  
sol = Solution()
# nums = [1,5,0,10,14]
# nums = [5,3,2,4]
nums = [6,6,0,1,1,4,6]
print(f'output: {sol.minDifference(nums)}')