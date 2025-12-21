import java.util.*;
import java.util.Map.Entry;

class FindXSumOfAllKLongSubarraysI {

    public int[] findXSum(int[] nums, int k, int x) {

        List<Integer> result = new ArrayList<>();
        Map<Integer, Integer> count = new HashMap<>();
        for (int i = 0; i < nums.length - k + 1; i++) {
            Queue<int[]> maxHeap = new PriorityQueue<>((e1, e2) -> {
                if (e1[0] == e2[0]) {
                    return Integer.compare(e2[1], e1[1]);
                }
                return Integer.compare(e2[0], e1[0]);
            });
            int sum = 0;
            if (i == 0) {
                for (int j = 0; j < k; j++) {
                    count.put(nums[j], count.getOrDefault(nums[j], 0) + 1);
                }
            } else {
                int prev = nums[i - 1];
                int next = nums[i + k - 1];
                count.put(prev, count.get(prev) - 1);
                count.put(next, count.getOrDefault(next, 0) + 1);
            }

            for (Entry<Integer, Integer> entry : count.entrySet()) {
                int key = entry.getKey(), val = entry.getValue();
                maxHeap.add(new int[] { val, key });
            }

            for (int j = 0; j < x; j++) {
                if (!maxHeap.isEmpty()) {
                    int[] item = maxHeap.poll();
                    int val = item[0], key = item[1];
                    sum += val * key;
                }
            }
            result.add(sum);
        }
        return result.stream().mapToInt(i -> i).toArray();
    }

    public static void main(String[] args) {
        FindXSumOfAllKLongSubarraysI sol = new FindXSumOfAllKLongSubarraysI();

        System.out.println(
                "Output: " + Arrays.toString(sol.findXSum(new int[] { 1, 1, 2, 2, 3, 4, 2, 3 }, 6, 2)) + ", expected: [6, 10, 12]");
        System.out.println(
                "Output: " + Arrays.toString(sol.findXSum(new int[] { 3, 8, 7, 8, 7, 5 }, 2, 2)) + ", expected: [11, 15, 15, 15, 12]");
        System.out.println("Output: " + Arrays.toString(sol.findXSum(new int[] { 9, 2, 2 }, 3, 3)) + ", expected: [13]");
    }
}
