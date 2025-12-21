import java.util.*;

class SwimInRisingWaterSolution {

    public int swimInWater(int[][] grid) {
        Queue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        Set<String> visited = new HashSet<>();
        int[][] directions = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };
        pq.offer(new int[] { grid[0][0], 0, 0 });
        visited.add("0:0");

        while (!pq.isEmpty()) {
            int[] item = pq.poll();
            int cost = item[0], r = item[1], c = item[2];
            if (r == grid.length - 1 && c == grid.length - 1) {
                return cost;
            }
            for (int[] direction : directions) {
                int nr = r + direction[0], nc = c + direction[1];
                if (nr < 0 || nr >= grid.length || nc < 0 || nc >= grid.length || visited.contains(nr + ":" + nc)) {
                    continue;
                }
                visited.add(nr + ":" + nc);
                int newCost = Math.max(cost, grid[nr][nc]);
                pq.offer(new int[] { newCost, nr, nc });
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        SwimInRisingWaterSolution sol = new SwimInRisingWaterSolution();
        System.out.println("Output: " + sol.swimInWater(new int[][] { { 0, 2 }, { 1, 3 } }) + ", expected: 3");
        System.out
                .println(
                        "Output: "
                                + sol.swimInWater(new int[][] { { 0, 1, 2, 3, 4 }, { 24, 23, 22, 21, 5 },
                                        { 12, 13, 14, 15, 16 }, { 11, 17, 18, 19, 20 }, { 10, 9, 8, 7, 6 } })
                                + ", expected: 16");
    }
}
