class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        '''
        Since we want to check if water can flow into each ocean and water can only flow from high to low.
        So we will do several dfs:
            1. left to right (water flowing back into pacific ocean)
            2. right to left (water flowing back into atlantic ocean)
            3. top to bottom (water flowing back into pacific ocean)
            4. bottom to top (water flowing back into atlantic ocean)

        Also, because water can flow from each cell to any other cell around it (top, bottom, left, right) as long as the height is lower,
        we will need to check through all 4 directions within each dfs search. If current cell's height is >= prev_height, then we continue to explore as this means water can flow back (we are checking in reverse)
        '''
        ROWS = len(heights)
        COLS = len(heights[0])
        atl, pac = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited: set, prev_height):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or heights[r][c] < prev_height:
                return
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visited, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pac, 0)
            dfs(r, COLS - 1, atl, 0)

        for c in range(COLS):
            dfs(0, c, pac, 0)
            dfs(ROWS - 1, c, atl, 0)

        result = list(atl & pac)
        result.sort()
        return result


sol = Solution()
print(
    f'output: {sol.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])}, expected: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]')
print(f'output: {sol.pacificAtlantic([[1]])}, expected: [[0, 0]]')
