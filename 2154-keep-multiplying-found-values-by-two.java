import java.util.*;

class KeepMultiplyingFoundValuesByTwo {
    public int findFinalValue(int[] nums, int original) {
        Set<Integer> numsSet = new HashSet<>();
        for (int num : nums) {
            numsSet.add(num);
        }

        for (int i = 0; i <= nums.length; i++) {
            if (!numsSet.contains(original)) {
                break;
            }
            original *= 2;
        }
        return original;
    }
  
    public static void main(String[] args) {
        KeepMultiplyingFoundValuesByTwo sol = new KeepMultiplyingFoundValuesByTwo();
        System.out.println("Output: " + sol.findFinalValue(new int[]{5, 3, 6, 1, 12}, 3) + ", expected: 24");
        System.out.println("Output: " + sol.findFinalValue(new int[]{2, 7, 9}, 4) + ", expected: 4");
    }
}
