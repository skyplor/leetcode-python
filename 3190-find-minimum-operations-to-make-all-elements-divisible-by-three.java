class FindMinimumOperationsToMakeAllElementsDivisibleByThree {

    public int minimumOperations(int[] nums) {
        int res = 0;
        for (int num : nums) {
            if (num % 3 > 0) {
                res++;
            }
        }

        return res;
    }

    public static void main(String[] args) {
        FindMinimumOperationsToMakeAllElementsDivisibleByThree sol = new FindMinimumOperationsToMakeAllElementsDivisibleByThree();
        System.out.println("Output: " + sol.minimumOperations(new int[] { 1, 2, 3, 4 }) + ", expected: 3");
        System.out.println("Output: " + sol.minimumOperations(new int[] { 3, 6, 9 }) + ", expected: 0");
    }
}
