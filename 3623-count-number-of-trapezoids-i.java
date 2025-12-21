import java.util.*;

class CountNumberOfTrapezoidsI {
  
    public int countTrapezoids(int[][] points) {
        int MOD = (int) Math.pow(10, 9) + 7;

        Map<Integer, Integer> count = new HashMap<>();
        for (int[] point : points) {
            int y = point[1];
            count.put(y, count.getOrDefault(y, 0) + 1);
        }
        long res = 0;
        long prev = 0;
        for (long v : count.values()) {
            long cur = v * (v - 1) / 2;
            res = (res + prev * cur) % MOD;
            prev = (prev + cur) % MOD;
        }
        return (int) res % MOD;
    }
    public static void main(String[] args) {
        CountNumberOfTrapezoidsI sol = new CountNumberOfTrapezoidsI();
        System.out.println("Output: " + sol.countTrapezoids(new int[][]{{1,0}, {2,0}, {3,0}, {2,2}, {3,2}}) + ", expected: 3");
    }
}
