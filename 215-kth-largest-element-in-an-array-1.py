from typing import List
from heapq import heappush, heappop

class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    maxheap = []
    for num in nums:
      heappush(maxheap, -num)
    
    i = 1
    while i < k:
      heappop(maxheap)
      i += 1
    return -maxheap[0]
sol = Solution()
nums = [3,2,1,5,6,4]
k = 2
output = sol.findKthLargest(nums, k)
print(f'nums: {nums}\nk: {k}\noutput: {output}')