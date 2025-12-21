class CheckIfDigitsAreEqualInStringAfterOperationsI {

    public boolean hasSameDigits(String s) {
        int n = s.length();
        int[] digits = new int[n];

        for (int i = 0; i < n; i++)
            digits[i] = s.charAt(i) - '0';
        while (n > 1) {
            for (int i = 0; i < s.length() - 1; i++) {
                digits[i] = (digits[i] + digits[i + 1]) % 10;
            }
            n--;
            if (n == 2 && digits[0] == digits[1])
                return true;
        }

        return false;
    }

    public static void main(String[] args) {
        CheckIfDigitsAreEqualInStringAfterOperationsI sol = new CheckIfDigitsAreEqualInStringAfterOperationsI();
        System.out.println("Output: " + sol.hasSameDigits("3902") + ", expected: true");
        System.out.println("Output: " + sol.hasSameDigits("34789") + ", expected: false");
    }
}
