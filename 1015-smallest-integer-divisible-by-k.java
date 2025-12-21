class SmallestIntegerDivisibleByK {
    public int smallestRepunitDivByK(int k) {
        if (k % 2 == 0 || k % 5 == 0) {
            return -1;
        }

        int rem = 0;
        for (int i = 1; i <= k; i++) {
            rem = (rem * 10 + 1) % k;
            if (rem == 0) {
                return i;
            }
        }
        return -1;
    }
  
    public static void main(String[] args) {
        SmallestIntegerDivisibleByK sol = new SmallestIntegerDivisibleByK();
        System.out.println("Output: " + sol.smallestRepunitDivByK(1) + ", expected: 1");
        System.out.println("Output: " + sol.smallestRepunitDivByK(2) + ", expected: -1");
        System.out.println("Output: " + sol.smallestRepunitDivByK(3) + ", expected: 3");
    }
}
