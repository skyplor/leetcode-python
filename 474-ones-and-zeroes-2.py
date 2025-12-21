class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        '''
        2D DP approach using 0/1 knapsack with two constraints.

        dp[i][j] = maximum number of strings we can form with at most i 0s and j 1s

        For each string, we decide whether to include it or not:
        - Skip: dp[i][j] remains unchanged
        - Include: dp[i][j] = 1 + dp[i - zeros_in_string][j - ones_in_string]

        We iterate backwards through the DP table to ensure each string is only 
        used once (if we go forwards, we might reuse updated values from the 
        current iteration).

        Time: O(len(strs) * m * n)
        Space: O(m * n)
        '''

        dp = [[0] * (n+1) for _ in range(m+1)]
        for str in strs:
            cur_ones = str.count('1')
            cur_zeros = len(str) - cur_ones
            for zeros in range(m, cur_zeros - 1, -1):
                for ones in range(n, cur_ones - 1, -1):
                    dp[zeros][ones] = max(
                        dp[zeros][ones], 1 + dp[zeros - cur_zeros][ones - cur_ones])

        return dp[m][n]


sol = Solution()
print(
    f'output: {sol.findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3)}, expected: 4')
print(
    f'output: {sol.findMaxForm(strs=["10", "0", "1"], m=1, n=1)}, expected: 2')
