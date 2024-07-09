from typing import List
from collections import defaultdict, deque
from operator import itemgetter
from heapq import heappush, heappop

class Solution:
  # def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
  #   '''
  #   Step 1: Build a adjacency list of the graph nodes, for the list, we sort it in ascending weights
  #   Step 2: retrieve the adjacency list of node K, add each of them into queue
  #   Step 3: We have a variable 'res' = 0. Using BFS, we load ALL neighbours. For each neighbour, if weight is not 0, we push each of them into the queue again, decrementing the weight by 1. Once all neighbours are processed, we increment res by 1.
  #   Step 4: if weight is 0, then we 'process' this node. We add this node into "visited" set to mark it as visited. We also add all its neighbours into the queue
  #   Step 4a: We check if this "visited" set's length == n. If yes, we have visited all nodes and we can return current 'res'
  #   '''
    
  #   sortedTimes = sorted(times, key = itemgetter(2) )
  #   adjList = defaultdict(list)
  #   for src,target,weight in sortedTimes:
  #     adjList[src].append((weight, target))
    
  #   res = 0
  #   visited = set([k])
  #   queue = deque()
  #   for edges in adjList[k]:
  #     queue.append(edges)
  #   while queue or len(visited) < n:
  #     for _ in range(len(queue)):
  #       weight,target = queue.popleft()
  #       if target in visited:
  #         continue
  #       if weight > 1:
  #         queue.append((weight - 1, target))
  #       else:
  #         # process node
  #         visited.add(target)

  #         for edges in adjList[target]:
  #           queue.append(edges)
  #     res += 1
      
  #   return res if len(visited) == n else -1
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
      '''
      Step 1: Build a adjacency list of the graph nodes, for the list, we sort it in ascending weights
      Step 2: retrieve the adjacency list of node K, add each of them into a minheap
      Step 3: We have a variable 'res' = 0. Using BFS, we pop from minheap. 
      Step 4: Then we 'process' this node if this node wasn't visited. We add this node into "visited" set to mark it as visited. We load ALL its neighbours. For each neighbour, we add the current weight to their weight and add this new edge into the minheap
      Step 5: We check if this "visited" set's length == n. If yes, we have visited all nodes and we can return current 'res'
      '''
    
      sortedTimes = sorted(times, key = itemgetter(2) )
      adjList = defaultdict(list)
      for src,target,weight in sortedTimes:
        adjList[src].append((weight, target))

      if not adjList[k]:
        return -1

      res = 0
      visited = set([k])
      minheap = []
      for edges in adjList[k]:
        heappush(minheap, edges)
      while minheap:
        w1,t1 = heappop(minheap)
        if t1 in visited:
          continue
        # process node
        visited.add(t1)
        res = max(w1, res)

        for w2, t2 in adjList[t1]:
          heappush(minheap, (w1 + w2, t2))

      return res if len(visited) == n else -1
        
  
sol = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
# times = [[1,2,1]]
# n = 2
# k = 1
# times = [[1,2,1]]
# n = 2
# k = 2
print(f'output: {sol.networkDelayTime(times, n, k)}')