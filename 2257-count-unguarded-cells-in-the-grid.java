class CountUnguardedCellsInTheGrid {
    public int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
        int[][] grid = new int[m][n];
        for (int i = 0; i < guards.length; i++) {
            int r = guards[i][0], c = guards[i][1];
            grid[r][c] = 'G';
        }
        for (int i = 0; i < walls.length; i++) {
            int r = walls[i][0], c = walls[i][1];
            grid[r][c] = 'W';
        }

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 'G') {
                    markGuarded(grid, r, c, -1, 0, m, n);
                    markGuarded(grid, r, c, 1, 0, m, n);
                    markGuarded(grid, r, c, 0, -1, m, n);
                    markGuarded(grid, r, c, 0, 1, m, n);
                }
            }
        }

        int res = 0;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 0) {
                    res += 1;
                }
            }
        }

        return res;
    }

    private void markGuarded(int[][] grid, int r, int c, int dr, int dc, int m, int n) {
        int nr = r + dr, nc = c + dc;
        while (nr >= 0 && nr < m && nc >= 0 && nc < n) {
            if (grid[nr][nc] == 'G' || grid[nr][nc] == 'W') {
                break;
            }
            grid[nr][nc] = 1;
            nr += dr;
            nc += dc;
        }
    }

    public static void main(String[] args) {
        CountUnguardedCellsInTheGrid sol = new CountUnguardedCellsInTheGrid();
        System.out.println("Output: " + sol.countUnguarded(4, 6, new int[][] { { 0, 0 }, { 1, 1 }, { 2, 3 } },
                new int[][] { { 0, 1 }, { 2, 2 }, { 1, 4 } }) + ", expected: 7");
        System.out.println("Output: " + sol.countUnguarded(3, 3, new int[][] { { 1, 1 } },
                new int[][] { { 0, 1 }, { 1, 0 }, { 2, 1 }, { 1, 2 } }) + ", expected: 4");
    }
}
