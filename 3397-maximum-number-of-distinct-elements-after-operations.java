import java.util.Arrays;

class MaximumNumberOfDistinctElementsAfterOperationsSolution {

    public int maxDistinctElements(int[] nums, int k) {
        Arrays.sort(nums);
        int res = 0, prev = Integer.MIN_VALUE;
        for (int x : nums) {
            if (Math.max(x - k, prev + 1) <= x + k) {
                prev = Math.max(x - k, prev + 1);
                res++;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        MaximumNumberOfDistinctElementsAfterOperationsSolution sol = new MaximumNumberOfDistinctElementsAfterOperationsSolution();
        System.out.println("Output: " + sol.maxDistinctElements(new int[] { 1, 2, 2, 3, 3, 4 }, 2) + ", expected: 6");
    }

}
