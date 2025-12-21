class SmallestNumberWithAllSetBits {
    public int smallestNumber(int n) {
        int res = 1;
        while (res < n) {
            res <<= 1;
            res += 1;
        }

        return res;
    }
  
    public static void main(String[] args) {
        SmallestNumberWithAllSetBits sol = new SmallestNumberWithAllSetBits();
        System.out.println("Output: " + sol.smallestNumber(5) + ", expected: 7");
        System.out.println("Output: " + sol.smallestNumber(10) + ", expected: 15");
        System.out.println("Output: " + sol.smallestNumber(3) + ", expected: 3");
    }
}
