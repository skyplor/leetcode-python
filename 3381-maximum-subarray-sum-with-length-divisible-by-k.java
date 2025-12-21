class MaximumSubarraySumWithLengthDivisibleByK {
    public long maxSubarraySum(int[] nums, int k) {
        int n = nums.length;
        long[] prefixSum = new long[n+1];
        long[] minPrefix = new long[k];
        for (int i = 1; i < k; i++) {
            minPrefix[i] = Long.MAX_VALUE;
        }
        long res = Long.MIN_VALUE;

        for (int i = 1; i < n+1; i++) {
            prefixSum[i] = prefixSum[i-1] + nums[i-1];
            int offset = i % k;

            if (i >= k) {  // Only compute result after we have at least k elements
                res = Math.max(res, prefixSum[i] - minPrefix[offset]);
            }
            minPrefix[offset] = Math.min(minPrefix[offset], prefixSum[i]);
        }

        return res;
    }

    public static void main(String[] args) {
        MaximumSubarraySumWithLengthDivisibleByK sol = new MaximumSubarraySumWithLengthDivisibleByK();
        System.out.println("Output: " + sol.maxSubarraySum(new int[] { 1, 2 }, 1) + ", expected 3");
        System.out.println("Output: " + sol.maxSubarraySum(new int[] { -1, -2, -3, -4, -5 }, 4) + ", expected -10");
        System.out.println("Output: " + sol.maxSubarraySum(new int[] { -5, 1, 2, -3, 4 }, 2) + ", expected 4");
    }
}
