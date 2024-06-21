from typing import List

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    res = [intervals[0]]

    for start,end in intervals:
      prev_end = res[-1][1]

      if start <= prev_end:
        res[-1][1] = max(prev_end, end)
      else:
        res.append([start, end])
        
    return res
  
sol = Solution()
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
output = sol.merge(intervals)
print(f'intervals: {intervals}\noutput: {output}')