class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        '''
        We first generate the grid and add in those guards and walls
        We go through each cell, 
            - if encounter a G, using DFS, we go all 4 directions and continue to mark all cells that are empty and in the range of this cell to -1 until we hit a W or G
            - if encounter a W, continue

        After marking, we go through each cell again and count those cells that are unmarked
        '''
        grid = [[None] * n for _ in range(m)]

        def mark_guarded(r: int, c: int, dr: int, dc: int):
            nr, nc = r + dr, c + dc
            while 0 <= nr < m and 0 <= nc < n:
                if grid[nr][nc] in ['G', 'W']:
                    break
                grid[nr][nc] = 1
                nr += dr
                nc += dc

        for r, c in guards:
            grid[r][c] = 'G'

        for r, c in walls:
            grid[r][c] = 'W'

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 'G':
                    mark_guarded(r, c, -1, 0)
                    mark_guarded(r, c, 1, 0)
                    mark_guarded(r, c, 0, -1)
                    mark_guarded(r, c, 0, 1)

        res = 0
        for r in range(m):
            for c in range(n):
                if not grid[r][c]:
                    res += 1

        return res


sol = Solution()
m = 4
n = 6
guards = [[0, 0], [1, 1], [2, 3]]
walls = [[0, 1], [2, 2], [1, 4]]
print(f'output: {sol.countUnguarded(m, n, guards, walls)}, expected: 7')
m = 3
n = 3
guards = [[1, 1]]
walls = [[0, 1], [1, 0], [2, 1], [1, 2]]
print(f'output: {sol.countUnguarded(m, n, guards, walls)}, expected: 4')
