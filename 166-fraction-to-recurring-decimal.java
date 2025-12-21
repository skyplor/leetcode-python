import java.util.*;

class FractionToRecurringDecimalSolution {
    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) {
            return "0";
        }

        StringBuilder result = new StringBuilder();

        if ((numerator < 0 && denominator > 0) || (denominator < 0 && numerator > 0)) {
            result.append("-");
        }

        long num = Math.abs((long) numerator);
        long den = Math.abs((long) denominator);

        long remainder = num % den;
        // Calculate integer portion
        if (num >= den) {
            long divResult = num / den;
            result.append(divResult);
            if (remainder > 0) {
                result.append(".");
            }
        } else {
            result.append("0.");
        }

        Map<Long, Integer> seen = new HashMap<>();

        while (remainder > 0) {
            if (seen.containsKey(remainder)) {
                result.insert(seen.get(remainder), "(");
                result.append(")");
                break;
            }

            seen.put(remainder, result.length());

            num = remainder * 10;
            long divResult = num / den;
            remainder = num % den;
            result.append(divResult);
        }

        return result.toString();
    }

    public static void main(String[] args) {
        FractionToRecurringDecimalSolution sol = new FractionToRecurringDecimalSolution();
        System.out.println("output: " + sol.fractionToDecimal(1, 2) + ", expected: 0.5");
        System.out.println("output: " + sol.fractionToDecimal(2, 1) + ", expected: 2");
        System.out.println("output: " + sol.fractionToDecimal(4, 333) + ", expected: 0.(012)");
        System.out.println("output: " + sol.fractionToDecimal(1, 6) + ", expected: 0.1(6)");
        System.out.println("output: " + sol.fractionToDecimal(-50, 8) + ", expected: -6.25");
        System.out.println("output: " + sol.fractionToDecimal(50, -8) + ", expected: -6.25");
        System.out.println(
                "output: " + sol.fractionToDecimal(-1, -2147483648) + ", expected: 0.0000000004656612873077392578125");
    }
}
