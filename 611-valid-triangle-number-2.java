import java.util.Arrays;

class ValidTriangleNumberSolution {
    /**
     * For a valid triangle, sum of 2 sides must be larger than 3rd side,
     * i.e. a + b > c
     * We can first sort the nums list,
     * then we have a loop that goes through each number,
     * setting that as `c`.
     * Next, we use 2 pointers to find all valid pairs of `a` and `b` that is
     * greater than `c`.
     */

    public int triangleNumber(int[] nums) {
        Arrays.sort(nums);
        int result = 0;

        for (int c = 0; c < nums.length; c++) {
            int a = 0, b = c - 1;
            while (a < b) {
                if (nums[a] + nums[b] <= nums[c]) {
                    a++;
                } else {
                    // if the sum is greater, then all pairs from a, a+1... to b will work, so we
                    // need to get all triangles between b and a
                    result += b - a;
                    b--;
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        ValidTriangleNumberSolution sol = new ValidTriangleNumberSolution();
        System.out.println("Output: " + sol.triangleNumber(new int[] { 2, 2, 3, 4 }) + ", expected: 3");
        System.out.println("Output: " + sol.triangleNumber(new int[] { 4, 2, 3, 4 }) + ", expected: 4");
    }

}
