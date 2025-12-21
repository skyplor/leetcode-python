from typing import List


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        '''
        Since each child has to make exactly `n-1` moves, that means the child at (0, 0) (child_1) will only have 1 path, i.e (i, j) -> (i + 1, j + 1) ... (n-1, n-1)
        For child at (0, n-1) (child_2):
            - if row < n-2, each time will have 2 choices (i+1, n-1) or (i+1, n-2)
            - else, will only have 1 choice, (n-1, n-1)
        For child at (n-1, 0) (child_3):
            - if col < n-2, each time will have 2 choices (n-1, j+1) or (n-2, j+1)
            - else, will only have 1 choice, (n-1, n-1)

        We can use a 3-D DP to approach this problem by keeping track of the maximum fruits taken at each state.
        We can have dp[move][row][col] where move will increment by 1 each time
            - child_1 will always be moving dp[move][move][move]

        For the other 2 children, we will need to determine the invalid cells.
            - if a cell is (i, i), that means it's the diagonal cell and it would have been taken by child_1, so this is invalid
            - if when we reach a cell, the remaining move is 0 and the cell is not (n-1, n-1), then it is invalid

        For each valid cell:
            1. we need to determine the previous possible cells (this depends on whether we are calculating for child_2 or child_3)
                - child_2
                    - dp[move-1][row-1][col]
                    - dp[move-1][row-1][col-1]
                    - dp[move-1][row-1][col+1]
                - child_3
                    - dp[move-1][row][col-1]
                    - dp[move-1][row-1][col-1]
                    - dp[move-1][row+1][col-1]
            2. then we get the max by taking the max of the previous possible cells
                - child_2: max(dp[move-1][row-1][col], dp[move-1][row-1][col-1], dp[move-1][row-1][col+1])
                - child_3: max(dp[move-1][row][col-1], dp[move-1][row-1][col-1], dp[move-1][row+1][col-1])
            3. then adding it to the current cell

        At the end we return dp[0][n-1][n-1] by summing up
        '''
        n = len(fruits)
        
        res = sum(fruits[i][i] for i in range(n))

        def dp():
            grid = [[0] * n for _ in range(n)]
            grid[0][n-1] = fruits[0][n-1]
            
            for i in range(1, n-1):
                for j in range(max(i + 1, n - 1 - i), n):
                    best = grid[i - 1][j]
                    best = max(best, grid[i - 1][j - 1])
                    if j < n - 1: best = max(best, grid[i - 1][j + 1])
                    grid[i][j] = best + fruits[i][j]
                    
            return grid[n - 2][n - 1]
        
        res += dp()
        
        for i in range(n):
            for j in range(i):
                fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]
                
        res += dp()
        
        return res


sol = Solution()
fruits = [[1, 2, 3, 4], [5, 6, 8, 7], [9, 10, 11, 12], [13, 14, 15, 16]]
output = sol.maxCollectedFruits(fruits)
print(f'output: {output}')
