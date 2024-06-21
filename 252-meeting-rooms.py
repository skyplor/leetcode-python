from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __repr__(self) -> str:
       print(f'Interval: [{self.start}, {self.end}]')

class Solution:
  def canAttendMeetings(self, intervals: List[List[Interval]]) -> bool:
    if not intervals:
      return True

    intervals.sort(key=lambda i: i.start)

    prev_end = intervals[0].end
    for interval in intervals[1:]:
      start = interval.start
      end = interval.end
      if start < prev_end:
        return False
      else:
        prev_end = end
        
    return True
  
sol = Solution()
# interval_1 = Interval(0, 30)
# interval_2 = Interval(5, 10)
# interval_3 = Interval(15, 20)
interval_1 = Interval(7, 10)
interval_2 = Interval(2, 4)
# intervals = [interval_1, interval_2, interval_3]
intervals = [interval_1, interval_2]
output = sol.canAttendMeetings(intervals)
print(f'intervals: {intervals}\noutput: {output}')
