class CountTheNumberOfSubstringsWithDominantOnes {

    public int numberOfSubstrings(String s) {
        int right = 0;
        int n = s.length();
        int[] nextZero = new int[n];

        int prev = n;
        for (int i = n - 1; i > -1; i--) {
            nextZero[i] = prev;
            if (s.charAt(i) == '0') {
                prev = i;
            }
        }

        int res = 0;
        for (int left = 0; left < n; left++) {
            int zeroes = 0, ones = 0;
            if (s.charAt(left) == '0')
                zeroes = 1;
            right = left;

            while (zeroes * zeroes <= n) {
                int next = nextZero[right];
                ones = next - left - zeroes;
                if (ones >= zeroes * zeroes) {
                    res += Math.min(next - right, ones - (zeroes * zeroes) + 1);
                }
                zeroes++;
                right = next;
                if (right == n) {
                    break;
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        CountTheNumberOfSubstringsWithDominantOnes sol = new CountTheNumberOfSubstringsWithDominantOnes();
        System.out.println("Output: " + sol.numberOfSubstrings("00011") + ", expected: 5");
        System.out.println("Output: " + sol.numberOfSubstrings("101101") + ", expected: 16");
    }
}
