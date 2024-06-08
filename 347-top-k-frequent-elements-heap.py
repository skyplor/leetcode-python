from collections import defaultdict
from heapq import heappush, heappop
from typing import List

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    num_occurrence = defaultdict(int)
    for num in nums:
      num_occurrence[num] += 1

    max_heap = []
    for key in num_occurrence:
      heappush(max_heap, (-num_occurrence[key], key))

    result = []
    
    for _ in range(k):
      _,ans = heappop(max_heap)
      result.append(ans)
    
    return result
sol = Solution()
# print(sol.topKFrequent([-1, -1], 1))
print(sol.topKFrequent([1, -1, 2, 2, 3, 1, 2], 2))