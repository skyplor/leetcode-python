import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

class FindResultantArrayAfterRemovingAnagramsSolution {

    public String sortedString(String s) {
        char[] charArray = s.toCharArray();
        Arrays.sort(charArray);
        return new String(charArray);
    }

    public List<String> removeAnagrams(String[] words) {
        int n = words.length;
        String prevSorted = sortedString(words[0]);
        int i = 1;
        int idxToAdd = 0;
        List<String> result = new ArrayList<>();
        while (i < n) {
            String currSorted = sortedString(words[i]);
            if (!currSorted.equalsIgnoreCase(prevSorted)) {
                result.add(words[idxToAdd]);
                idxToAdd = i;
            }

            i++;
            prevSorted = currSorted;
        }
        result.add(words[idxToAdd]);

        return result;
    }

    public static void main(String[] args) {
        FindResultantArrayAfterRemovingAnagramsSolution sol = new FindResultantArrayAfterRemovingAnagramsSolution();
        System.out.println("Output: "
                + Arrays.toString(
                        sol.removeAnagrams(new String[] { "abba", "baba", "bbaa", "cd", "cd" }).toArray(new String[0]))
                + ", expected: [\"abba\", \"cd\"]");
        System.out.println("Output: "
                + Arrays.toString(sol.removeAnagrams(new String[] { "a", "b", "c", "d", "e" }).toArray(new String[0]))
                + ", expected: [\"a\",\"b\",\"c\",\"d\",\"e\"]");
    }

}
