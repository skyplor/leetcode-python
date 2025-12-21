from typing import List

class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    res = 0
    intervals.sort()
    prev_end = intervals[0][1]

    for start,end in intervals[1:]:
      if start >= prev_end:
        prev_end = end
      else:
        # remove one of the intervals
        res += 1
        prev_end = min(prev_end, end)

    return res
sol = Solution()
intervals = [[1,2], [2,3],[3,4],[1,3]]
output = sol.eraseOverlapIntervals(intervals)
print(f'intervals: {intervals}\noutput: {output}')