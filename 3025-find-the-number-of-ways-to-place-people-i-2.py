from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        '''
        We will have a `result` variable and initialise it to 0
        We first sort the points by x-coordinate and then by negated y-coordinate because we want all points to be sorted left to right, then top to bottom within each x-coordinatet.
        This allows us to process the points in order, ensuring that the next point will be at the same x-coordinate or to the right.

        For each point as a potential top-left corner, we examine subsequent points (which are guaranteed to have x ≥ current x due to sorting).
        We track bottom as the lowest y-coordinate of rectangles we've already counted.
        For each subsequent point, if bottom < y ≤ top, it forms a valid non-overlapping rectangle.
        We stop when bottom == top because no further points can satisfy the constraint.

        Time: O(n^2)
        Space: O(1)
        '''

        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)

        result = 0
        for i, (_, y1) in enumerate(points):
            bottom = float('-inf')
            for j in range(i+1, n):
                _, y2 = points[j]
                if bottom < y2 <= y1:
                    result += 1
                    bottom = y2
                    if bottom == y1:
                        break

        return result


sol = Solution()
points = [[1, 1], [2, 2], [3, 3]]
print(f'output: {sol.numberOfPairs(points)}, expected: 0')
points = [[6, 2], [4, 4], [2, 6]]
print(f'output: {sol.numberOfPairs(points)}, expected: 2')
points = [[3, 1], [1, 3], [1, 1]]
print(f'output: {sol.numberOfPairs(points)}, expected: 2')
