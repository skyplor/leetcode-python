class Solution:
    def numberOfWays(self, corridor: str) -> int:
        '''
        We first calculate the total number of seats such that it has to be even.
        If there's odd number, we return 0 at the start. 

        Next, we use modified prefix sum to calculate the number of seats from the left,
            if we encounter a 3rd seat, we restart from 1, and if we encounter a flower,
            we take the value from the previous index.

        So in the end it will be something like 0, 1, 1, 2, 2, 2, 1, 2, 2, 1, 2...
        Now that we got the prefix sum, we find all the 2's and treat each as a group.

        Then similar to how we permute between groups,
            we just take the number of 2s in each group and multiply.

        e.g [1, 2, 2, 2, 1, 1, 2, 2, 2]

        One thing to note is to treat the last group of 2s as 1
        '''
        GROUPING_MAP = {0: 1, 1: 2, 2: 1}
        s_count = corridor.count('S')
        if s_count < 2 or s_count % 2 != 0:
            return 0

        groupings = [0] * len(corridor)
        for i, ch in enumerate(corridor):
            if ch == 'P':
                groupings[i] = groupings[i-1]
                continue
            groupings[i] = GROUPING_MAP[groupings[i-1]]

        right = 1
        res = 1
        left = 0
        while right < len(corridor) - 1:
            prev, curr = groupings[right-1], groupings[right]
            if prev == 1 and curr == 2:
                # start of a new group
                multiplier = 1
                left = right
                if groupings[right] == 2:
                    while right < len(corridor) - 1 and groupings[right] == 2:
                        right += 1
                    if right < len(corridor) - 1:
                        multiplier = right - left

                    res = (res * multiplier) % (10 ** 9 + 7)

            right += 1

        return res


sol = Solution()
print(f'output: {sol.numberOfWays("SSPPSPS")}, expected: 3')
print(f'output: {sol.numberOfWays("PPSPSP")}, expected: 1')
print(f'output: {sol.numberOfWays("S")}, expected: 0')
