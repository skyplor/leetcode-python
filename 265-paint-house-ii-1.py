class Solution:
    def min_cost_i_i(self, costs: list[list[int]]) -> int:
        '''
        Similar to 256. Paint House, but we can use 2d matrix instead of single row
        Time Complexity:
            O(n*k*k) = O(nk^2)
            
        Because allocating of the temp_dp requires O(k)
        '''
        n = len(costs)
        k = len(costs[0])
        dp = [[0] * k for _ in range(n)]
        dp[0] = costs[0][:]

        for house in range(1, n):
            for color in range(k):
                temp_dp = dp[house-1][:]
                temp_dp[color] = float('inf')
                dp[house][color] = costs[house][color] + min(temp_dp)

        return min(dp[n-1])


sol = Solution()
costs = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
output = sol.min_cost_i_i(costs)
print(f'output: {output}')
