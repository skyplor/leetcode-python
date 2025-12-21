from typing import List


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        '''
        - Child 1 (starts at (0,0)): Has exactly one path along the diagonal (0,0) → (1,1) → ... → (n-1,n-1)
        - Child 2 (starts at (0,n-1)): Must reach near (n-1,n-1) while avoiding diagonal cells
        - Child 3 (starts at (n-1,0)): Must reach near (n-1,n-1) while avoiding diagonal cells

        We can partition the grid:
        - Child 1: Takes diagonal cells where row == col
        - Child 2: Takes upper triangle cells where row < col  
        - Child 3: Takes lower triangle cells where row > col

        This ensures no overlaps and allows independent optimization for each child.

        Solution Approach:
        1. Child 1: Simply sum all diagonal cells fruits[i][i]

        2. Child 2: Use layer-by-layer DP from (0,n-1) toward (n-2,n-1)
        - Valid moves: down-left [1,-1], down [1,0], down-right [1,1]
        - Only visit cells where row < col (upper triangle)
        - Stop at (n-2,n-1) which is adjacent to the final destination

        3. Child 3: Use layer-by-layer DP from (n-1,0) toward (n-1,n-2)  
        - Valid moves: up-right [-1,1], right [0,1], down-right [1,1]
        - Only visit cells where row > col (lower triangle)
        - Stop at (n-1,n-2) which is adjacent to the final destination

        Why this works:
        - Each child operates in their exclusive region
        - No coordination needed since regions don't overlap
        - Child 2 and 3 end adjacent to (n-1,n-1), effectively "reaching" the destination
        - Time complexity: O(n²) per child instead of O(n³) for full coordination
        - Space complexity: O(n) for layer tracking instead of O(n³) for 3D DP

        Implementation:
        - Use current_layer dictionary to track reachable positions and their maximum fruit values
        - Process exactly n-2 steps (not n-1) since we end one cell away from final destination
        - Take max value from all possible previous positions when building next layer
        '''

        def is_valid_for_child_2(row: int, col: int) -> bool:
            return row < col

        def is_valid_for_child_3(row: int, col: int) -> bool:
            return col < row

        n = len(fruits)
        res = sum(fruits[i][i] for i in range(n))

        child_2_directions = [[1, -1], [1, 0], [1, 1]]
        child_3_directions = [[-1, 1], [0, 1], [1, 1]]

        current_layer = {(0, n-1): fruits[0][n-1]}

        # # child_2, start from (0, n-1)
        for _ in range(n-2):
            next_layer = {}
            for (r, c), value in current_layer.items():
                for dr, dc in child_2_directions:
                    next_row, next_col = r + dr, c + dc
                    if next_row in range(n) and next_col in range(n) and is_valid_for_child_2(next_row, next_col):
                        next_layer[(next_row, next_col)] = max(next_layer.get(
                            (next_row, next_col), 0), value + fruits[next_row][next_col])
            current_layer = next_layer

        child_2_max = current_layer.get((n-2, n-1), 0)

        current_layer = {(n-1, 0): fruits[n-1][0]}

        # child_3, start from (n-1, 0)
        for _ in range(n-2):
            next_layer = {}
            for (r, c), value in current_layer.items():
                for dr, dc in child_3_directions:
                    next_row, next_col = r + dr, c + dc
                    if next_row in range(n) and next_col in range(n) and is_valid_for_child_3(next_row, next_col):
                        next_layer[(next_row, next_col)] = max(next_layer.get(
                            (next_row, next_col), 0), value + fruits[next_row][next_col])
            current_layer = next_layer

        child_3_max = current_layer.get((n-1, n-2), 0)
        res += child_2_max + child_3_max

        return res


sol = Solution()
fruits = [[1, 2, 3, 4], [5, 6, 8, 7], [9, 10, 11, 12], [13, 14, 15, 16]]
output = sol.maxCollectedFruits(fruits)
print(f'output: {output}')
