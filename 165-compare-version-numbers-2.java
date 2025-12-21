class CompareVersionNumbers2Solution {
    public int compareVersion(String version1, String version2) {
        /**
         * We can use 2 pointers to loop through each character of each version.
         *  - While we haven't reach the next dot,
         *      - we try to get the integer value by getting the character, casting it to int, incrementing pointer
         */

        int p1 = 0, p2 = 0;
        int n1 = version1.length(), n2 = version2.length();
        while (p1 < n1 || p2 < n2) {
            int cur_val_1 = 0, cur_val_2 = 0;
            while (p1 < n1 && version1.charAt(p1) != '.') {
                cur_val_1 = cur_val_1 * 10 + Integer.parseInt(String.valueOf(version1.charAt(p1)));
                p1++;
            }
            while (p2 < n2 && version2.charAt(p2) != '.') {
                cur_val_2 = cur_val_2 * 10 + Integer.parseInt(String.valueOf(version2.charAt(p2)));
                p2++;
            }

            if (cur_val_1 == cur_val_2) {
                p1++;
                p2++;
                continue;
            }

            if (cur_val_1 < cur_val_2) {
                return -1;
            }
            return 1;

        }

        return 0;
    }

    public static void main(String[] args) {
        CompareVersionNumbers2Solution sol = new CompareVersionNumbers2Solution();
        String version1 = "1.2";
        String version2 = "1.10";
        System.out.println("output: " + sol.compareVersion(version1, version2) + ", expected: -1");
        version1 = "1.01";
        version2 = "1.001";
        System.out.println("output: " + sol.compareVersion(version1, version2) + ", expected: 0");
        version1 = "1.0";
        version2 = "1.0.0.0";
        System.out.println("output: " + sol.compareVersion(version1, version2) + ", expected: 0");
    }
}
