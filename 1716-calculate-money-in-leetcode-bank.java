class CalculateMoneyInLeetcodeBank {
    public int totalMoney(int n) {
        int result = 0, last = 0;
        for (int i = 1; i <= n; i++) {
            if (i % 7 == 1) {
                last = Math.max(1, last - 5);
                result += last;
            } else {
                last++;
                result += last;
            }
        }

        return result;
    }
    public static void main(String[] args) {
        CalculateMoneyInLeetcodeBank sol = new CalculateMoneyInLeetcodeBank();
        System.out.println("Output: " + sol.totalMoney(4) + ", expected: 10");
        System.out.println("Output: " + sol.totalMoney(10) + ", expected: 37");
        System.out.println("Output: " + sol.totalMoney(20) + ", expected: 96");
    }
}
