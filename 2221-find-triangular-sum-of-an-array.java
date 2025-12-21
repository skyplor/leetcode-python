class FindTriangularSumOfArray {
    public int triangularSum(int[] nums) {
        if (nums.length == 1) return nums[0];
        for (int i = nums.length - 1; i >= 0; i--) {
            for (int j = 0; j < i; j++) {
                nums[j] = (nums[j] + nums[j+1]) % 10;
            }
        }
        return nums[0];
    }
    public static void main(String[] args) {
        FindTriangularSumOfArray sol = new FindTriangularSumOfArray();
        System.out.println("output: " + sol.triangularSum(new int[]{1,2,3,4,5}) + ", expected: 8");
        System.out.println("output: " + sol.triangularSum(new int[]{5}) + ", expected: 5");
    }
}
