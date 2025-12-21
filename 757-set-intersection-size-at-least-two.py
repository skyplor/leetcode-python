from collections import defaultdict


class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        '''
        Using greedy approach, we first sort the intervals by the end_time.
        We have a set of `nums` that we picked
        Next, we go through each sorted interval, we check how many of the last 2 points in `nums` are part of the current interval.
            - 0: add current's end_time and end_time - 1 into `nums`
            - 1: add current's end_time into `nums`
            - 2: Do nothing

        At the end, return len(nums)
        '''
        nums = []
        sorted_intervals = sorted(intervals, key=lambda i: i[1])
        for start, end in sorted_intervals:
            count = 0
            if nums and nums[-1] >= start:
                count += 1
            if len(nums) >= 2 and nums[-2] >= start:
                count += 1

            if count == 0:
                nums.append(end - 1)
                nums.append(end)
            elif count == 1:
                if nums[-1] == end:
                    nums.append(end - 1)
                else:
                    nums.append(end)

        return len(nums)


sol = Solution()
print(
    f'output: {sol.intersectionSizeTwo([[1, 3], [3, 7], [8, 9]])}, expected: 5')
print(
    f'output: {sol.intersectionSizeTwo([[1, 3], [1, 4], [2, 5], [3, 5]])}, expected: 3')
print(
    f'output: {sol.intersectionSizeTwo([[1, 2], [2, 3], [2, 4], [4, 5]])}, expected: 5')
print(
    f'output: {sol.intersectionSizeTwo([[1, 3], [3, 7], [5, 7], [7, 8]])}, expected: 5')
