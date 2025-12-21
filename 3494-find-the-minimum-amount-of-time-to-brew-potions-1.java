class FindMinimumTimeBrewPotionsSolution {

    public long minTime(int[] skill, int[] mana) {
        int n = skill.length, m = mana.length;
        long[] endTime = new long[n];
        for (int i = 0; i < n; i++) {
            endTime[i] += skill[i] * mana[0];
            if (i > 0) {
                endTime[i] += endTime[i - 1];
            }
        }
        for (int j = 1; j < m; j++) {
            endTime[n - 1] = endTime[n - 1] + (skill[n - 1] * mana[j]);
            for (int k = n - 2; k >= 0; k--) {
                long tempEndTime = endTime[k + 1] - (skill[k + 1] * mana[j]);
                long tempStartTime = tempEndTime - (skill[k] * mana[j]);
                if (tempStartTime > endTime[k]) {
                    endTime[k] = tempEndTime;
                } else {
                    endTime[k] += skill[k] * mana[j];
                }
            }

            for (int l = 1; l < n; l++) {
                endTime[l] = endTime[l - 1] + (skill[l] * mana[j]);
            }
        }

        return endTime[n - 1];
    }

    public static void main(String[] args) {
        FindMinimumTimeBrewPotionsSolution sol = new FindMinimumTimeBrewPotionsSolution();
        System.out.println(
                "Output:  " + sol.minTime(new int[] { 1, 5, 2, 4 }, new int[] { 5, 1, 4, 2 }) + ", expected: 110");
    }
}