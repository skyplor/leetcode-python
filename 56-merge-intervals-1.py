from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        We need 2 variables: res and last_end
        res will store the result set
        Since we are merging overlapping intervals, we sort by start time to process them in timeline order.

        We sort by start time because:
          1. It gives us a left-to-right processing order on the timeline
          2. When we process intervals in start-time order, we only need to check if the current interval overlaps with the LAST interval in our result (since all previous intervals in the result are guaranteed to be non-overlapping and to the left)
          3. Overlap condition becomes simple: current.start <= last.end
          4. If they overlap, we merge by keeping the earlier start (which is already last.start) and taking the maximum end time
        '''
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = res[-1][1]
            if start > last_end:
                res.append([start, end])
            else:
                res[-1][1] = max(last_end, end)
                
        return res


sol = Solution()
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
intervals = [[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]
output = sol.merge(intervals)
print(f'intervals: {intervals}\noutput: {output}')
