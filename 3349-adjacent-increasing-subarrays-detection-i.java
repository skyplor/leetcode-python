import java.util.Arrays;
import java.util.List;

class AdjacentIncreasingSubarraysDetectionISolution {

    public boolean hasIncreasingSubarrays(List<Integer> nums, int k) {
        int n = nums.size();
        int first = 1, second = k + 1;
        if (k == 1) {
            return n >= 2;
        }
        int count = 0;

        while (second < n) {
            if (nums.get(first - 1) < nums.get(first) && nums.get(second - 1) < nums.get(second)) {
                count++;
                if (count == k - 1) {
                    return true;
                }
            } else {
                count = 0;
            }
            first++;
            second++;
        }

        return false;
    }

    public static void main(String[] args) {
        AdjacentIncreasingSubarraysDetectionISolution sol = new AdjacentIncreasingSubarraysDetectionISolution();
        System.out.println("Output: "
                + sol.hasIncreasingSubarrays(Arrays.asList(new Integer[] { 2, 5, 7, 8, 9, 2, 3, 4, 3, 1 }), 3)
                + ", expected: true");
        System.out.println("Output: "
                + sol.hasIncreasingSubarrays(Arrays.asList(new Integer[] { 1, 2, 3, 4, 4, 4, 4, 5, 6, 7 }), 5)
                + ", expected: false");
        System.out.println("Output: " + sol.hasIncreasingSubarrays(Arrays.asList(new Integer[] { -15, 19 }), 1)
                + ", expected: true");
        System.out
                .println("Output: " + sol.hasIncreasingSubarrays(Arrays.asList(new Integer[] { 5, 8, -2, -1 }), 2)
                        + ", expected: true");

    }

}
