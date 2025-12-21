from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
  def minCostConnectPoints(self, points: List[List[int]]) -> int:
    '''
    Minimum spanning tree using Prim's Algo
    Connect all nodes without forming a cycle
      - we will need (n-1) edges
      
    we will need a cost variable
      
    Step 1: we will first create an adjacency list that contains edges from each point to all other points
    Step 2: start at any single node, start BFS, with VISITED set, and Frontier (min heap)
    '''
    adjList = defaultdict(list)
    n = len(points)
    for i in range(n):
      x1, y1 = points[i]
      for j in range(i + 1, n):
        x2, y2 = points[j]
        distance = abs(x1 - x2) + abs(y1 - y2)
        adjList[i].append([distance, j])
        adjList[j].append([distance, i])

    # Prim's
    cost = 0
    visited = set()
    minHeap = [[0, 0]] # [cost, point]
      
    def bfs():
      nonlocal cost

      while len(visited) < n:
        minDistance, i = heappop(minHeap)
        if i in visited:
          continue
        visited.add(i)
        cost += minDistance
        edges = adjList[i]
        for distance, pointIndex in edges:
          if pointIndex not in visited:
            heappush(minHeap, [distance, pointIndex])

    bfs()

    return cost
  
sol = Solution()
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(f'output: {sol.minCostConnectPoints(points)}')