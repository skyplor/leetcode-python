import java.util.*;

class AdjacentIncreasingSubarraysDetectionIISolution1 {

    public int binarySearch(int start, int end, List<Integer> nums) {
        while (start <= end) {
            int k = start + (end - start) / 2;
            boolean isValid = checkValid(nums, k);
            if (isValid) {
                start = k + 1;
            } else {
                end = k - 1;
            }
        }
        return end;
    }

    public boolean checkValid(List<Integer> nums, int k) {
        int first = 1;
        int second = k + 1;
        int n = nums.size();
        if (k == 1) {
            return n >= 2;
        }

        int counter = 0;
        while (second < n) {
            if (nums.get(first - 1) < nums.get(first) && nums.get(second - 1) < nums.get(second)) {
                counter++;
                if (counter == k - 1) {
                    return true;
                }
            } else {
                counter = 0;
            }
            first++;
            second++;
        }
        return false;
    }

    public int maxIncreasingSubarrays(List<Integer> nums) {
        return binarySearch(1, (int) Math.ceil(nums.size() / 2), nums);
    }

    public static void main(String[] args) {
        AdjacentIncreasingSubarraysDetectionIISolution1 sol = new AdjacentIncreasingSubarraysDetectionIISolution1();
        System.out.println(String.format("Output: %d, expected: %d",
                sol.maxIncreasingSubarrays(Arrays.asList(2, 5, 7, 8, 9, 2, 3, 4, 3, 1)), 3));
    }
}
