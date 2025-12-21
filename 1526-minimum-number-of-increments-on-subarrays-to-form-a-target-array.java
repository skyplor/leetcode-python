class MinimumNumberOfIncrementsOnSubarraysToFormATargetArray {
    public int minNumberOperations(int[] target) {
        int res = 0, prev = 0;
        for (int cur : target) {
            if (cur > prev) {
                res += cur - prev;
            }
            prev = cur;
        }
        return res;
    }

    public static void main(String[] args) {
        MinimumNumberOfIncrementsOnSubarraysToFormATargetArray sol = new MinimumNumberOfIncrementsOnSubarraysToFormATargetArray();
        System.out.println("Output: " + sol.minNumberOperations(new int[] { 1, 2, 3, 2, 1 }) + ", expected: 3");
        System.out.println("Output: " + sol.minNumberOperations(new int[] { 3, 1, 1, 2 }) + ", expected: 4");
        System.out.println("Output: " + sol.minNumberOperations(new int[] { 3, 1, 5, 4, 2 }) + ", expected: 7");
    }
}
