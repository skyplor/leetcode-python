import java.util.*;

class SetIntersectionSizeAtLeastTwo {

    public int intersectionSizeTwo(int[][] intervals) {
        int[] nums = new int[2 * intervals.length];
        int size = 0;
        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[1], i2[1]));
        for (int[] interval : intervals) {
            int start = interval[0], end = interval[1];
            int count = 0;
            if (size > 0 && nums[size - 1] >= start) count++;
            if (size >= 2 && nums[size - 2] >= start) count++;

            if (count == 0) {
                nums[size++] = end - 1;
                nums[size++] = end;
            } else if (count == 1) {
                if (nums[size - 1] == end) {
                    nums[size++] = end - 1;
                } else {
                    nums[size++] = end;
                }
            }
        }
        return size;
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
