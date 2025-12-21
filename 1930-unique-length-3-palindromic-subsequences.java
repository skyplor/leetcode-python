import java.util.*;

class UniqueLength3PalindromicSubsequences {
  
    public int countPalindromicSubsequence(String s) {
        Set<Character> left = new HashSet<>();
        Set<Character> right = new HashSet<>();
        int[] rightCount = new int[26];

        for (char c : s.toCharArray()) {
            right.add(c);
            rightCount[c - 'a']++;
        }
        Set<String> res = new HashSet<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (i > 0) {
                left.add(s.charAt(i-1));
            }
            rightCount[c - 'a']--;
            if (rightCount[c-'a'] == 0) {
                right.remove(c);
            }
            for (Character leftC : left) {
                if (right.contains(leftC)) {
                    res.add("" + leftC + c + leftC);
                }
            }
        }
        return res.size();
    }
    public static void main(String[] args) {
        UniqueLength3PalindromicSubsequences sol = new UniqueLength3PalindromicSubsequences();
        System.out.println("Output: " + sol.countPalindromicSubsequence("aabca") + ", expected: 3");
        System.out.println("Output: " + sol.countPalindromicSubsequence("adc") + ", expected: 0");
        System.out.println("Output: " + sol.countPalindromicSubsequence("bbcbaba") + ", expected: 4");
    }
}
