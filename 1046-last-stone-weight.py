from typing import List
from heapq import heappush, heappop

class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    maxheap = []
    for stone in stones:
      heappush(maxheap, -stone)
    while len(maxheap) > 1:
      s1 = heappop(maxheap)
      s2 = heappop(maxheap)
      if s1 != s2:
        new_weight = abs(s1 - s2)
        heappush(maxheap, -new_weight)
        
    return -maxheap[0] if len(maxheap) > 0 else 0
    
sol = Solution()
# stones = [2, 7, 4, 1, 8, 1]
stones = [1]
output = sol.lastStoneWeight(stones)
print(f'stones: {stones}\noutput: {output}')