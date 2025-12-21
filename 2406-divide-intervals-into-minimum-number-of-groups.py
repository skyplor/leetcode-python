class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        '''
        We will need to determine which are the intervals that are overlapping and the maximum number of overlapping groups at a single time (this will give us the minimum groups needed)
        We can use sweep line algorithm for this
        See miscellaneous/largest-occurrence-from-intervals.py
        We have an events list that consist of tuples (time, delta), time being the start/end time and delta being +1 for start and -1 for end + 1 (end+1 because we need to consider end as well and only exclude if it's past end)
        We then sort the events based on the time
        Next, we have a max_counter (the result we want) and a cur_counter. Whenever cur_counter > max_counter, we set max_counter to cur_counter
        '''
        events = []
        max_counter = cur_counter = 0
        for start, end in intervals:
            events.append((start, 1))
            events.append((end + 1, -1))

        events.sort()
        for _, delta in events:
            cur_counter += delta
            if max_counter < cur_counter:
                max_counter = cur_counter

        return max_counter


sol = Solution()
intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
output = sol.minGroups(intervals)
print(f'output: {output}')
