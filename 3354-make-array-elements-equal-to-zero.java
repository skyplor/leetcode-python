import java.util.*;

class MakeArrayElementsEqualToZero {
    public int countValidSelections(int[] nums) {
        List<Integer> zeroIndices = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                zeroIndices.add(i);
            }
        }

        int res = 0;
        for (Integer idx : zeroIndices) {
            int left = 0, right = 0;
            for (int j = 0; j < nums.length; j++) {
                if (j < idx) {
                    left += nums[j];
                } else if (j > idx) {
                    right += nums[j];
                }
            }
            if (left == right) {
                res += 2;
            } else if (Math.abs(left - right) == 1) {
                res += 1;
            }
        }
        return res;
    }
    public static void main(String[] args) {
        MakeArrayElementsEqualToZero sol = new MakeArrayElementsEqualToZero();
        System.out.println("Output: " + sol.countValidSelections(new int[] {1, 0, 2, 0, 3}) + ", expected: 2");
        System.out.println("Output: " + sol.countValidSelections(new int[] {2, 3, 4, 0, 4, 1, 0}) + ", expected: 0");
    }
}
