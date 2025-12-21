import java.util.*;

class NextGreaterNumericallyBalancedNumber {
  
    public int nextBeautifulNumber(int n) {
        List<Integer> numbers = genBeautifulNumbers();
        for (Integer integer : numbers) {
            if (integer > n) {
                return integer;
            }
        }
        return -1;
    }

    private List<Integer> genBeautifulNumbers() {
        List<String> bases = new ArrayList<>();
        for (int i = 1; i <= 6; i++) {
            bases.add(String.valueOf(i).repeat(i));
        }
        Set<Integer> beautifulNumbers = new HashSet<>();
        int limit = 10_000_000;

        for (int size = 1; size <= bases.size(); size++) {
            for (List<String> combo : combinations(bases, size)) {
                String combined = String.join("", combo);
                
                // Early skip if combined string is too long
                if (combined.length() > 7) {
                    continue;
                }
                
                // Generate all permutations
                for (String perm : permutations(combined)) {
                    int num = Integer.parseInt(perm);
                    if (num < limit) {
                        beautifulNumbers.add(num);
                    }
                }
            }
        }
        
        List<Integer> result = new ArrayList<>(beautifulNumbers);
        for (String base : bases) {
            result.add(Integer.valueOf(base));
        }
        Collections.sort(result);
        return result;
    }

    private static <T> List<List<T>> combinations(List<T> list, int k) {
        List<List<T>> result = new ArrayList<>();
        combinationsHelper(list, k, 0, new ArrayList<>(), result);
        return result;
    }
    
    private static <T> void combinationsHelper(List<T> list, int k, int start, 
                                                List<T> current, List<List<T>> result) {
        if (current.size() == k) {
            result.add(new ArrayList<>(current));
            return;
        }
        
        for (int i = start; i < list.size(); i++) {
            current.add(list.get(i));
            combinationsHelper(list, k, i + 1, current, result);
            current.remove(current.size() - 1);
        }
    }
    
    // Generate all permutations of a string
    private static Set<String> permutations(String str) {
        Set<String> result = new HashSet<>();
        permutationsHelper(str.toCharArray(), 0, result);
        return result;
    }
    
    private static void permutationsHelper(char[] chars, int index, Set<String> result) {
        if (index == chars.length - 1) {
            result.add(new String(chars));
            return;
        }
        
        for (int i = index; i < chars.length; i++) {
            swap(chars, i, index);
            permutationsHelper(chars, index + 1, result);
            swap(chars, i, index); // backtrack
        }
    }
    
    private static void swap(char[] chars, int i, int j) {
        char temp = chars[i];
        chars[i] = chars[j];
        chars[j] = temp;
    }

    public static void main(String[] args) {
        NextGreaterNumericallyBalancedNumber sol = new NextGreaterNumericallyBalancedNumber();
        System.out.println("Output: " + sol.nextBeautifulNumber(1) + ", expected: 22");
        System.out.println("Output: " + sol.nextBeautifulNumber(1000) + ", expected: 1333");
        System.out.println("Output: " + sol.nextBeautifulNumber(3000) + ", expected: 3133");
        System.out.println("Output: " + sol.nextBeautifulNumber(59866) + ", expected: 122333");
        System.out.println("Output: " + sol.nextBeautifulNumber(748601) + ", expected: 1224444");
    }
}
