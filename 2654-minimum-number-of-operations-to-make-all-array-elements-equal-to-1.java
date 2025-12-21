import java.util.Arrays;

class MinimumNumberOfOperationsToMakeAllArrayElementsEqualTo1 {
    public int minOperations(int[] nums) {
        int onesCount = 0;
        for (int n : nums) {
            if (n == 1) {
                onesCount++;
            }
        }
        if (onesCount > 0) {
            return nums.length - onesCount;
        }

        if (gcdMultiple(nums) > 1) {
            return -1;
        }

        for (int windowSize = 2; windowSize <= nums.length; windowSize++) {
            for (int start = 0; start < nums.length - windowSize + 1; start++) {
                int divisor = gcdMultiple(Arrays.copyOfRange(nums, start, start + windowSize));
                if (divisor == 1) {
                    return windowSize + nums.length - 2;
                }
            }
        }
        return -1;
    }

    public int gcdMultiple(int[] numbers) {
        int result = numbers[0];
        for (int i = 1; i < numbers.length; i++) {
            result = gcd(result, numbers[i]);
            if (result == 1) {
                return result;
            }
        }
        return result;
    }

    public int gcd(int n1, int n2) {
        int small = n1, large = n2;
        if (n1 > n2) {
            small = n2;
            large = n1;
        }
        int remainder = large % small;
        while (remainder > 0) {
            large = small;
            small = remainder;
            remainder = large % small;
        }
        return small;
    }
  
    public static void main(String[] args) {
        MinimumNumberOfOperationsToMakeAllArrayElementsEqualTo1 sol = new MinimumNumberOfOperationsToMakeAllArrayElementsEqualTo1();
        System.out.println("Output: " + sol.minOperations(new int[] {2, 6, 3, 4}) + ", expected: 4");
        System.out.println("Output: " + sol.minOperations(new int[] {2, 10, 6, 14}) + ", expected: -1");
    }
}
