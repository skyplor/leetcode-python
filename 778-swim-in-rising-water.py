from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        '''
        We can use a priority queue (min_heap) for this question.
        Specifically, we will traverse from (0, 0) by adding it into the min_heap
        Next, we pop it, mark as visited, and explore all 4 neighbours. The priority value is the max(current_max, curr_node_val), so we will also need to store the current_max
            - We will only push each neighbour in IF the neighbour hasn't been visited before
            
        If we pop a grid that is (n-1, n-1), we have found the answer and the result is the max(current_max, curr_node_val)
        '''
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        min_heap = [(grid[0][0], 0, 0)]
        visited.add((0, 0))
        while min_heap:
            curr_max, r, c = heappop(min_heap)
            if r == n - 1 and c == n - 1:
                return curr_max
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= n or nc >= n or (nr, nc) in visited:
                    continue
                visited.add((nr, nc))
                priority_val = max(curr_max, grid[nr][nc])
                heappush(min_heap, (priority_val, nr, nc))
                
        return -1
        


sol = Solution()
print(f'output: {sol.swimInWater([[0, 2], [1, 3]])}, expected: 3')
print(
    f'output: {sol.swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]])}, expected: 16')
