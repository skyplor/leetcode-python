from typing import List

class Solution:
  def canJump(self, nums: List[int]) -> bool:
    '''
    if we are at the last position, can we reach the last position?
    if we are at the last 2nd position, can we reach the last position?
    e.g [2,3,1,1,4]
    pos[n] = for i in range(1, num[n] + 1): return pos[n+i]
    '''
    # Recursion
    # Time: O(max(nums) ^n)
    # Space: O(n)

    # n = len(nums)
    # def can_reach(i):
    #   if i == n - 1:
    #     return True
    #   for jump in range(1, nums[i] + 1):
    #     if can_reach(i + jump):
    #       return True

    #   return False

    # return can_reach(0)

    # Top-down DP (Memoization)
    # Time: O(n^2)
    # Space: O(n)
    # n = len(nums)
    # memo = {n-1: True}
    # def can_reach(i):
    #   if i in memo:
    #     return memo[i]

    #   for jump in range(1, nums[i] + 1):
    #     if can_reach(i + jump):
    #       memo[i] = True
    #       return True

    #   memo[i] = False
    #   return False
    # return can_reach(0)

    # Greedy
    n = len(nums)
    goal = n-1
    for i in range(n-1)[::-1]:
      steps = nums[i]
      if i + steps >= goal:
        goal = i

    return goal == 0
  
sol = Solution()
# nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]
nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
print(f'output: {sol.canJump(nums)}')