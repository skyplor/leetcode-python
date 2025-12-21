from typing import List


class Solution:
    def max_value(self, weights: List[int], values: List[int], max_weight: int) -> int:
        '''
        3 rules of DP:
            1. Express in terms of index. In this case, at each index, we have a bag capacity W so `dp(idx, W)`
            2. Explore all possibilities (pick vs no-pick)
            3. Get the max of all possibilities

        So based on this, we can have a 2-D DP. At each index, we can either take the item or don't take the item. Then we continue to explore the next index

        '''

        n = len(weights)
        dp = [[0] * (max_weight + 1) for _ in range(n)]
    
        if weights[0] <= max_weight:
            for w in range(weights[0], max_weight + 1):
                dp[0][w] = values[0]
            
        for i in range(1, n):
            for w in range(max_weight + 1):
                dont_take_value = dp[i-1][w]
                take_value = float('-inf')
                if weights[i] <= w:
                    take_value = values[i] + dp[i-1][w-weights[i]]

                dp[i][w] = max(dont_take_value, take_value)

        return dp[n-1][max_weight]


sol = Solution()
weights = [10, 20, 30]
values = [60, 100, 120]
max_weight = 50
print(f'output: {sol.max_value(weights, values, max_weight)}')
weights = [1, 2, 3]
values = [10, 20, 30]
max_weight = 5
print(f'output: {sol.max_value(weights, values, max_weight)}')
