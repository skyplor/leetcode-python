import java.util.*;

class LexicographicallySmallestStringAfterApplyingOperationsSolution {

    public String findLesSmallestString(String s, int a, int b) {
        String res = s;
        Set<String> seen = new HashSet<>();
        Queue<String> queue = new ArrayDeque<>();
        queue.add(s);
        int n = s.length();

        while (!queue.isEmpty()) {
            String cur = queue.poll();
            char[] addedChars = cur.toCharArray();
            for (int i = 1; i < n; i += 2) {
                addedChars[i] = (char) ((addedChars[i] - '0' + a) % 10 + '0');
            }
            String addedString = String.valueOf(addedChars);
            String rotatedString = cur.substring(n - b) + cur.substring(0, n - b);
            for (String t : List.of(addedString, rotatedString)) {
                if (!seen.contains(t)) {
                    seen.add(t);
                    queue.offer(t);
                    if (res.compareTo(t) > 0) {
                        res = t;
                    }
                }
            }
        }

        return res;
    }

    public static void main(String[] args) {
        LexicographicallySmallestStringAfterApplyingOperationsSolution sol = new LexicographicallySmallestStringAfterApplyingOperationsSolution();
        System.out.println("Output: " + sol.findLesSmallestString("5525", 9, 2) + ", expected: 2050");
    }
}
