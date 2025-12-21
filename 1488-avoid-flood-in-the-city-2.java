import java.util.*;

class AvoidFloodInTheCitySolution2 {
    public int[] avoidFlood(int[] rains) {
        int[] ans = new int[rains.length];
        Map<Integer, Integer> lakeFullDayMap = new HashMap<>();
        TreeSet<Integer> dryDaysIndices = new TreeSet<>();
        for (int i = 0; i < rains.length; i++) {
            int lake = rains[i];
            if (lake == 0) {
                dryDaysIndices.add(i);
                ans[i] = 1;
            } else {
                ans[i] = -1;
                Integer index = lakeFullDayMap.get(lake);
                if (index != null) {
                    Integer nextDryDayIndex = dryDaysIndices.ceiling(index);
                    if (nextDryDayIndex == null) return new int[0];

                    dryDaysIndices.remove(nextDryDayIndex);
                    ans[nextDryDayIndex] = lake;
                }
                lakeFullDayMap.put(lake, i);
            }
        }

        return ans;
    }

    public static void main(String[] args) {
        AvoidFloodInTheCitySolution2 sol = new AvoidFloodInTheCitySolution2();
        System.out.println("output: " + sol.avoidFlood(new int[] { 1, 2, 3, 4 }) + ", expected: [-1,-1,-1,-1]");
        System.out
                .println("output: " + sol.avoidFlood(new int[] { 1, 2, 0, 0, 2, 1 }) + ", expected: [-1,-1,2,1,-1,-1]");
        System.out.println("output: " + sol.avoidFlood(new int[] { 1, 2, 0, 1, 2 }) + ", expected: []");
    }

}
