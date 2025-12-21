class CheckIfAll1sAreAtLeastLengthKPlacesAway {
    public boolean kLengthApart(int[] nums, int k) {
        int prev = -k - 1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0){
                continue;
            }

            if (i - prev - 1 < k) {
                return false;
            }
            prev = i;
        }
        return true;
    }
  
    public static void main(String[] args) {
        CheckIfAll1sAreAtLeastLengthKPlacesAway sol = new CheckIfAll1sAreAtLeastLengthKPlacesAway();
        System.out.println("Output: " + sol.kLengthApart(new int[]{1, 0, 0, 0, 1, 0, 0, 1}, 2) + ", expected: True");
        System.out.println("Output: " + sol.kLengthApart(new int[]{1, 0, 0, 1, 0, 1}, 2) + ", expected: False");
    }
}
