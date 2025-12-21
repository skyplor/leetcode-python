import java.util.*;

class SetIntersectionSizeAtLeastTwo {

    public int intersectionSizeTwo(int[][] intervals) {
        List<Integer> nums = new ArrayList<>();
        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[1], i2[1]));
        for (int[] interval : intervals) {
            int start = interval[0], end = interval[1];
            int count = 0;
            if (nums.size() > 0 && nums.get(nums.size() - 1) >= start) {
                count++;
            }
            if (nums.size() >= 2 && nums.get(nums.size() - 2) >= start) {
                count++;
            }

            if (count == 0) {
                nums.add(end - 1);
                nums.add(end);
            } else if (count == 1) {
                if (nums.get(nums.size() - 1) == end) {
                    nums.add(end - 1);
                } else {
                    nums.add(end);
                }
            }
        }
        return nums.size();
    }

    public static void main(String[] args) {
        SetIntersectionSizeAtLeastTwo sol = new SetIntersectionSizeAtLeastTwo();
        System.out.println(
                "Output: " + sol.intersectionSizeTwo(new int[][] { { 1, 3 }, { 3, 7 }, { 8, 9 } }) + ", expected: 5");
        System.out.println("Output: " + sol.intersectionSizeTwo(new int[][] { { 1, 3 }, { 1, 4 }, { 2, 5 }, { 3, 5 } })
                + ", expected: 3");
        System.out.println("Output: " + sol.intersectionSizeTwo(new int[][] { { 1, 2 }, { 2, 3 }, { 2, 4 }, { 4, 5 } })
                + ", expected: 5");
    }
}
