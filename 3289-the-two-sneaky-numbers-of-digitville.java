import java.util.*;

class TheTwoSneakyNumbersOfDigitville {
    public int[] getSneakyNumbers(int[] nums) {
        int[] results = new int[2];
        int idx = 0;
        Set<Integer> seen = new HashSet<>();
        for (int i : nums) {
            if (seen.contains(i)) {
                results[idx++] = i;
            } else {
                seen.add(i);
            }
        }
        return results;
    }

    public static void main(String[] args) {
        TheTwoSneakyNumbersOfDigitville sol = new TheTwoSneakyNumbersOfDigitville();
        System.out.println("Output: " + sol.getSneakyNumbers(new int[] { 0, 1, 1, 0 }) + ", expected: [0, 1]");
        System.out.println("Output: " + sol.getSneakyNumbers(new int[] { 0, 3, 2, 1, 3, 2 }) + ", expected: [2, 3]");
        System.out.println("Output: " + sol.getSneakyNumbers(new int[] { 7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2 })
                + ", expected: [4, 5]");
    }
}
