from typing import List

class Solution:
  def findTargetSumWays(self, nums: List[int], target: int) -> int:
    '''
                    index, sum
                       (0, 0)
                     +1 // \\ -1
                  (1, 1)     (1, -1)
               +1 // \\ -1    // \\
            (2, 2)    (2, 0)   ...
            // \\   +1 // \\ -1
             ...   (3, 1)  ...
                 +1 // \\ -1
              (4, 2)    ...
            +1 // \\ -1
         (5, 3)    ...
    
    We will notice that once we are at the last index, depending on current sum, we will know the choice:
    if sum == target + -nums[index] or sum == target + nums[index], then we can + nums[index] so it hits the target
    we will store these calculated values as key in a hash to memoize (index, sum) -> number of ways
    
    then we reduce the target and go to the next index using DFS/backtracking
    '''
    
    dp = {}    

    def backtrack(i, sum):
      if i == len(nums):
        return 1 if target == sum else 0
      if (i, sum) in dp:
        return dp[(i, sum)]
      
      dp[(i, sum)] = backtrack(i + 1, sum + nums[i]) + backtrack(i + 1, sum - nums[i])

      return dp[(i, sum)]
    
    return backtrack(0, 0)
  
sol = Solution()
nums = [1]
target = 1
# nums = [1,1,1,1,1]
# target = 3
print(f'output: {sol.findTargetSumWays(nums, target)}')