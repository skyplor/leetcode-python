import java.util.Arrays;

class LargestParameterTriangleSolution {
    public int largestPerimeter(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0, j = nums.length - 1; i < j; i++, j--) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
        for (int i = 0; i < nums.length - 2; i++) {
            int a = nums[i+2];
            int b = nums[i+1];
            int c = nums[i];
            if (a + b > c) {
                return a + b + c;
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        LargestParameterTriangleSolution sol = new LargestParameterTriangleSolution();
        System.out.println("Output: " + sol.largestPerimeter(new int[] { 2, 1, 2 }) + ", expected: 5");
        System.out.println("Output: " + sol.largestPerimeter(new int[] { 1, 2, 1, 10 }) + ", expected: 0");
    }
}
