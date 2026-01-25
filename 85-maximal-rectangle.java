import java.util.ArrayDeque;
import java.util.Deque;

class MaximalRectangle {
    public int maximalRectangle(char[][] matrix) {
        int n = matrix[0].length, maxArea = 0;
        int[] heights = new int[n+1];
        for (char[] row : matrix) {
            for (int i = 0; i < row.length; i++) {
                char colVal = row[i];
                if (colVal == '1') {
                    heights[i]++;
                } else {
                    heights[i] = 0;
                }
            }

            Deque<int[]> stack = new ArrayDeque<>();
            for (int i = 0; i < heights.length; i++) {
                int h = heights[i];
                int prevI = i;
                while (stack.size() > 0 && (stack.peek()[1] > h)) {
                    int[] top = stack.pop();
                    maxArea = Math.max(maxArea, (i - top[0])*top[1]);
                    prevI = top[0];
                }
                stack.push(new int[]{prevI, h});
            }

            while (stack.size() > 0) {
                int[] top = stack.pop();
                int i = top[0], h = top[1];
                maxArea = Math.max(maxArea, (n - i) * h);
            }
        }
        return maxArea;
    }

    public static void main(String[] args) {
        MaximalRectangle sol = new MaximalRectangle();
        System.out.println("Output: " + sol.maximalRectangle(new char[][] {{'1', '0', '1', '0', '0'}, {'1', '0', '1', '1', '1'}, {'1', '1', '1', '1', '1'}, {'1', '0', '0', '1', '0'}}) + ", expected: 6");
        System.out.println("Output: " + sol.maximalRectangle(new char[][] {{'0'}}) + ", expected: 0");
        System.out.println("Output: " + sol.maximalRectangle(new char[][] {{'1'}}) + ", expected: 1");
    }
}