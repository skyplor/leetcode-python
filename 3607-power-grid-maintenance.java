import java.util.*;

class PowerGridMaintenance {
    int[] parent, rank;

    public int[] processQueries(int c, int[][] connections, int[][] queries) {
        Set<Integer> offline = new HashSet<>();
        parent = new int[c + 1];
        rank = new int[c + 1];
        for (int i = 0; i < parent.length; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < rank.length; i++) {
            rank[i] = 1;
        }

        for (int[] conn : connections) {
            int s1 = conn[0], s2 = conn[1];
            union(s1, s2);
        }

        Map<Integer, Queue<Integer>> connectedComponents = new HashMap<>();
        for (int i = 1; i < parent.length; i++) {
            int root = find(i);
            Queue<Integer> pq = connectedComponents.getOrDefault(root, new PriorityQueue<>());
            pq.add(i);
            connectedComponents.put(root, pq);
        }

        Map<Integer, Integer> componentRoot = new HashMap<>();
        for (int i = 1; i < parent.length; i++) {
            componentRoot.put(i, find(i));
        }

        List<Integer> res = new ArrayList<>();
        for (int[] q : queries) {
            int station = q[1];
            if (q[0] == 2) {
                offline.add(station);
                continue;
            }

            Queue<Integer> conn = connectedComponents.getOrDefault(componentRoot.get(station), new PriorityQueue<>());
            if (!offline.contains(station)) {
                res.add(station);
                continue;
            }

            while (!conn.isEmpty() && (offline.contains(conn.peek()) || conn.peek() == station)) {
                conn.poll();
            }

            if (!conn.isEmpty()) {
                res.add(conn.peek());
            } else {
                res.add(-1);
            }
        }

        return res.stream().mapToInt(i -> i).toArray();
    }

    private int find(int i) {
        if (parent[i] == i) {
            return i;
        }
        while (parent[i] != i) {
            parent[i] = parent[parent[i]];
            i = parent[i];
        }
        return parent[i];
    }

    private void union(int i, int j) {
        int parent_i = find(i), parent_j = find(j);
        if (parent_i == parent_j) {
            return;
        }

        if (rank[parent_i] < rank[parent_j]) {
            parent[parent_i] = parent[parent_j];
            rank[parent_j] += rank[parent_i];
        } else {
            parent[parent_j] = parent[parent_i];
            rank[parent_i] += rank[parent_j];
        }
    }

    public static void main(String[] args) {
        PowerGridMaintenance sol = new PowerGridMaintenance();
        System.out.println("Output: "
                + Arrays.toString(sol.processQueries(5, new int[][] { { 3, 1 }, { 2, 4 }, { 2, 1 }, { 1, 4 } },
                        new int[][] { { 2, 3 }, { 2, 1 }, { 1, 1 }, { 1, 3 }, { 2, 2 }, { 2, 1 }, {
                                1, 2 }, { 2, 3 }, { 1, 4 }, { 2, 2 }, { 1, 1 }, { 2, 2 }, { 2, 1 }, { 2, 2 } }))
                + ", expected: [2, 2, 4, 4, 4]");
    }
}
