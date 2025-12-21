class MinimumOperationsToMakeArraySumDivisibleByK {
    public int minOperations(int[] nums, int k) {
        int total = 0;
        for (int num : nums) {
            total += num;
        }
        return total % k;
    }
  
    public static void main(String[] args) {
        MinimumOperationsToMakeArraySumDivisibleByK sol = new MinimumOperationsToMakeArraySumDivisibleByK();
        System.out.println("Output: " + sol.minOperations(new int[]{3, 9, 7}, 5) + ", expected: 4");
        System.out.println("Output: " + sol.minOperations(new int[]{4, 1, 3}, 4) + ", expected: 0");
        System.out.println("Output: " + sol.minOperations(new int[]{3, 2}, 6) + ", expected: 5");
    }
}
