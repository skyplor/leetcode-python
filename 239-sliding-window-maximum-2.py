from typing import List
from heapq import heappush, heappop

class Solution:
  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    res = []
    heap = []

    for i in range(k):
      heappush(heap, [-nums[i], i])

    res.append(-heap[0][0])

    for r in range(k, len(nums)):
      heappush(heap, [-nums[r], r])

      while heap[0][1] < r - k + 1:
        heappop(heap)

      res.append(-heap[0][0])

    return res

sol = Solution()
# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
nums = [1, -1]
k = 1
output = sol.maxSlidingWindow(nums, k)
print(f'nums: {nums}\nk: {k}\nOutput: {output}')