from collections import deque


class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        '''
        We will have a loop that goes through each row. At each row, we know the height we can have for each column
        We can use a monotonically increasing stack to store the index of the possible rectangle and the height at the column
        '''
        n = len(matrix[0])
        max_area = 0
        heights = [0] * (n+1)
        for row in matrix:
            for col_i, col in enumerate(row):
                if col == '0':
                    heights[col_i] = 0
                else:
                    heights[col_i] += 1

            stack = deque()
            for i, h in enumerate(heights):
                prev_i = i
                while stack and stack[-1][1] > h:
                    top_i, top_h = stack.pop()
                    max_area = max(max_area, (i - top_i) * top_h)
                    prev_i = top_i
                stack.append([prev_i, h])

            for i, h in stack:
                max_area = max(max_area, (n - i) * h)

        return max_area


sol = Solution()
print(
    f'output: {sol.maximalRectangle([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]])}, expected: 6')
print(f'output: {sol.maximalRectangle([["0"]])}, expected: 0')
print(f'output: {sol.maximalRectangle([["1"]])}, expected: 1')
