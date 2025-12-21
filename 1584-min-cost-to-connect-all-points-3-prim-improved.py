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
            
        This is a slight improvement from the previous Prim's algorithm by only calculating the edges on-the-fly so we don't need to pre-generate the edges, resulting in reduction in storage size

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
        heappush(min_heap, (0, points[0]))
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
                heappush(min_heap, (next_distance, (x2, y2)))

        return res


sol = Solution()
points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
output = sol.minCostConnectPoints(points)
print(f'output: {output}')
