from collections import defaultdict
from math import gcd


class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        '''
        Solution: Count trapezoids using inclusion-exclusion principle.

        Approach:
        1. A trapezoid is a convex quadrilateral with at least one pair of parallel sides
        2. Generate all possible edges (line segments between pairs of points)
        3. Group edges by slope - edges with the same slope are parallel
        4. Within each slope group, group edges by intercept (line equation)
        - Edges with same slope AND intercept are collinear (on the same line)
        - Edges with same slope but different intercepts are on parallel lines
        5. Count all ways to pick 2 edges from different parallel lines (same slope, different intercept)
        This gives us trapezoid candidates, but includes double-counting of parallelograms

        Why parallelograms are double-counted:
        - A parallelogram has 2 pairs of parallel sides
        - When we count "pairs of parallel edges", we count each parallelogram twice:
        * Once for the first pair of parallel sides
        * Once for the second pair of parallel sides

        Detecting parallelograms:
        - For 4 points to form a parallelogram, their diagonals must bisect each other
        - Two edges that share the same midpoint represent the diagonals of a parallelogram
        - Group edges by midpoint, then by slope
        - Count pairs of edges with same midpoint but different slopes

        Formula: Trapezoids = (Parallel edge pairs on different lines) - (Parallelograms)

        Implementation details:
        - Use floating point for slopes/intercepts (works for this problem's constraints)
        - For midpoint: use (x1+x2)*10000 + (y1+y2) as unique hash to avoid floating point
        - Count pairs incrementally: for each new count, multiply by running total
        This computes sum(count[i] * count[j]) for all i < j efficiently

        Time Complexity: O(n²) to generate edges + O(n²) to count pairs
        Space Complexity: O(n²) to store edge groupings
        '''
        inf = 10**9 + 7

        def get_slope(x1, y1, x2, y2):
            dx, dy = x1 - x2, y1 - y2
            if x1 == x2:
                return inf
            return dy / dx

        def get_intercept(x1, y1, x2, y2):
            dx, dy = x1 - x2, y1 - y2
            if x1 == x2:
                return x1

            return (y1 * dx - x1 * dy) / dx

        n = len(points)
        res = 0
        slope_to_intercepts = defaultdict(list)
        mid_to_slopes = defaultdict(list)

        # Generate all edges and group them
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                slope = get_slope(x1, y1, x2, y2)
                intercept = get_intercept(x1, y1, x2, y2)
                slope_to_intercepts[slope].append(intercept)

                mid = (x1 + x2) * 10000 + (y1 + y2)
                mid_to_slopes[mid].append(slope)

        # Count trapezoid candidates (pairs of parallel edges on different lines)
        for intercepts in slope_to_intercepts.values():
            if len(intercepts) == 1:
                continue
            intercept_counts = defaultdict(int)
            for intercept in intercepts:
                intercept_counts[intercept] += 1

            total_sum = 0
            for count in intercept_counts.values():
                res += total_sum * count
                total_sum += count

        # Count and subtract parallelograms (double-counted above)
        for slopes in mid_to_slopes.values():
            if len(slopes) == 1:
                continue

            slope_counts = defaultdict(int)
            for slope in slopes:
                slope_counts[slope] += 1

            total_sum = 0
            for count in slope_counts.values():
                res -= total_sum * count
                total_sum += count

        return res


sol = Solution()
print(f'output: {sol.countTrapezoids([[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]])}, expected: 2')
print(f'output: {sol.countTrapezoids([[0, 0], [1, 0], [0, 1], [2, 1]])}, expected: 1')
