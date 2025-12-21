class MaximumRunningTimeOfNComputers {

    public long maxRunTime(int n, int[] batteries) {
        long left = 1, right = 0;
        for (int b : batteries) {
            right += b;
        }
        right /= n;

        while (left < right) {
            long mid = left + (right - left + 1) / 2;
            if (isAchievable(n, batteries, mid)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }

    private boolean isAchievable(int n, int[] batteries, long target) {
        long total = 0;
        for (int b : batteries) {
            total += Math.min(target, b);
        }
        return total >= target * n;
    }

    public static void main(String[] args) {
        MaximumRunningTimeOfNComputers sol = new MaximumRunningTimeOfNComputers();
        System.out.println("Output: " + sol.maxRunTime(2, new int[] { 3, 3, 3 }) + ", expected: 4");
        System.out.println("Output: " + sol.maxRunTime(2, new int[] { 1, 1, 1, 1 }) + ", expected: 2");
    }
}
