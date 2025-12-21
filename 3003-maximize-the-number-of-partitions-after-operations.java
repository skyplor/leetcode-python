import java.util.HashMap;
import java.util.Map;

class MaximizeTheNumberOfPartitionsAfterOperationsSolution {

    Map<String, Integer> memo;

    public int maxPartitionsAfterOperations(String s, int k) {
        memo = new HashMap<>();
        return dp(s, k, 0, false, 0);
    }

    public int dp(String s, int k, int mask, boolean change, int i) {
        if (i == s.length()) {
            return 1;
        }

        String key = mask + "|" + (change? 1:0) + "|" + i;
    
        if (memo.containsKey(key)) {
            return memo.get(key);
        }

        int maxPartitions = 0;
        int curr = s.charAt(i) - 'a';
        int currMask = 1 << curr;
        int newMask = mask | currMask;
        if (Integer.bitCount(newMask) <= k) {
            maxPartitions = Math.max(maxPartitions, dp(s, k, newMask, change, i + 1));
        } else {
            maxPartitions = Math.max(maxPartitions, dp(s, k, currMask, change, i + 1) + 1);
        }

        if (!change) {
            for (int j = 0; j < 26; j++) {
                if (j == curr)
                    continue;
                currMask = 1 << j;
                newMask = mask | currMask;
                if (Integer.bitCount(newMask) <= k) {
                    maxPartitions = Math.max(maxPartitions, dp(s, k, newMask, true, i + 1));
                } else {
                    maxPartitions = Math.max(maxPartitions, dp(s, k, currMask, true, i + 1) + 1);
                }
            }
        }
        memo.put(key, maxPartitions);
        return maxPartitions;
    }

    public static void main(String[] args) {
        MaximizeTheNumberOfPartitionsAfterOperationsSolution sol = new MaximizeTheNumberOfPartitionsAfterOperationsSolution();
        System.out.println(String.format("Output: %d, expected: %d", sol.maxPartitionsAfterOperations("accca", 2), 3));
        System.out.println(String.format("Output: %d, expected: %d", sol.maxPartitionsAfterOperations("aabaab", 3), 1));
        System.out.println(String.format("Output: %d, expected: %d", sol.maxPartitionsAfterOperations("xxyz", 1), 4));
        System.out.println(String.format("Output: %d, expected: %d", sol.maxPartitionsAfterOperations("abcdefghijklmnnnnnnnnnnnnnnnnnnnnnnnnnnaopqrstuvwxyz", 14), 2));
    }

}
