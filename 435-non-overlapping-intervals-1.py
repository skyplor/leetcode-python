from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        We can use the greedy approach here by sorting according to the end time.
        This way, we are taking the shorter span ones because if both have same start time, we will loop and get the one that has the earlier stop time.
        Why we need to do this is because if we take the longer span ones, then it has a higher probability of overlapping the next few ones.
        We will need 2 variables, count and last_end
        So we sort, then go through each interval, if the last_end > current_start, then we exclude this entry. Else, we include, update last_end to current's end and increment count
        '''
        intervals.sort(key=lambda x: x[1])
        count = 0
        last_end = float('-inf')
        for current_start, current_end in intervals:
            if current_start < last_end:
                count += 1
            else:
                last_end = current_end

        return count


sol = Solution()
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
output = sol.eraseOverlapIntervals(intervals)
print(f'intervals: {intervals}\noutput: {output}')
