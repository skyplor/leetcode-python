class CompareVersionNumbersSolution {
    public int compareVersion(String version1, String version2) {
        /**
         * Since each contain only digits, we can split by the dots, get the one with
         * the longer length and loop through the elements.
         * In each iteration, we compare both splitted array by casting the string as
         * integer value
         */

        String[] v1_elements = version1.split("\\.");
        String[] v2_elements = version2.split("\\.");
        int n1 = v1_elements.length, n2 = v2_elements.length;
        for (int i = 0; i < Math.max(n1, n2); i++) {
            int e1 = 0, e2 = 0;
            if (i < n1) {
                e1 = Integer.parseInt(v1_elements[i]);
            }
            if (i < n2) {
                e2 = Integer.parseInt(v2_elements[i]);
            }
            if (e1 < e2) {
                return -1;
            }
            if (e1 > e2) {
                return 1;
            }
        }

        return 0;
    }

    public static void main(String[] args) {
        CompareVersionNumbersSolution sol = new CompareVersionNumbersSolution();
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
