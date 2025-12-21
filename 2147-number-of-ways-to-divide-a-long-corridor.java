import java.util.*;

class NumberOfWaysToDivideALongCorridor {
    public int numberOfWays(String corridor) {
        int sCount = 0;
        for (char c : corridor.toCharArray()) {
            if (c == 'S') {
                sCount++;
            }
        }
        if (sCount < 2 || sCount % 2 == 1) {
            return 0;
        }

        Map<Integer, Integer> GROUPINGMAP = new HashMap<>() {
            {
                put(0, 1);
                put(1, 2);
                put(2, 1);
            }
        };
        int[] groupings = new int[corridor.length()];
        groupings[0] = corridor.charAt(0) == 'P' ? 0 : 1;
        for (int i = 1; i < corridor.length(); i++) {
            if (corridor.charAt(i) == 'P') {
                groupings[i] = groupings[i-1];
                continue;
            }
            groupings[i] = GROUPINGMAP.get(groupings[i-1]);
        }
        int right = 1, left = 0;
        long res = 1;
        while (right < corridor.length() - 1) {
            int prev = groupings[right - 1], curr = groupings[right];
            if (prev == 1 && curr == 2) {
                int multiplier = 1;
                left = right;
                if (groupings[right] == 2) {
                    while (right < corridor.length() - 1 && groupings[right] == 2) {
                        right++;
                    }
                    if (right < corridor.length() - 1) {
                        multiplier = right - left;
                    }
                    res = (res * multiplier) % 1_000_000_007;
                }
            }
            right++;
        }
        return (int) res;
    }

    public static void main(String[] args) {
        NumberOfWaysToDivideALongCorridor sol = new NumberOfWaysToDivideALongCorridor();
        System.out.println("Output: " + sol.numberOfWays("SSPPSPS") + ", expected: 3");
        System.out.println("Output: " + sol.numberOfWays("PPSPSP") + ", expected: 1");
        System.out.println("Output: " + sol.numberOfWays("S") + ", expected: 0");
    }
}
