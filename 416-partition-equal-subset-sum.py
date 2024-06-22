from typing import List

class Solution:
  def canPartition(self, nums: List[int]) -> bool:
    # using dfs will result in time limit exceeding
    # def dfs(subnums, target):
    #   if not subnums: return False
    #   if sum(subnums) == target:
    #     return True
    #   # include first integer
    #   include = dfs(subnums[1:], target - subnums[0]) if target > 0 else False
    #   # exclude first integer
    #   exclude = dfs(subnums[1:], target)
      
    #   return include or exclude

    # return dfs(nums, sum(nums) / 2)
    #
    # using dp
    # we will go from right to left, each time we add that number to existing set of possible results
    if sum(nums) % 2:
      return False
    dp = set([0])
    target = sum(nums) // 2
    for i in range(len(nums) - 1, -1, -1):
      num = nums[i]
      current_dp = set(dp)
      for n in current_dp:
        current_sum = num + n
        if current_sum == target:
          return True
        dp.add(current_sum)
        
    return False
  
sol = Solution()
nums = [1,5,11,5]
# nums = [1,2,3,5]
output = sol.canPartition(nums)
print(f'output: {output}')