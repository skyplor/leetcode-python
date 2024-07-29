from typing import List
from heapq import heappush, heappop

class Solution:
  def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    # Solution 1:
    '''
    using maxheap with heights as the key
    '''
    max_heap = []
    for i in range(len(names)):
      heappush(max_heap, (-heights[i], names[i]))
      
    res = []
    while max_heap:
      _, name = heappop(max_heap)
      res.append(name)

    return res
    
    # Solution 2:
    # '''
    # using zip and sort them and return in array
    # '''
    # return [name for _, name in sorted(zip(heights, names), reverse=True)]

sol = Solution()
names = ["Mary","John","Emma"]
heights = [180,165,170]
print(f'output: {sol.sortPeople(names, heights)}')