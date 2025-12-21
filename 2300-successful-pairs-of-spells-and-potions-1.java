import java.util.*;

class SuccessfulPairsOfSpellsAndPotionsSolution1 {

    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int n = spells.length, m = potions.length;
        Arrays.sort(potions);
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            int idx = binarySearch(potions, 0, m, ((int) Math.ceil(success * 1.0 / spells[i])));
            result[i] = m - idx;
        }
        return result;
    }

    public int binarySearch(int[] potions, int left, int right, int target) {
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (potions[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    public static void main(String[] args) {
        SuccessfulPairsOfSpellsAndPotionsSolution1 sol = new SuccessfulPairsOfSpellsAndPotionsSolution1();
        System.out.println(
                "Output: " + Arrays.toString(sol.successfulPairs(new int[] { 5, 1, 3 }, new int[] { 1, 2, 3, 4, 5 }, 7))
                        + ", expected: [4,0,3]");
        System.out.println(
                "Output: " + Arrays.toString(sol.successfulPairs(new int[] { 3, 1, 2 }, new int[] { 8, 5, 8 }, 16))
                        + ", expected: [2,0,2]");
    }
}
