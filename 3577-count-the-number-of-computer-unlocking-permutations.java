class CountTheNumberOfComputerUnlockingPermutations {
    public int countPermutations(int[] complexity) {
        int first = complexity[0];
        for (int i = 1; i < complexity.length; i++) {
            if (complexity[i] <= first) {
                return 0;
            }
        }
        long res = 1;
        for (int i = 1; i < complexity.length; i++) {
            res = (res * i) % (1_000_000_007);
        }
        return (int) res;
    }

    public static void main(String[] args) {
        CountTheNumberOfComputerUnlockingPermutations sol = new CountTheNumberOfComputerUnlockingPermutations();
        System.out.println("Output: " + sol.countPermutations(new int[] { 1, 2, 3 }) + ", expected: 2");
        System.out.println("Output: " + sol.countPermutations(new int[] { 3, 3, 3, 4, 4, 4 }) + ", expected: 0");
        System.out.println("Output: " + sol.countPermutations(new int[] { 38, 223, 100, 123, 406, 234, 256, 93, 222, 259, 233, 69, 139, 245, 45, 98, 214 }) + ", expected: 789741546");
    }
}
