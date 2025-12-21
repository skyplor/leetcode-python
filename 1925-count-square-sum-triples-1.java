class CountSquareSumTriples {
    public int countTriples(int n) {
        int res = 0;
        for (int n1 = 1; n1 <= n; n1++) {
            for (int n2 = n1 + 1; n2 <= n; n2++) {
                int total = n1*n1 + n2*n2;
                int c = (int) Math.sqrt(total);
                if (c <= n && c * c == total) {
                    res += 2;
                }
            }
        }
        return res;
    }
  
    public static void main(String[] args) {
        CountSquareSumTriples sol = new CountSquareSumTriples();
        System.out.println("Output: " + sol.countTriples(5) + ", expected: 2");
        System.out.println("Output: " + sol.countTriples(10) + ", expected: 4");
    }
}
