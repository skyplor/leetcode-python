class OneBitAndTwoBitCharacters {
    public boolean isOneBitCharacter(int[] bits) {
        int i = 0;
        while (i < bits.length - 1) {
            if (bits[i] == 0) {
                i++;
                continue;
            }
            i += 2;
        }
        return i == bits.length - 1;
    }

    public static void main(String[] args) {
        OneBitAndTwoBitCharacters sol = new OneBitAndTwoBitCharacters();
        System.out.println("Output: " + sol.isOneBitCharacter(new int[] { 1, 0, 0 }) + ", expected: true");
        System.out.println("Output: " + sol.isOneBitCharacter(new int[] { 1, 1, 1, 0 }) + ", expected: false");
    }
}
