class OnesAndZeroes {

    public int findMaxForm(String[] strs, int m, int n) {

        int[][] dp = new int[m + 1][n + 1];
        for (String s : strs) {

            int curOnes = (int) s.chars().filter(c -> c == '1').count(), curZeros = s.length() - curOnes;
            for (int zeros = m; zeros > curZeros - 1; zeros--) {
                for (int ones = n; ones > curOnes - 1; ones--) {
                    dp[zeros][ones] = Math.max(dp[zeros][ones], 1 + dp[zeros - curZeros][ones - curOnes]);
                }
            }

        }

        return dp[m][n];
    }

    public static void main(String[] args) {
        OnesAndZeroes sol = new OnesAndZeroes();
        System.out.println(
                "Output: " + sol.findMaxForm(new String[] { "10", "0001", "111001", "1", "0" }, 5, 3) + " expected: 4");
        System.out.println("Output: " + sol.findMaxForm(new String[] { "10", "0", "1" }, 1, 1) + " expected: 2");
    }
}
