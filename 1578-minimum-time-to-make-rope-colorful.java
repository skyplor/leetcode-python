class MinimumTimeToMakeRopeColorful {
    public int minCost(String colors, int[] neededTime) {
        if (colors.length() == 1) {
            return 0;
        }

        int result = 0, prevIdx = 0;

        for (int i = 1; i < colors.length(); i++) {
            if (colors.charAt(prevIdx) == colors.charAt(i)) {
                if (neededTime[i] < neededTime[prevIdx]) {
                    result += neededTime[i];
                } else {
                    result += neededTime[prevIdx];
                    prevIdx = i;
                }
            } else {
                prevIdx = i;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        MinimumTimeToMakeRopeColorful sol = new MinimumTimeToMakeRopeColorful();
        String colors;
        int[] neededTime;

        colors = "abaac";
        neededTime = new int[] { 1, 2, 3, 4, 5 };
        System.out.println("Output: " + sol.minCost(colors, neededTime) + ", expected: 3");
        colors = "abc";
        neededTime = new int[] { 1, 2, 3 };
        System.out.println("Output: " + sol.minCost(colors, neededTime) + ", expected: 0");
        colors = "aabaa";
        neededTime = new int[] { 1, 2, 3, 4, 1 };
        System.out.println("Output: " + sol.minCost(colors, neededTime) + ", expected: 2");
        colors = "aaabbbabbbb";
        neededTime = new int[] { 3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1 };
        System.out.println("Output: " + sol.minCost(colors, neededTime) + ", expected: 26");
    }
}
