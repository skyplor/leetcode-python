class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        '''
        DP with Remainder Tracking

        We only care about remainder mod 3 (0, 1, or 2), not exact sums.

        dp[i][r] = max sum from index i onwards that has remainder r (mod 3)

        Base case:
        - dp[n][0] = 0 (empty sum has remainder 0)
        - dp[n][1] = dp[n][2] = -inf (can't achieve remainder 1/2 with no elements)

        To achieve remainder r at index i, we have two choices:
            1. Skip nums[i]: future elements must give remainder r -> dp[i+1][r]
            2. Take nums[i]: future must give remainder (r - nums[i]) % 3 
        so total is r -> nums[i] + dp[i+1][(r - nums[i]) % 3]

        Answer: dp[0][0] = max sum divisible by 3 using all elements

        Time: O(n), Space: O(n)
        '''

        n = len(nums)
        dp = [[-1] * 3 for _ in range(n + 1)]

        dp[n][0] = 0
        dp[n][1] = float('-inf')
        dp[n][2] = float('-inf')

        for i in range(n-1, -1, -1):
            for r in range(3):
                dp[i][r] = max(nums[i] + dp[i+1]
                               [(r - nums[i]) % 3], dp[i+1][r])

        return dp[0][0]


sol = Solution()
print(f'output: {sol.maxSumDivThree([3, 6, 5, 1, 8])}, expected: 18')
print(f'output: {sol.maxSumDivThree([4])}, expected: 0')
print(f'output: {sol.maxSumDivThree([1, 2, 3, 4, 4])}, expected: 12')
