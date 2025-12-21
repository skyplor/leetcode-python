class GreatestSumDivisibleByThree {
    public int maxSumDivThree(int[] nums) {
        int[] dp = {0, -Integer.MAX_VALUE, -Integer.MAX_VALUE};
        for (int i = nums.length - 1; i >= 0; i--) {
            int[] newDp = {0, 0, 0};
            for (int r = 0; r < 3; r++) {
                newDp[r] = Math.max(nums[i] + dp[((r - nums[i]) % 3 + 3) % 3], dp[r]);
            }
            dp = newDp;
        }

        return dp[0];
    }

    public static void main(String[] args) {
        GreatestSumDivisibleByThree sol = new GreatestSumDivisibleByThree();
        System.out.println("Output: " + sol.maxSumDivThree(new int[] { 3, 6, 5, 1, 8 }) + ", expected: 18");
        System.out.println("Output: " + sol.maxSumDivThree(new int[] { 4 }) + ", expected: 0");
        System.out.println("Output: " + sol.maxSumDivThree(new int[] { 1, 2, 3, 4, 4 }) + ", expected: 12");
    }
}