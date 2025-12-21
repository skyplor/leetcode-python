import math
from collections import defaultdict


class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        '''
        We first use hash to get the number of points for each y-coordinate
        Next, we iterate through each group, calculate the total number of combinations for that group, i.e. count choose 2
        We then use the previous calculated total pairs and multiply by this combination to get the number of possible quadrilaterals we can get (because we choose 2 from current group and choose 2 from ALL previous points)
        Then we add this calculated value into our `res`
        we can then include the current calculated points into the previous calculated pairs and continue to the next group
        At the end we return the `res`
        '''
        MOD = 10 ** 9 + 7
        count = defaultdict(int)
        res = 0
        prev_total_acc_pairs = 0

        for _, y1 in points:
            count[y1] += 1

        for val in count.values():
            cur = math.comb(val, 2)
            res = (res + prev_total_acc_pairs * cur) % MOD
            prev_total_acc_pairs = (prev_total_acc_pairs + cur) % MOD

        return res


sol = Solution()
print(f'output: {sol.countTrapezoids([[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]])}, expected: 3')
print(f'output: {sol.countTrapezoids([[0, 0], [1, 0], [0, 1], [2, 1]])}, expected: 1')
