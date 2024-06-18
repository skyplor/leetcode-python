from typing import List
from heapq import heappush, heappop, heapify

class KthLargest:
  
  def __init__(self, k: int, nums: List[int]):
    self.heap = nums
    heapify(self.heap)
    self.k = k
    while len(self.heap) > k:
      heappop(self.heap)
  
  def add(self, val: int) -> int:
    heappush(self.heap, val)
    if len(self.heap) > self.k:
      heappop(self.heap)
    return self.heap[0]
  
k = 3
# nums = [4, 5, 8, 2]
nums = []
obj = KthLargest(k, nums)
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))