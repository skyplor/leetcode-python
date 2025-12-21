class TakingMaximumEnergyFromTheMysticDungeonSolution {

    public int maxEnergy(int[] energy, int k) {
        int n = energy.length;

        for (int i = k; i < n; i++) {
            if (energy[i] + energy[i - k] > energy[i]) {
                energy[i] = energy[i - k] + energy[i];
            }
        }

        int result = Integer.MIN_VALUE;
        for (int i = n - k; i < n; i++) {
            if (energy[i] > result) {
                result = energy[i];
            }
        }

        return result;
    }

    public static void main(String[] args) {
        TakingMaximumEnergyFromTheMysticDungeonSolution sol = new TakingMaximumEnergyFromTheMysticDungeonSolution();
        System.out.println("Output: " + sol.maxEnergy(new int[] { 5, 2, -10, -5, 1 }, 3) + ", expected: 3");
        System.out.println("Output: " + sol.maxEnergy(new int[] { -2, -3, -1 }, 2) + ", expected: -1");
        System.out.println("Output: " + sol.maxEnergy(new int[] { 8, -5 }, 1) + ", expected: 3");
    }

}
