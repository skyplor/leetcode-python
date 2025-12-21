from collections import defaultdict


class Solution:
    def max_duffel_bag_value(self, cake_tuples: list[tuple[int, int]], capacity: int) -> int:
        '''
        This is an unbounded knapsack problem
        We can use recursion + dp (caching).

        For each cake, we try to do recursive call for all other cakes including itself, reducing the capacity for each call
            - We need to check that reducing the capacity results in either 0 or positive capacity before taking the cake
        Base case will be when the capacity == 0
            - When this is the case, we check the current running monetary value, and update the max monetary value if it is larger

        We also need to check if we can still take ANY cake. If we can't take any more cakes, even if capacity is not 0, this current value is the max value we have
        '''
        dp = defaultdict(int)

        def take_cake(capacity: int) -> int:

            if capacity == 0:
                return 0

            if capacity in dp:
                return dp[capacity]

            for wt, val in cake_tuples:
                if capacity - wt >= 0:
                    dp[capacity] = max(
                        dp[capacity], val + take_cake(capacity - wt))
                    
            return dp[capacity]

        return take_cake(capacity)


sol = Solution()
cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 20
print(
    f'output: {sol.max_duffel_bag_value(cake_tuples, capacity)}, expected: 555')
