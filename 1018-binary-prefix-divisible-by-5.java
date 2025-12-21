import java.util.*;

class BinaryPrefixDivisibleBy5 {
    public List<Boolean> prefixesDivBy5(int[] nums) {
        List<Boolean> res = new ArrayList<>();
        int cur = 0;
        for (int i = 0; i < nums.length; i++) {
            cur <<= 1;
            cur |= nums[i];
            cur %= 5; // we mod by 5 to prevent overflow
            res.add(cur % 5 == 0);
        }
        return res;
    }
  
    public static void main(String[] args) {
        BinaryPrefixDivisibleBy5 sol = new BinaryPrefixDivisibleBy5();
        System.out.println("Output: " + sol.prefixesDivBy5(new int[]{0, 1, 1}).toString() + ", expected: [true, false, false]");
        System.out.println("Output: " + sol.prefixesDivBy5(new int[]{1, 1, 1}).toString() + ", expected: [false, false, false]");
    }
}
