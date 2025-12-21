from typing import List
from heapq import heappop, heappush


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        We can use Prim's Algorithm to find the min cost.
        We will need a visited set to store all nodes that have been visited to prevent us from visiting them again
        Next, we will also need a heap, specifically min_heap to allow popping of the next minimum edge

        Main logic:
            - We will push the first point into heap (with the distance to it) e.g (2, 3) cost: 2, point: 3
            - While the heap isn't empty, we pop the minimum cost item, check if the point is already visited.
                - If yes, ignore and continue to pop again
                - Else, add to visited, add the cost, and using BFS, add all edges from this point into the min heap, calculating the distance on-the-fly
            - return the minimum cost
            
        This is a slight optimisation in the Prim's algorithm by adding caching to the already discovered distances for each point.
        We store the minimum distance discovered till now for a point and only add into heap IF the distance is shorter than what's stored in the cache.

        Complexity
        Time: O(n² log n)
        Space: O(n)
        '''
        def calculate_distance(p1, p2):
            (x1, y1), (x2, y2) = p1, p2
            return abs(x1-x2) + abs(y1-y2)

        visited = set()
        min_heap = []
        res = 0
        x0, y0 = points[0]
        cache = {(x0, y0): 0}
        heappush(min_heap, (0, (x0, y0)))
        while min_heap:
            distance, (x1, y1) = heappop(min_heap)
            if (x1, y1) in visited:
                continue
            res += distance
            visited.add((x1, y1))
            for x2, y2 in points:
                if (x2, y2) in visited:
                    continue
                next_distance = calculate_distance((x1, y1), (x2, y2))
                if next_distance < cache.get((x2, y2), float('inf')):
                    cache[(x2, y2)] = next_distance
                    heappush(min_heap, (next_distance, (x2, y2)))

        return res


sol = Solution()
points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
output = sol.minCostConnectPoints(points)
print(f'output: {output}')
