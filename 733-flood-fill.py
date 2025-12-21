from typing import List
from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''
        using BFS, we have a queue. We also need a seen hash to mark the cell as visited to prevent revisiting, in each iteration,
          we popleft from the queue and then change the pixel value
          next, we mark the neighbours as visited and enqueue all the neighbours IF the neighbour shares the same pixel value

        we then return the same image back
        '''
        seen = set()
        queue = deque()
        ROW = len(image)
        COL = len(image[0])
        value = image[sr][sc]

        seen.add((sr, sc))
        queue.append((sr, sc))
        while queue:
            cur_r, cur_c = queue.popleft()
            image[cur_r][cur_c] = color

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                new_r, new_c = cur_r + dr, cur_c + dc
                if (new_r in range(ROW) and
                    new_c in range(COL) and
                    (new_r, new_c) not in seen and
                        image[new_r][new_c] == value):
                    seen.add((new_r, new_c))
                    queue.append((new_r, new_c))

        return image


sol = Solution()
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1
# sc = 1
# color = 2
image = [[0, 0, 0], [0, 0, 0]]
sr = 0
sc = 0
color = 0
output = sol.floodFill(image, sr, sc, color)
print(f'output: {output}')
