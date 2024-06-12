from typing import List
from collections import deque

class Solution:
  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    res = []
    q = deque()
    l = r = 0
    while r < len(nums):
      # pop smaller values from q
      while q and nums[q[-1]] < nums[r]:
        q.pop()

      q.append(r)
      
      # remove left val from window
      if l > q[0]:
        q.popleft()
        
      if (r + 1) >= k:
        res.append(nums[q[0]])
        l += 1
      r += 1

    return res

sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
# nums = [1, -1]
# k = 1
output = sol.maxSlidingWindow(nums, k)
print(f'nums: {nums}\nk: {k}\nOutput: {output}')