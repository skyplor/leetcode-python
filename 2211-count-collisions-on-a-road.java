class CountCollisionsOnARoad {
    public int countCollisions(String directions) {
        int startIndex = 0, endIndex = directions.length() - 1;
        while (startIndex < directions.length() && directions.charAt(startIndex) == 'L') {
            startIndex++;
        }
        while (endIndex >= startIndex && directions.charAt(endIndex) == 'R') {
            endIndex--;
        }
        int res = 0;
        for (int i = startIndex; i <= endIndex; i++) {
            if (directions.charAt(i) == 'S') {
                continue;
            }
            res++;
        }
        return res;
    }
  
    public static void main(String[] args) {
        CountCollisionsOnARoad sol = new CountCollisionsOnARoad();
        System.out.println("Output: " + sol.countCollisions("RLRSLL") + ", expected: 5");
        System.out.println("Output: " + sol.countCollisions("LLRR") + ", expected: 0");
        System.out.println("Output: " + sol.countCollisions("SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR") + ", expected: 20");
        System.out.println("Output: " + sol.countCollisions("L") + ", expected: 0");
        System.out.println("Output: " + sol.countCollisions("R") + ", expected: 0");
    }
}
