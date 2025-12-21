class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        '''
        Using difference array technique, we add the cells for each row separately by determining where is the starting and ending.
        To do this, we add 1 to the cell where the subquery starts, and deduct 1 to the cell right of where the subquery ends
        After that, we compute the prefix sum by going through each cell again and update the final value using matrix[r][c] = matrix[r][c] + matrix[r][c-1]
        '''
        matrix = [[0] * n for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2 + 1):
                matrix[r][c1] += 1
                if (c2+1 < n):
                    matrix[r][c2+1] -= 1

        for r in range(n):
            for c in range(1, n):
                matrix[r][c] += matrix[r][c-1]

        return matrix


sol = Solution()
print(
    f'output: {sol.rangeAddQueries(n=3, queries=[[1, 1, 2, 2], [0, 0, 1, 1]])}, expected: [[1,1,0],[1,2,1],[0,1,1]]')
print(
    f'output: {sol.rangeAddQueries(n=2, queries=[[0, 0, 1, 1]])}, expected: [[1,1],[1,1]]')
