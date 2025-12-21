import java.util.*;

class MaximumNumberOfKDivisibleComponents {

    public int maxKDivisibleComponents(int n, int[][] edges, int[] values, int k) {
        Map<Integer, List<Integer>> adjList = new HashMap<>();
        for (int[] edge : edges) {
            int first = edge[0], second = edge[1];
            List<Integer> firstChildren = adjList.getOrDefault(first, new ArrayList<>());
            firstChildren.add(second);
            adjList.put(first, firstChildren);
            List<Integer> secondChildren = adjList.getOrDefault(second, new ArrayList<>());
            secondChildren.add(first);
            adjList.put(second, secondChildren);
        }
        int[] res = new int[1];
        dfs(adjList, values, k, 0, -1, res);

        return res[0];
    }

    private long dfs(Map<Integer, List<Integer>> adjList, int[] values, int k, int cur, int parent, int[] res) {
        long total = values[cur];
        for (int child : adjList.getOrDefault(cur, new ArrayList<>())) {
            if (child != parent) {
                total += dfs(adjList, values, k, child, cur, res);
            }
        }
        if (total % k == 0) {
            res[0]++;
        }
        return total;
    }

    public static void main(String[] args) {
        MaximumNumberOfKDivisibleComponents sol = new MaximumNumberOfKDivisibleComponents();
        System.out.println(
                "Output: " + sol.maxKDivisibleComponents(5, new int[][] { { 0, 2 }, { 1, 2 }, { 1, 3 }, { 2, 4 } },
                        new int[] { 1, 8, 1, 4, 4 }, 6) + ", expected: 2");
        System.out.println("Output: " + sol.maxKDivisibleComponents(7,
                new int[][] { { 0, 1 }, { 0, 2 }, { 1, 3 }, { 1, 4 }, { 2, 5 }, { 2, 6 } },
                new int[] { 3, 0, 6, 1, 5, 2, 1 }, 3) + ", expected: 3");
    }
}
