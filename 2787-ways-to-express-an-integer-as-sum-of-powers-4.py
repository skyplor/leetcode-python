class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        '''        
        This is a space-optimized DP solution that explores all possible ways to form the target sum n 
        using distinct positive integers raised to the power x. For each number, we have two choices: 
        include it in our sum or exclude it.

        Let dp[limit] represent the number of ways to form the sum 'limit' using the numbers processed so far.

        For each number i and target sum limit, we have two possibilities:
            1. Don't take number i: keep dp[limit] as is
            2. Take number i (if i^x ≤ limit): add dp[limit - i^x] ways

        So: dp[limit] = dp[limit] + dp[limit - i^x] (if i^x ≤ limit)

        Space Optimization:
        - We use a 1D array instead of 2D since we only need the previous "row" to compute the current one
        - Process limits in REVERSE order (n down to 0) to ensure dp[limit - i^x] hasn't been 
        updated yet in the current iteration (it still contains the "previous row" value)

        Base case: dp[0] = 1 (one way to make sum 0 with no numbers)
        Answer: dp[n] after processing all valid numbers
        Starting index: largest number whose x-th power ≤ n (with floating-point correction)
        '''
        starting_index = int(n ** (1/x))
        while (starting_index + 1) ** x <= n:
            starting_index += 1
        while starting_index ** x > n:
            starting_index -= 1

        dp = [0] * (n+1)
        MOD = 10 ** 9 + 7

        dp[0] = 1

        for i in range(1, starting_index+1):
            value = i ** x
            for limit in range(n, -1, -1):
                notake = dp[limit]

                take = 0
                if limit - value >= 0:
                    take = dp[limit - value]

                dp[limit] = (take + notake) % MOD

        return dp[n]


sol = Solution()
print(f'output: {sol.numberOfWays(64, 3)}')
# print(f'output: {sol.numberOfWays(4, 1)}')
