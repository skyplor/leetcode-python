import java.util.*;

class FinalValueOfVariableAfterPerformingOperationsSolution {

    public int finalValueAfterOperations(String[] operations) {
        return Arrays.asList(operations).stream().map(op -> op.contains("+") ? 1 : -1).reduce(0, Integer::sum);
    }
    public int finalValueAfterOperations2(String[] operations) {
        int res = 0;
        for (String op : operations) {
            int temp = op.contains("+") ? 1 : -1;
            res += temp;
        }
        return res;
    }

    public static void main(String[] args) {
        FinalValueOfVariableAfterPerformingOperationsSolution sol = new FinalValueOfVariableAfterPerformingOperationsSolution();
        System.out.println(
                "Output: " + sol.finalValueAfterOperations(new String[] { "--X", "X++", "X++" }) + ", expected: 1");
        System.out.println(
                "Output: " + sol.finalValueAfterOperations(new String[] { "++X", "++X", "X++" }) + ", expected: 3");
        System.out.println("Output: " + sol.finalValueAfterOperations(new String[] { "X++", "++X", "--X", "X--" })
                + ", expected: 0");
    }

}
