import java.util.*;

class MakeSumDivisiblebyP {
    public int minSubarray(int[] nums, int p) {
        long total = 0;
        for (int num : nums) {
            total += num;
        }
        if (total < p) {
            return -1;
        }
        long k = total % p;
        if (k == 0) {
            return 0;
        }
        int n = nums.length;
        int res = n;
        long currTotal = 0;
        Map<Long, Integer> prefixIndices = new HashMap<>();
        prefixIndices.put(0L, -1);

        for (int i = 0; i < n; i++) {
            currTotal = (currTotal + nums[i]) % p;
            long target = (currTotal - k + p) % p;
            if (prefixIndices.containsKey(target)) {
                res = Math.min(res, i - prefixIndices.get(target));
            }
            prefixIndices.put(currTotal, i);
        }

        return res == n ? -1 : res;
    }

    public static void main(String[] args) {
        MakeSumDivisiblebyP sol = new MakeSumDivisiblebyP();
        System.out.println("Output: " + sol.minSubarray(new int[]{3, 1, 4, 2}, 6) + ", expected: 1");
        System.out.println("Output: " + sol.minSubarray(new int[]{6, 3, 5, 2}, 9) + ", expected: 2");
        System.out.println("Output: " + sol.minSubarray(new int[]{1, 2, 3}, 3) + ", expected: 0");
    }
}
