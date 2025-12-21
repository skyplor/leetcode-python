class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        '''        
        This is a DP that explores all possible ways to form the target sum n using distinct positive integers raised to the power x.
        For each number, we have two choices: include it in our sum or exclude it.

        Let dp[i][limit] represent the number of ways to form the sum limit using numbers from {1, 2, 3, ..., i} where each number is raised to the power x.
        For each number i and target sum limit, we have two possibilities:
            1. Don't take number i: dp[i][limit] = dp[i-1][limit]
            2. Take number i (if i^x ≤ limit): Add dp[i-1][limit - i^x] ways

        So: dp[i][limit] = dp[i-1][limit] + dp[i-1][limit - i^x] (if possible)

        Base case: dp[0][0] = 1 (one way to make sum 0 with no numbers)
        Answer: dp[starting_index][n] where starting_index is the largest number whose x-th power ≤ n
        Optimization: Process limits in reverse order to handle the "take/don't take" pattern cleanly
        '''
        starting_index = int(n ** (1/x))
        while (starting_index + 1) ** x <= n:
            starting_index += 1
        while starting_index ** x > n:
            starting_index -= 1

        dp = [[0] * (n+1) for _ in range(starting_index+1)]
        MOD = 10 ** 9 + 7

        dp[0][0] = 1

        for i in range(1, starting_index+1):
            value = i ** x
            for limit in range(n, -1, -1):
                notake = dp[i-1][limit]

                take = 0
                if limit - value >= 0:
                    take = dp[i-1][limit - value]

                dp[i][limit] = (take + notake) % MOD

        res = dp[starting_index][n]

        return res


sol = Solution()
print(f'output: {sol.numberOfWays(64, 3)}')
# print(f'output: {sol.numberOfWays(4, 1)}')
