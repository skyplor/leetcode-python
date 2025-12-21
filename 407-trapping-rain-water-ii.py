from heapq import heappush, heappop


class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        '''
        We will first go through the borders of the heightMap.
        This allows us to narrow in on the cells that can hold the water as cells at the border will not be able to hold water
        We will utilise a min_heap to store each cell.
        At each stage,
            while the heap isn't empty,
            we pop the cell with the lowest height,
            calculate the amount of water it can hold (using the max_height - cur_height),
            add this amount of water into the result variable,
            then adding all its adjacent neighbours into the heap

        At the end, we return the result
        '''

        min_heap = []
        ROWS = len(heightMap)
        COLS = len(heightMap[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for row in range(ROWS):
            for col in range(COLS):
                if row in [0, ROWS - 1] or col in [0, COLS - 1]:
                    heappush(min_heap, (heightMap[row][col], row, col))
                    heightMap[row][col] = -1

        res = 0
        max_height = -1
        while min_heap:
            height, row, col = heappop(min_heap)
            max_height = max(max_height, height)
            res += max_height - height

            for dr, dc in DIRECTIONS:
                new_row, new_col = row + dr, col + dc
                if new_row not in range(ROWS) or new_col not in range(COLS) or heightMap[new_row][new_col] == -1:
                    continue
                heappush(
                    min_heap, (heightMap[new_row][new_col], new_row, new_col))
                heightMap[new_row][new_col] = -1

        return res


sol = Solution()
print(
    f'output: {sol.trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]])}, expected: 4')
print(
    f'output: {sol.trapRainWater([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]])}, expected: 10')
