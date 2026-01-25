import java.util.Arrays;

class MinimumDifferenceBetweenHighestAndLowestOfKScores {
    public int minimumDifference(int[] nums, int k) {
        int minDiff = Integer.MAX_VALUE;
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - k + 1; i++) {
            int currDiff = nums[i+k-1] - nums[i];
            if (currDiff < minDiff) {
                minDiff = currDiff;
            }
        }
        return minDiff;
    }

    public static void main(String[] args) {
        MinimumDifferenceBetweenHighestAndLowestOfKScores sol = new MinimumDifferenceBetweenHighestAndLowestOfKScores();
        System.out.println("Output: " + sol.minimumDifference(new int[] { 90 }, 1) + ", expected: 0");
        System.out.println("Output: " + sol.minimumDifference(new int[] { 9, 4, 1, 7 }, 2) + ", expected: 2");
    }
}