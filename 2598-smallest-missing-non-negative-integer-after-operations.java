import java.util.*;

class SmallestMissingNonNegativeIntegerAfterOperationsSolution {
    public int findSmallestInteger(int[] nums, int value) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int i : nums) {
            int key = ((i % value) + value) % value;
            int cur = 0;
            if (count.containsKey(key)) {
                cur = count.get(key);
            }
            count.put(key, cur + 1);
        }

        for (int i = 0; i < nums.length; i++) {
            int mod = i % value;
            if (!count.containsKey(mod) || count.get(mod) == 0) {
                return i;
            }
            int cur = count.get(mod);
            count.put(mod, cur - 1);
        }

        return nums.length;
    }

    public static void main(String[] args) {
        SmallestMissingNonNegativeIntegerAfterOperationsSolution sol = new SmallestMissingNonNegativeIntegerAfterOperationsSolution();
        System.out.println(String.format("Output: %d, expected: 4",
                sol.findSmallestInteger(new int[] { 1, -10, 7, 13, 6, 8 }, 5)));
        System.out.println(String.format("Output: %d, expected: 2",
                sol.findSmallestInteger(new int[] { 1, -10, 7, 13, 6, 8 }, 7)));
        System.out.println(String.format("Output: %d, expected: 10",
                sol.findSmallestInteger(new int[] { 3, 0, 3, 2, 4, 2, 1, 1, 0, 4 }, 5)));
        System.out.println(String.format("Output: %d, expected: 4",
                sol.findSmallestInteger(new int[] { 0, 3, -7, 1 }, 3)));
    }

}
