import java.util.*;

class TrappingRainWaterIISolution {
    public int trapRainWater(int[][] heightMap) {
        Queue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        for (int r = 0; r < heightMap.length; r++) {
            for (int c = 0; c < heightMap[0].length; c++) {
                if (r == 0 || r == heightMap.length - 1 || c == 0 || c == heightMap[0].length - 1) {
                    minHeap.add(new int[] { heightMap[r][c], r, c });
                    heightMap[r][c] = -1;
                }
            }
        }

        int res = 0;
        int maxHeight = -1;
        int[][] directions = {{ -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 }};
        while (!minHeap.isEmpty()) {
            int[] currElement = minHeap.poll();
            maxHeight = Math.max(maxHeight, currElement[0]);
            res += maxHeight - currElement[0];

            for (int[] direction : directions) {
                int nr = currElement[1] + direction[0];
                int nc = currElement[2] + direction[1];
                if (nr < 0 || nr >= heightMap.length || nc < 0 || nc >= heightMap[0].length
                        || heightMap[nr][nc] == -1) {
                    continue;
                }
                minHeap.add(new int[] { heightMap[nr][nc], nr, nc });
                heightMap[nr][nc] = -1;
            }
        }

        return res;
    }

    public static void main(String[] args) {
        TrappingRainWaterIISolution sol = new TrappingRainWaterIISolution();
        System.out.println("Output: "
                + sol.trapRainWater(new int[][] { { 1, 4, 3, 1, 3, 2 }, { 3, 2, 1, 3, 2, 4 }, { 2, 3, 3, 2, 3, 1 } })
                + ", expected: 4");
        System.out.println("Output: " + sol.trapRainWater(new int[][] { { 3, 3, 3, 3, 3 }, { 3, 2, 2, 2, 3 },
                { 3, 2, 1, 2, 3 }, { 3, 2, 2, 2, 3 }, { 3, 3, 3, 3, 3 } }) + ", expected: 10");
    }
}