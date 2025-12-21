import java.util.*;

class FindXSumOfAllKLongSubarraysII {

    public long[] findXSum(int[] nums, int k, int x) {
        Map<Integer, Integer> frequency = new HashMap<>();
        TreeSet<int[]> top = new TreeSet<>((a, b) -> {
            if (a[0] != b[0])
                return a[0] - b[0];
            return a[1] - b[1];
        });
        TreeSet<int[]> rest = new TreeSet<>((a, b) -> {
            if (a[0] != b[0])
                return a[0] - b[0];
            return a[1] - b[1];
        });

        long runningTotal = 0;
        long[] result = new long[nums.length - k + 1];

        for (int i = 0; i < k; i++) {
            runningTotal = add(frequency, nums[i], x, runningTotal, top, rest);
        }
        result[0] = runningTotal;

        for (int i = k; i < nums.length; i++) {
            runningTotal = remove(frequency, nums[i - k], x, runningTotal, top, rest);
            runningTotal = add(frequency, nums[i], x, runningTotal, top, rest);
            result[i - k + 1] = runningTotal;
        }
        return result;
    }

    long balance(int x, long runningTotal, TreeSet<int[]> top, TreeSet<int[]> rest) {
        while (top.size() < x && !rest.isEmpty()) {
            int[] restElement = rest.last();
            runningTotal += (long) restElement[0] * restElement[1];
            top.add(restElement);
            rest.remove(restElement);
        }

        while (top.size() > x) {
            int[] topElement = top.first();
            runningTotal -= (long) topElement[0] * topElement[1];
            rest.add(topElement);
            top.remove(topElement);
        }

        while (!rest.isEmpty() && !top.isEmpty()) {
            int[] restElement = rest.last();
            int[] topElement = top.first();
            if (restElement[0] > topElement[0] ||
                    (restElement[0] == topElement[0] && restElement[1] > topElement[1])) {

                runningTotal += (long) restElement[0] * restElement[1] -
                        (long) topElement[0] * topElement[1];
                rest.add(topElement);
                top.add(restElement);
                rest.remove(restElement);
                top.remove(topElement);
            } else {
                break;
            }
        }

        return runningTotal;
    }

    long add(Map<Integer, Integer> frequency, int num, int x, long runningTotal, TreeSet<int[]> top,
            TreeSet<int[]> rest) {
        int[] old = { frequency.getOrDefault(num, 0), num };
        if (top.contains(old)) {
            top.remove(old);
            runningTotal -= (long) old[0] * old[1];
        } else if (rest.contains(old)) {
            rest.remove(old);
        }
        frequency.put(num, frequency.getOrDefault(num, 0) + 1);
        rest.add(new int[] { frequency.get(num), num });

        return balance(x, runningTotal, top, rest);
    }

    long remove(Map<Integer, Integer> frequency, int num, int x, long runningTotal, TreeSet<int[]> top,
            TreeSet<int[]> rest) {
        int[] old = { frequency.getOrDefault(num, 0), num };
        if (top.contains(old)) {
            top.remove(old);
            runningTotal -= (long) old[0] * old[1];
        } else if (rest.contains(old)) {
            rest.remove(old);
        }
        frequency.put(num, frequency.getOrDefault(num, 0) - 1);
        if (frequency.get(num) > 0) {
            rest.add(new int[] { frequency.get(num), num });
        } else {
            frequency.remove(num);
        }

        return balance(x, runningTotal, top, rest);
    }

    public static void main(String[] args) {
        FindXSumOfAllKLongSubarraysII sol = new FindXSumOfAllKLongSubarraysII();

        System.out.println(
                "Output: " + Arrays.toString(sol.findXSum(new int[] { 1, 1, 2, 2, 3, 4, 2, 3 }, 6, 2))
                        + ", expected: [6, 10, 12]");
        System.out.println(
                "Output: " + Arrays.toString(sol.findXSum(new int[] { 3, 8, 7, 8, 7, 5 }, 2, 2))
                        + ", expected: [11, 15, 15, 15, 12]");
        System.out
                .println("Output: " + Arrays.toString(sol.findXSum(new int[] { 9, 2, 2 }, 3, 3)) + ", expected: [13]");
    }
}
