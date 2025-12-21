import java.util.Arrays;

class CountCoveredBuildings {
    public int countCoveredBuildings(int n, int[][] buildings) {
        int[] minY = new int[n+1];
        int[] maxY = new int[n+1];
        int[] minX = new int[n+1];
        int[] maxX = new int[n+1];

        Arrays.fill(minY, Integer.MAX_VALUE);
        Arrays.fill(minX, Integer.MAX_VALUE);
        Arrays.fill(maxY, Integer.MIN_VALUE);
        Arrays.fill(maxX, Integer.MIN_VALUE);

        for (int i = 0; i < buildings.length; i++) {
            int x = buildings[i][0], y = buildings[i][1];
            minY[x] = Math.min(minY[x], y);
            minX[y] = Math.min(minX[y], x);
            maxY[x] = Math.max(maxY[x], y);
            maxX[y] = Math.max(maxX[y], x);
        }

        int covered = 0;
        for (int[] building : buildings) {
            int x = building[0], y = building[1];
            if (x > minX[y] && x < maxX[y] && y > minY[x] && y < maxY[x]) {
                covered++;
            }
        }

        return covered;
    }
  
    public static void main(String[] args) {
        CountCoveredBuildings sol = new CountCoveredBuildings();
        System.out.println("Output: " + sol.countCoveredBuildings(3, new int[][]{{1,2},{2,2},{3,2},{2,1},{2,3}}) + ", expected: 1");
        System.out.println("Output: " + sol.countCoveredBuildings(3, new int[][]{{1,1},{1,2},{2,1},{2,2}}) + ", expected: 0");
        System.out.println("Output: " + sol.countCoveredBuildings(5, new int[][]{{1,3},{3,2},{3,3},{3,5},{5,3}}) + ", expected: 1");
        System.out.println("Output: " + sol.countCoveredBuildings(3, new int[][]{{1,1}, {1,2}, {1,3}}) + ", expected: 0");
    }
}
