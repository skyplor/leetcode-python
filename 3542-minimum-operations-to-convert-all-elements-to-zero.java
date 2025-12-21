import java.util.*;

class MinimumOperationsToConvertAllElementsToZero {
    public int minOperations(int[] nums) {
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        int res = 0;
        for (int num : nums) {
            while (num < stack.peek()) {
                stack.pop();
            }
            if (num != stack.peek()) {
                res++;
            }
            stack.push(num);
        }
        return res;
    }

    public static void main(String[] args) {
        MinimumOperationsToConvertAllElementsToZero sol = new MinimumOperationsToConvertAllElementsToZero();
        System.out.println("Output: " + sol.minOperations(new int[] { 0, 2 }) + ", expected: 1");
        System.out.println("Output: " + sol.minOperations(new int[] { 3, 1, 2, 1 }) + ", expected: 3");
        System.out.println("Output: " + sol.minOperations(new int[] { 1, 2, 1, 2, 1, 2 }) + ", expected: 4");
    }
}
