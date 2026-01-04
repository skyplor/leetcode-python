class FourDivisors {

    public int sumFourDivisors(int[] nums) {
        int total = 0;
        for (int n : nums) {
            int tempRunningTotal = 0;
            int count = 0;
            for (int i = 1; i * i <= n; i++) {
                if (n % i == 0) {
                    if (i != n / i) {
                        count += 2;
                        tempRunningTotal += i + n / i;
                    } else {
                        count++;
                        tempRunningTotal += i;
                    }
                }

                if (count > 4) {
                    break;
                }
            }
            if (count == 4) {
                total += tempRunningTotal;
            }
        }
        return total;
    }

    public static void main(String[] args) {
        FourDivisors sol = new FourDivisors();
        System.out.println("Output: " + sol.sumFourDivisors(new int[] { 21, 4, 7 }) + ", expected: 32");
        System.out.println("Output: " + sol.sumFourDivisors(new int[] { 21, 21 }) + ", expected: 64");
        System.out.println("Output: " + sol.sumFourDivisors(new int[] { 1, 2, 3, 4, 5 }) + ", expected: 0");
    }
}
