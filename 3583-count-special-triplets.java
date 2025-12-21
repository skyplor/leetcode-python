import java.util.*;

class CountSpecialTriplets {
    public int specialTriplets(int[] nums) {
        long MOD = 1_000_000_007;
        int n = nums.length;
        long[] prefix = new long[n];
        Map<Integer, Long> count = new HashMap<>();
        for (int j = 0; j < n; j++) {
            int num = nums[j];
            prefix[j] = count.getOrDefault(num * 2, 0L);
            count.put(num, count.getOrDefault(num, 0L) + 1);
        }

        long res = 0;
        count = new HashMap<>();
        for (int j = n - 1; j > -1; j--) {
            int num = nums[j];
            long suffix = count.getOrDefault(num*2, 0L);
            res = (res + (prefix[j] * suffix)) % MOD;
            count.put(num, count.getOrDefault(num, 0L) + 1);
        }

        return (int) res;
    }
  
    public static void main(String[] args) {
        CountSpecialTriplets sol = new CountSpecialTriplets();
        System.out.println("Output: " + sol.specialTriplets(new int[]{6, 3, 6}) + ", expected: 1");
        System.out.println("Output: " + sol.specialTriplets(new int[]{0, 1, 0, 0}) + ", expected: 1");
        System.out.println("Output: " + sol.specialTriplets(new int[]{8, 4, 2, 8, 4}) + ", expected: 2");
    }
}
