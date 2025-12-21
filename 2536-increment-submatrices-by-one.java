import java.util.Arrays;

class IncrementSubmatricesByOne {
    public int[][] rangeAddQueries(int n, int[][] queries) {
        int[][] matrix = new int[n][n];
        for (int[] query : queries) {
            int r1 = query[0], c1 = query[1], r2 = query[2], c2 = query[3];
            for (int r = r1; r <= r2; r++) {
                matrix[r][c1] += 1;
                if (c2 + 1 < n) {
                    matrix[r][c2+1] -= 1;
                }
            }
        }

        for (int r = 0; r < n; r++) {
            for (int c = 1; c < n; c++) {
                matrix[r][c] += matrix[r][c-1];
            }
        }

        return matrix;
    }

    public static void main(String[] args) {
        IncrementSubmatricesByOne sol = new IncrementSubmatricesByOne();
        System.out.println("Output: " + Arrays.deepToString(sol.rangeAddQueries(3, new int[][] { { 1, 1, 2, 2 }, { 0, 0, 1, 1 } }))
                + ", expected: [[1,1,0],[1,2,1],[0,1,1]]");
        System.out.println(
                "Output: " + Arrays.deepToString(sol.rangeAddQueries(2, new int[][] { { 0, 0, 1, 1 } })) + ", expected: [[1,1],[1,1]]");
    }
}
