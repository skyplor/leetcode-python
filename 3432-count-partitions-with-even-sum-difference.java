class CountPartitionsWithEvenSumDifference {
    public int countPartitions(int[] nums) {
        int total = 0;
        for (int num : nums) {
            total += num;
        }
        int res = 0;
        int curTotal = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            curTotal += nums[i];
            if ((2 * curTotal - total) % 2 == 0) {
                res++;
            }
        }

        return res;
    }
  
    public static void main(String[] args) {
        CountPartitionsWithEvenSumDifference sol = new CountPartitionsWithEvenSumDifference();
        System.out.println("Output: " + sol.countPartitions(new int[]{10,10,3,7,6}) + ", expected: 4");
        System.out.println("Output: " + sol.countPartitions(new int[]{1,2,2}) + ", expected: 0");
        System.out.println("Output: " + sol.countPartitions(new int[]{2,4,6,8}) + ", expected: 3");
    }
}
