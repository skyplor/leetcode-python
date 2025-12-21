from collections import defaultdict
import bisect


class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        '''
        We first sort the power
        Next, we compress the sorted power to remove the duplicated values and at the same time compute the sum of each value and use a hashmap to store the sum of each value
        Next, we iterate through the compressed list of sorted powers
            - in each iteration, we use binary search to find the last value that is <= current value - 3 (we can use bisect_right)
                - we need to take note to subtract 1 from it because it will find the index that is > current value - 3.
                - Once we get the idx,
                    - if we take the current value, we will get the total of current value's sum + prev index's sum.
                    - if we don't take current value, we get the sum based on the prev index value
                    - Then we simply get the max of the 2 sum
        at the end, we just return dp[n-1]
        '''
        sum_map = defaultdict(int)
        for item in power:
            sum_map[item] += item
        values = [key for key in sum_map.keys()]
        n = len(values)
        values.sort()
        dp = [0] * n
        dp[0] = sum_map[values[0]]

        for i in range(1, n):
            item = values[i]
            idx = bisect.bisect_right(values, item - 3) - 1
            dont_take = dp[i-1]

            take = sum_map[item]
            if 0 <= idx < n:
                take += dp[idx]
            dp[i] = max(dont_take, take)

        return dp[n - 1]


sol = Solution()
print(f'output: {sol.maximumTotalDamage([1, 1, 3, 4])}, expected: 6')
print(f'output: {sol.maximumTotalDamage([7, 1, 6, 6])}, expected: 13')
