class Solution:
    def frogJump(self, heights: list[int]) -> int:
        n = len(heights)
        dp = [-1 for _ in range(n)]
        dp[0] = 0
        for i in range(1, n):
            # from i - 1
            prev1_min = dp[i-1] + abs(heights[i] - heights[i - 1])
            dp[i] = prev1_min

            if i > 1:
                # from i - 2
                prev2_min = dp[i-2] + abs(heights[i] - heights[i-2])
                dp[i] = min(prev2_min, prev1_min)

        return dp[n-1]


sol = Solution()
heights = [10, 20, 30, 10]
output = sol.frogJump(heights)
print(f'output: {output}')
