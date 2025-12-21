from typing import List

class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    # using 1-d DP, we need to find out the base case. what is the smallest case that can give us the result immediately
    # we can start at the last index and that will give us the result immediately
    # so it will be dp[len(nums) - 1] = 1
    n = len(nums)
    dp = [1] * (n)
    for i in range(n)[::-1]:
      for j in range(i+1, n):
        if nums[i] < nums[j]:
          dp[i] = max(dp[i], 1 + dp[j])
          
    return max(dp)
    
sol = Solution()
nums = [10,9,2,5,3,7,101,18]
output = sol.lengthOfLIS(nums)
print(f'nums: {nums}\noutput: {output}')