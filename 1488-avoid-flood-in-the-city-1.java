import java.util.*;

class AvoidFloodInTheCitySolution {
    public int[] avoidFlood(int[] rains) {
        Queue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        Map<Integer, List<Integer>> lakeIndicesMap = new HashMap<>();
        Map<Integer, Boolean> lakeStates = new HashMap<>();

        for (int i = 0; i < rains.length; i++) {
            int lake = rains[i];
            if (lake > 0) {
                if (!lakeIndicesMap.containsKey(lake)) {
                    lakeIndicesMap.put(lake, new ArrayList<>());
                }
                List<Integer> lakeIndices = lakeIndicesMap.get(lake);
                lakeIndices.add(i);
            }
        }

        int[] ans = new int[rains.length];

        for (int i = 0; i < rains.length; i++) {
            int lake = rains[i];
            if (lake > 0) {
                if (lakeStates.getOrDefault(lake, false)) {
                    return new int[0];
                } else {
                    lakeStates.put(lake, true);
                    List<Integer> lakeIndices = lakeIndicesMap.get(lake);
                    ans[i] = -1;
                    if (lakeIndices.size() > 0) {
                        lakeIndices.remove(0);
                    }
                    if (lakeIndices.size() > 0) {
                        minHeap.offer(new int[] { lakeIndices.get(0), lake });
                    }
                }
            } else {
                ans[i] = 1;
                if (minHeap.size() > 0) {
                    int[] nextElement = minHeap.poll();
                    int nextLake = nextElement[1];
                    lakeStates.put(nextLake, false);
                    ans[i] = nextLake;
                }

            }
        }

        return ans;
    }

    public static void main(String[] args) {
        AvoidFloodInTheCitySolution sol = new AvoidFloodInTheCitySolution();
        System.out.println("output: " + sol.avoidFlood(new int[] { 1, 2, 3, 4 }) + ", expected: [-1,-1,-1,-1]");
        System.out
                .println("output: " + sol.avoidFlood(new int[] { 1, 2, 0, 0, 2, 1 }) + ", expected: [-1,-1,2,1,-1,-1]");
        System.out.println("output: " + sol.avoidFlood(new int[] { 1, 2, 0, 1, 2 }) + ", expected: []");
    }

}
