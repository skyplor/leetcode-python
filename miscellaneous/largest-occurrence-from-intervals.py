from typing import List


class Solution:
    def largest_occurrence(self, intervals: List[List[int]]) -> int:
        '''
        We can use sweep line algorithm for this
        Sweep line algo:
            - create max_count, cur_count and result variables
            - create an events list that contains the tuple (time, delta)
                - time being the start or end time
                - delta being +1 for start, -1 for end+1 (since intervals are inclusive)
            - process each interval, and populate events list with the tuple above
            - sort the events list by the time
            - process each event
                - add the delta to the cur_count
                - update max_count if cur_count > max_count
                - update result to the current time/position if cur_count > max_count (this gives us a number with maximum occurrence)

        if result is -1, we can set the result to the first interval's start time
        '''
        max_count = cur_count = 0
        result = -1
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end + 1, -1))

        events.sort(key=lambda x: x[0])
        for time, delta in events:
            cur_count += delta
            if cur_count > max_count:
                max_count = cur_count
                result = time

        if result == -1:
            result = intervals[0][0]

        return result


sol = Solution()
intervals = [[1, 10], [1, 3], [11, 24], [2, 4]]
output = sol.largest_occurrence(intervals)
print(f'output: {output}')
