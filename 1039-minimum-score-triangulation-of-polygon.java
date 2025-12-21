class MinimumScoreTriangulationPolygonSolution {
    public int minScoreTriangulation(int[] values) {
        int n = values.length;
        int[][] dp = new int[n][n];
        for (int length = 3; length < n + 1; length++) {
            for (int i = 0; i < n - length + 1; i++) {
                int j = i + length - 1;
                dp[i][j] = Integer.MAX_VALUE;

                for (int k = i + 1; k < j; k++) {
                    int score = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j];
                    dp[i][j] = Math.min(dp[i][j], score);
                }
            }
        }

        return dp[0][n-1];
    }

    public static void main(String[] args) {
        MinimumScoreTriangulationPolygonSolution sol = new MinimumScoreTriangulationPolygonSolution();
        System.out.println("Output: " + sol.minScoreTriangulation(new int[] {1, 2, 3}) + ", expected: 6");
        System.out.println("Output: " + sol.minScoreTriangulation(new int[] {3, 7, 4, 5}) + ", expected: 144");
        System.out.println("Output: " + sol.minScoreTriangulation(new int[] {1, 3, 1, 4, 1, 5}) + ", expected: 13");
    }
}
