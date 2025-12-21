class MinimumOneBitOperationsToMakeIntegersZero {

    public int minimumOneBitOperations(int n) {
        int res = 0;
        while (n != 0) {
            res ^= n;
            n >>= 1;
        }

        return res;
    }
  
    public static void main(String[] args) {
        MinimumOneBitOperationsToMakeIntegersZero sol = new MinimumOneBitOperationsToMakeIntegersZero();
        System.out.println("Output: " + sol.minimumOneBitOperations(3) + ", expected: 2");
        System.out.println("Output: " + sol.minimumOneBitOperations(6) + ", expected: 4");
    }
}
