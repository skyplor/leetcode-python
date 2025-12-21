import java.util.*;

class MaximumFrequencyOfAnElementAfterPerformingOperationsIISolution {

    public int maxFrequency(int[] nums, int k, int numOperations) {
        Arrays.sort(nums);
        Map<Integer, Integer> freq = new HashMap<>();
        Set<Integer> candidatesSet = new HashSet<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
            candidatesSet.add(num - k);
            candidatesSet.add(num);
            candidatesSet.add(num + k);
        }

        List<Integer> candidates = new ArrayList<>(candidatesSet);
        Collections.sort(candidates);

        int maxFrequency = 0, left = 0, right = 0;

        for (Integer t : candidates) {
            while (right < nums.length && nums[right] <= t + k) {
                right++;
            }
            while (left < nums.length && nums[left] < t - k) {
                left++;
            }
            int totalInRange = right - left;
            int alreadyAt = freq.getOrDefault(t, 0);
            int canReach = totalInRange - alreadyAt;
            int maxFrequencyAtT = alreadyAt + Math.min(numOperations, canReach);
            if (maxFrequencyAtT > maxFrequency) {
                maxFrequency = maxFrequencyAtT;
            }
        }

        return maxFrequency;
    }

    public static void main(String[] args) {
        MaximumFrequencyOfAnElementAfterPerformingOperationsIISolution sol = new MaximumFrequencyOfAnElementAfterPerformingOperationsIISolution();
        System.out.println("Output: " + sol.maxFrequency(new int[] { 1, 4, 5 }, 1, 2) + ", expected: 2");
        System.out.println("Output: " + sol.maxFrequency(new int[] { 5, 11, 20, 20 }, 5, 1) + ", expected: 2");
    }
}
