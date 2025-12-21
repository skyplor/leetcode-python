class MaximumNumberOfOperationsToMoveOnesToTheEnd {
  
    public int maxOperations(String s) {
        int n = s.length();
        int i = n - 1;
        int totalOps = 0, totalGaps = 0;
        while (i >= 0) {
            if (s.charAt(i) == '1') {
                totalOps += totalGaps;
                i--;
                continue;
            }

            totalGaps++;
            while (i >= 0 && s.charAt(i) == '0') {
                i--;
            }
        }

        return totalOps;
    }
    public static void main(String[] args) {
        MaximumNumberOfOperationsToMoveOnesToTheEnd sol = new MaximumNumberOfOperationsToMoveOnesToTheEnd();
        System.out.println("Output: " + sol.maxOperations("1001101") + ", expected: 4");
        System.out.println("Output: " + sol.maxOperations("00111") + ", expected: 0");
    }
}
