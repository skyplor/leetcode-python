from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        We can use Union-Find + Kruskal's Algorithm to find the min cost.
        We will first create an edge from each point to all other points using 2 for loops. We calculate the cost in the process and add these into a list
        Next, we sort the list by the weight/cost and then iterate through it
        In each iteration, we use union-find to decide if we should include or exclude the edges, and if yes, we add the cost to the result
        
        Complexity
        Time: O(n² log n)
        Space: O(n²)
        '''
        res = 0
        parents = {}  # e.g {(0, 0): (0, 0)} tuple:tuple
        sizes = {}  # e.g {(0, 0): 1} tuple:int
        edges = []

        def calculate_distance(p1: List[int], p2: List[int]) -> int:
            x1, y1 = p1
            x2, y2 = p2
            return abs(x1 - x2) + abs(y1 - y2)

        def find(n1: List[int]) -> List[int]:
            x1, y1 = n1
            res = (x1, y1)
            while parents[res] != res:
                parents[res] = parents[parents[res]]
                res = parents[res]

            return res

        def union(n1: List[int], n2: List[int]):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if sizes[p1] > sizes[p2]:
                parents[p2] = p1
                sizes[p1] += sizes[p2]
            else:
                parents[p1] = p2
                sizes[p2] += sizes[p1]

            return True

        # initialise
        for x1, y1 in points:
            parents[(x1, y1)] = (x1, y1)
            sizes[(x1, y1)] = 1

        # generate edges
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                p1, p2 = points[i], points[j]
                cost = calculate_distance(p1, p2)
                edges.append([cost, p1, p2])

        # perform kruskal algorithm using union-find
        edges.sort(key=lambda x: x[0])

        for cost, n1, n2 in edges:
            if union(n1, n2):
                res += cost

        return res


sol = Solution()
points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
output = sol.minCostConnectPoints(points)
print(f'output: {output}')
