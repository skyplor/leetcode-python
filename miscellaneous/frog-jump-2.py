class Solution:
    def frogJump(self, heights: list[int]) -> int:
        n = len(heights)
        if n == 1:
            return 0

        prev2_min = 0
        prev1_min = abs(heights[1] - heights[0])

        for i in range(2, n):
            # from i - 1
            option_1 = prev1_min + abs(heights[i] - heights[i - 1])

            # from i - 2
            option_2 = prev2_min + abs(heights[i] - heights[i - 2])

            current = min(option_1, option_2)

            prev2_min, prev1_min = prev1_min, current

        return prev1_min


sol = Solution()
heights = [10, 20, 30, 10]
output = sol.frogJump(heights)
print(f'output: {output}')
