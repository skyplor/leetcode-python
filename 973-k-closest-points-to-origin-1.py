from typing import List
from heapq import heappush, heappop
import math

class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    maxheap = []
    for point in points:
      x, y = point
      distance = math.sqrt(((x - 0) ** 2) + ((y - 0) ** 2))
      heappush(maxheap, [-distance, point])
      while len(maxheap) > k:
        heappop(maxheap)
    
    res = []
    while maxheap:
      res.append(heappop(maxheap)[1])
    return res
      
    
sol = Solution()
points = [[1,3],[-2,2]]
k = 1
output = sol.kClosest(points, k)
print(f'points: {points}\nk: {k}\noutput: {output}')