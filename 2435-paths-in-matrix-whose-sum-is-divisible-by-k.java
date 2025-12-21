class PathsInMatrixWhoseSumIsDivisibleByK {
    public int numberOfPaths(int[][] grid, int k) {
        double MOD = Math.pow(10, 9) + 7;
        int ROWS = grid.length, COLS = grid[0].length;
        int[][][] cache = new int[ROWS + 1][COLS + 1][k];

        for (int row = ROWS - 1; row >= 0; row--) {
            for (int col = COLS - 1; col >= 0; col--) {
                for (int remainder = 0; remainder < k; remainder++) {
                    if (row == ROWS - 1 && col == COLS - 1) {
                        if ((remainder + grid[row][col]) % k == 0) {
                            cache[row][col][remainder] = 1;
                        } else {
                            cache[row][col][remainder] = 0;
                        }
                        continue;
                    }
                    int newRemainder = (remainder + grid[row][col]) % k;
                    cache[row][col][remainder] = (int) ((cache[row + 1][col][newRemainder] % MOD +
                            cache[row][col + 1][newRemainder] % MOD) % MOD);
                }
            }
        }
        return cache[0][0][0];
    }

    public static void main(String[] args) {
        PathsInMatrixWhoseSumIsDivisibleByK sol = new PathsInMatrixWhoseSumIsDivisibleByK();
        System.out.println("Output: " + sol.numberOfPaths(new int[][] { { 5, 2, 4 }, { 3, 0, 5 }, { 0, 7, 2 } }, 3) + ", expected: 2");
        System.out.println("Output: " + sol.numberOfPaths(new int[][] { { 0, 0 } }, 5) + ", expected: 1");
        System.out.println("Output: " + sol.numberOfPaths(new int[][]  {{7,3,4,9},{2,3,6,2},{2,3,7,0}}, 1) + ", expected: 10");

    }
}
