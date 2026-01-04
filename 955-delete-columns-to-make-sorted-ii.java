import java.util.*;

class DeleteColumnsToMakeSortedII {
    public int minDeletionSize(String[] strs) {
        int toDel = 0;
        List<Integer> checkList = new ArrayList<>();
        for (int i = 0; i < strs.length - 1; i++) {
            checkList.add(i);
        }
        for (int j = 0; j < strs[0].length(); j++) {
            List<Integer> newChecklist = new ArrayList<>();
            boolean shouldDelete = false;
            for (int i : checkList) {
                if (strs[i].charAt(j) > strs[i+1].charAt(j)) {
                    toDel++;
                    shouldDelete = true;
                    break;
                }
                if (strs[i].charAt(j) == strs[i+1].charAt(j)) {
                    newChecklist.add(i);
                }
            }

            if (!shouldDelete) {
                if (newChecklist.isEmpty()) {
                    return toDel;
                }
                checkList = newChecklist;
            }
        }
        return toDel;
    }

    public static void main(String[] args) {
        DeleteColumnsToMakeSortedII sol = new DeleteColumnsToMakeSortedII();
        System.out.println("Output: " + sol.minDeletionSize(new String[] { "ca", "bb", "ac" }) + ", expected: 1");
        System.out.println("Output: " + sol.minDeletionSize(new String[] { "xc", "yb", "za" }) + ", expected: 0");
        System.out.println("Output: " + sol.minDeletionSize(new String[] { "zyx", "wvu", "tsr" }) + ", expected: 3");
    }
}
