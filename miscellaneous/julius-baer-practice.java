package miscellaneous;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class JuliusBaerPractice {

    public String sortDigitsDesc(String input) {
        if (input == null || input.trim().isEmpty()) {
            return "";
        }

        String digitsOnly = input.replaceAll("\\D", "");
        char[] digitsArr = digitsOnly.toCharArray();
        Arrays.sort(digitsArr);

        for (int left = 0, right = digitsArr.length - 1; left < right; left++, right--) {
            char temp = digitsArr[left];
            digitsArr[left] = digitsArr[right];
            digitsArr[right] = temp;
        }

        return new String(digitsArr);
    }

    public String sortDigitsAsc(String input) {
        if (input == null || input.trim().isEmpty()) {
            return "";
        }

        String digitsOnly = input.replaceAll("\\D", "");
        char[] digitsArr = digitsOnly.toCharArray();
        Arrays.sort(digitsArr);

        return new String(digitsArr);
    }

    public boolean isValidChar(char c) {
        return Character.isDigit(c) || c == '-' || isDelimiter(c);
    }

    public boolean isDelimiter(char c) {
        return c == ',' || c == '|' || c == ';' || Character.isWhitespace(c);
    }

    public int[] stringToNumberTokens(String input) {
        if (input == null || input.trim().isEmpty()) {
            return new int[0];
        }

        List<String> tokens = new ArrayList<>();
        StringBuilder currentToken = new StringBuilder();

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (!isValidChar(c)) {
                throw new IllegalArgumentException("Input contains invalid characters");
            }

            if (Character.isDigit(c)) {
                currentToken.append(c);
            } else if (isDelimiter(c) && currentToken.length() > 0) { // we need to add the check for the length of
                                                                      // current token as we might have multiple
                                                                      // delimiters
                tokens.add(currentToken.toString());
                currentToken = new StringBuilder();
            } else {
                continue;
            }

        }

        if (currentToken.length() > 0) {
            tokens.add(currentToken.toString());
        }

        int[] result = new int[tokens.size()];
        for (int i = 0; i < tokens.size(); i++) {
            result[i] = Integer.parseInt(tokens.get(i));
        }

        return result;
    }

    public int[] sortNumbersDesc(String input) {
        if (input == null || input.trim().isEmpty()) {
            return new int[0];
        }

        int[] numbers = stringToNumberTokens(input);

        Arrays.sort(numbers);

        for (int left = 0, right = numbers.length - 1; left < right; left++, right--) {
            int temp = numbers[left];
            numbers[left] = numbers[right];
            numbers[right] = temp;
        }

        return numbers;
    }

    public String sortNumbersDescStr(String input) {
        if (input == null || input.trim().isEmpty()) {
            return "";
        }

        int[] numbers = stringToNumberTokens(input);
        Arrays.sort(numbers);

        // swap to reverse to desc
        for (int left = 0, right = numbers.length - 1; left < right; left++, right--) {
            int temp = numbers[left];
            numbers[left] = numbers[right];
            numbers[right] = temp;
        }

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < numbers.length; i++) {
            result.append(numbers[i]);
            if (i < numbers.length - 1) {
                result.append(",");
            }
        }

        return result.toString();
    }

    public int[] sortNumbersAsc(String input) {
        if (input == null || input.trim().isEmpty()) {
            return new int[0];
        }

        int[] numbers = stringToNumberTokens(input);
        Arrays.sort(numbers);

        return numbers;
    }

    public String sortNumbersAscStr(String input) {
        if (input == null || input.trim().isEmpty()) {
            return "";
        }

        int[] numbers = stringToNumberTokens(input);
        Arrays.sort(numbers);

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < numbers.length; i++) {
            result.append(numbers[i]);
            if (i < numbers.length - 1) {
                result.append(",");
            }
        }

        return result.toString();
    }

    public String reverseNumbers(String input) {
        if (input == null || input.trim().isEmpty()) {
            return "";
        }

        int[] numbers = stringToNumberTokens(input);

        // swap to reverse to desc
        for (int left = 0, right = numbers.length - 1; left < right; left++, right--) {
            int temp = numbers[left];
            numbers[left] = numbers[right];
            numbers[right] = temp;
        }

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < numbers.length; i++) {
            result.append(numbers[i]);
            if (i < numbers.length - 1) {
                result.append(",");
            }
        }

        return result.toString();
    }

    public String reverseDigits(String input) {
        if (input == null || input.trim().isEmpty()) {
            return "";
        }

        String digitsOnly = input.replaceAll("\\D", "");

        char[] digits = digitsOnly.toCharArray();

        // swap to reverse to desc
        for (int left = 0, right = digits.length - 1; left < right; left++, right--) {
            char temp = digits[left];
            digits[left] = digits[right];
            digits[right] = temp;
        }

        return IntStream.range(0, digits.length).mapToObj(i -> String.valueOf(digits[i]))
                .collect(Collectors.joining(","));
    }

    public int findLargest(String input) {
        return 0;
    }

    public int findSmallest(String input) {
        return 0;
    }

    public String getUniqueDigits(String input) {
        return "";
    }

    public int[] getUniqueNumbers(String input) {
        return new int[0];
    }

    public String getEvenDigits(String input) {
        return "";
    }

    public int[] getOddNumbers(String input) {
        return new int[0];
    }

    public int sumDigits(String input) {
        if (input == null || input.trim().isEmpty()) {
            return 0;
        }

        String digitsOnly = input.replaceAll("\\D", "");
        char[] digits = digitsOnly.toCharArray();

        int result = 0;
        for (char c : digits) {
            result += c - '0';
        }

        return result;
    }

    public long sumNumbers(String input) {
        if (input == null || input.trim().isEmpty()) {
            return 0;
        }

        long result = 0;
        StringBuilder currentToken = new StringBuilder();
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (!isValidChar(c)) {
                throw new IllegalArgumentException("Invalid character in input");
            }

            if (Character.isDigit(c)) {
                currentToken.append(c);
            } else if (isDelimiter(c)) {
                if (currentToken.length() > 0) {
                    result += Integer.parseInt(currentToken.toString());
                    currentToken = new StringBuilder();
                }
            }
        }
        if (currentToken.length() > 0) {
            result += Integer.parseInt(currentToken.toString());
        }

        return result;
    }

    public int countDigits(String input) {
        return 0;
    }

    public int countNumbers(String input) {
        return 0;
    }

    public int countDelimiters(String input) {
        return 0;
    }

    public long productDigits(String input) {
        return 0;
    }

    public long productNumbers(String input) {
        return 0;
    }

    public double averageDigits(String input) {
        return 0;
    }

    public double averageNumbers(String input) {
        return 0;
    }

    public int minDigit(String input) {
        return 0;
    }

    public int maxDigit(String input) {
        return 0;
    }

    public int minNumber(String input) {
        return 0;
    }

    public int maxNumber(String input) {
        return 0;
    }

    public long sumFactorials(String input) {
        return 0;
    }

    public long sumSquares(String input) {
        return 0;
    }

    public int sumEvenDigits(String input) {
        return 0;
    }

    public int sumOddNumbers(String input) {
        return 0;
    }

    public int sumNumbersAbove(String input, int threshold) {
        return 0;
    }

    public int digitalRoot(String input) {
        return 0;
    }

    public int checksum(String input) {
        return 0;
    }

    public double median(String input) {
        return 0;
    }

    public int[] mode(String input) {
        return new int[0];
    }

    public static void main(String[] args) {
        JuliusBaerPractice juliusBaerPractice = new JuliusBaerPractice();
        String input = "1,2,34";
        System.out.println(Arrays.toString(juliusBaerPractice.sortNumbersDesc(input)));
        assert juliusBaerPractice.sortDigitsDesc(input).equals("4321");
        assert juliusBaerPractice.sortDigitsAsc(input).equals("1234");
        assert Arrays.equals(juliusBaerPractice.sortNumbersDesc(input), new int[] {
                34, 2, 1 });
        assert Arrays.equals(juliusBaerPractice.sortNumbersAsc(input), new int[] { 1,
                2, 34 });
        assert juliusBaerPractice.sortNumbersDescStr(input).equals("34,2,1");
        assert juliusBaerPractice.sortNumbersAscStr(input).equals("1,2,34");
        assert juliusBaerPractice.reverseNumbers(input).equals("34,2,1");
        assert juliusBaerPractice.reverseDigits(input).equals("4,3,2,1");
        // assert juliusBaerPractice.findLargest(input) == 34;
        // assert juliusBaerPractice.findSmallest(input) == 1;
        assert juliusBaerPractice.sumDigits(input) == 10;
        assert juliusBaerPractice.sumNumbers(input) == 37;

        input = "1||2,,,,3";
        assert juliusBaerPractice.sortDigitsDesc(input).equals("321");
        assert juliusBaerPractice.sortDigitsAsc(input).equals("123");
        assert Arrays.equals(juliusBaerPractice.sortNumbersDesc(input), new int[] {
                3, 2, 1 });
        assert Arrays.equals(juliusBaerPractice.sortNumbersAsc(input), new int[] { 1,
                2, 3 });
        assert juliusBaerPractice.sortNumbersDescStr(input).equals("3,2,1");
        assert juliusBaerPractice.sortNumbersAscStr(input).equals("1,2,3");
        assert juliusBaerPractice.reverseNumbers(input).equals("3,2,1");
        assert juliusBaerPractice.reverseDigits(input).equals("3,2,1");
        // assert juliusBaerPractice.findLargest(input) == 3;
        // assert juliusBaerPractice.findSmallest(input) == 1;
        assert juliusBaerPractice.sumDigits(input) == 6;

        input = "-1,2,3";
        assert juliusBaerPractice.sortDigitsDesc(input).equals("321");
        assert juliusBaerPractice.sortDigitsAsc(input).equals("123");
        assert Arrays.equals(juliusBaerPractice.sortNumbersDesc(input), new int[] {
                3, 2, 1 });
        assert Arrays.equals(juliusBaerPractice.sortNumbersAsc(input), new int[] { 1,
                2, 3 });
        assert juliusBaerPractice.sortNumbersDescStr(input).equals("3,2,1");
        assert juliusBaerPractice.sortNumbersAscStr(input).equals("1,2,3");
        assert juliusBaerPractice.reverseNumbers(input).equals("3,2,1");
        assert juliusBaerPractice.reverseDigits(input).equals("3,2,1");
        // assert juliusBaerPractice.findLargest(input) == 3;
        // assert juliusBaerPractice.findSmallest(input) == 1;
        assert juliusBaerPractice.sumDigits(input) == 6;

        // input = "1,2,2,3,1";
        // assert juliusBaerPractice.getUniqueDigits(input).equals("123");
        // assert Arrays.equals(juliusBaerPractice.getUniqueNumbers(input), new int[] {
        // 1, 2, 3 });

        // input = "1||1,,,,2,30|30,,31";
        // assert juliusBaerPractice.getUniqueDigits(input).equals("231");
        // assert Arrays.equals(juliusBaerPractice.getUniqueNumbers(input), new int[] {
        // 2, 31 });

        // input = "1,2,34,5";
        // assert juliusBaerPractice.getEvenDigits(input).equals("24");
        // assert Arrays.equals(juliusBaerPractice.getOddNumbers(input), new int[] { 1,
        // 5 });

        input = "10||2,,,,30";
        assert juliusBaerPractice.sumNumbers(input) == 42;

        input = "-1,2,34";
        assert juliusBaerPractice.sumNumbers(input) == 37;
    }

}
