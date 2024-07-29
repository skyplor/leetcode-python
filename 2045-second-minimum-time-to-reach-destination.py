from typing import List
from collections import deque, defaultdict


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        '''
        2d array of minimum values. We will store 2 values in each cell
        Use "Floyd Warshall Algorithm" algorithm to find the minimum value for all pairs
        Then we get the res at graph[1][5] and get the 2nd value of the res
        using 3 loops
          - for k in range(n-1):
          -   for i in range(n-1):
          -     for j in range(n-1):
          -       first_min, next_min = graph[i][j]
          -       updated_first_min = first_min
          -       updated_next_min = next_min
          -       new_val = graph[i][k] + graph[k][j]
          -       if new_val < first_min:
          -         updated_first_min = new_val
          -         updated_next_min = first_min
          -       elif new_val > first_min and new_val < next_min:
          -         updated_next_min = new_val
          -       graph[i][j] = (updated_first_min, updated_next_min)

        traffic signal:
        - if current time // change % 2 == 0 means can continue to move
        - if current time // change % 2 == 1 means must stop until next green signal
          - The next green signal -> current time = math.ceil(current_time / change) * change
        '''
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        queue = deque([(1, 1)])
        dist1 = [-1] * (n + 1)
        dist2 = [-1] * (n + 1)
        dist1[1] = 0

        while queue:
            x, freq = queue.popleft()
            t = dist1[x] if freq == 1 else dist2[x]
            if (t // change) % 2:
                t = change * (t // change + 1) + time
            else:
                t += time
            for neighbor in adj[x]:
                if dist1[neighbor] == -1:
                    dist1[neighbor] = t
                    queue.append((neighbor, 1))
                elif dist2[neighbor] == -1 and dist1[neighbor] != t:
                    if neighbor == n:
                        return t
                    dist2[neighbor] = t
                    queue.append((neighbor, 2))
        return 0


sol = Solution()
n = 5
edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
time = 3
change = 5
print(f'output: {sol.secondMinimum(n, edges, time, change)}')
