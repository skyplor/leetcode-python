class NumberOfLaserBeamsInABank {
    public int numberOfBeams(String[] bank) {
        int res = 0, prev = 0;
        for (int i = 0; i < bank.length; i++) {
            int cur = (int) bank[i].chars().filter(c -> c == '1').count();
            if (cur == 0) {
                continue;
            }
            res += cur * prev;
            prev = cur;
        }
        return res;
    }

    public static void main(String[] args) {
        NumberOfLaserBeamsInABank sol = new NumberOfLaserBeamsInABank();
        System.out.println("Output: " + sol.numberOfBeams(new String[] { "011001", "000000", "010100", "001000" })
                + ", expected: 8");
        System.out.println("Output: " + sol.numberOfBeams(new String[] { "000", "111", "000" }) + ", expected: 0");
    }
}
