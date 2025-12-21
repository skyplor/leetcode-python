class Solution:
    def min_cost_i_i(self, costs: list[list[int]]) -> int:
        '''
        Similar to 256. Paint House. For this solution, to further optimise it so the time complexity is O(nk), we need to use 2 variables:
            - first_min, second_min

        Basic idea is we pre-retrieve the min values of the prev row. We have a backup min (second_min) as well in case we cannot use the first_min because the color of that first_min is used in the current house. So we have to use second_min just for this scenario
        Time Complexity:
            O(n*k)


        '''
        n = len(costs)
        k = len(costs[0])
        dp = [[0] * k for _ in range(n)]
        dp[0] = costs[0][:]

        for house in range(1, n):
            prev_costs = dp[house-1]
            first_min = second_min = float('inf')
            for cost in prev_costs:
                if cost < first_min:
                    first_min = cost
                elif cost < second_min:
                    second_min = cost

            for color in range(k):
                if prev_costs[color] == first_min:
                    dp[house][color] = costs[house][color] + second_min
                else:
                    dp[house][color] = costs[house][color] + first_min

        return min(dp[n-1])


sol = Solution()
# costs = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
costs = [[5, 5, 5], [5, 5, 5]]
output = sol.min_cost_i_i(costs)
print(f'output: {output}')
