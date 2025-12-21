from collections import defaultdict


class Solution:
    def max_duffel_bag_value(self, cake_tuples: list[tuple[int, int]], capacity: int) -> int:
        '''
        This is an unbounded knapsack problem
        We can use iterative way + DP to resolve this

        We will first create a DP with size `capacity + 1`
        All values will be 0 at the start
        We loop through the capacity from 1 to `capacity` and for each capacity, we loop through each cake.
            - If "current capacity - weight of cake" is >= 0, that means we can take the cake. 
            - If so, we update dp[c] to be the maximum of:
                * The current best value for capacity c
                * The value we get by taking this cake plus the optimal value for the remaining capacity
            
        At the end, we return dp[capacity]
        '''
        dp = [0 for _ in range(capacity+1)]

        for c in range(1, capacity+1):
            for wt, val in cake_tuples:
                if wt == 0:
                    continue
                if c - wt >= 0:
                    dp[c] = max(dp[c], val + dp[c - wt])

        return dp[capacity]


sol = Solution()
cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 20
print(
    f'output: {sol.max_duffel_bag_value(cake_tuples, capacity)}, expected: 555')
cake_tuples = [(0, 160), (3, 0), (2, 15)]
capacity = 20
print(
    f'output: {sol.max_duffel_bag_value(cake_tuples, capacity)}, expected: 150')
cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 0
print(
    f'output: {sol.max_duffel_bag_value(cake_tuples, capacity)}, expected: 0')
