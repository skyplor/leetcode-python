class CountOddNumbersInAnIntervalRange {
    public int countOdds(int low, int high) {
        int length = high - low + 1;
        int res = length / 2;
        if (length % 2 == 1 && low % 2 == 1) {
            res++;
        }

        return res;
    }
  
    public static void main(String[] args) {
        CountOddNumbersInAnIntervalRange sol = new CountOddNumbersInAnIntervalRange();
        System.out.println("Output: " + sol.countOdds(3, 7) + ", expected: 3");
        System.out.println("Output: " + sol.countOdds(8, 10) + ", expected: 1");
        System.out.println("Output: " + sol.countOdds(21, 22) + ", expected: 1");
    }
}
