import java.util.*;

class LC120TriangleSolution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            int val = triangle.get(n - 1).get(i);
            dp[i] = val;
        }

        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < i + 1; j++) {
                dp[j] = Math.min(dp[j], dp[j + 1]) + triangle.get(i).get(j);
            }
        }
        return dp[0];
    }

    public static void main(String[] args) {
        LC120TriangleSolution sol = new LC120TriangleSolution();
        System.out.println("Output: " + sol.minimumTotal(
                Arrays.asList(Arrays.asList(2), Arrays.asList(3, 4), Arrays.asList(6, 5, 7), Arrays.asList(4, 1, 8, 3)))
                + ", expected: 11");
    }
}
