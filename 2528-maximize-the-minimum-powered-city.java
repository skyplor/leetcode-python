import java.util.*;

class MaximizeTheMinimumPoweredCity {
    int k, r;
    int[] stations;
    public long maxPower(int[] stations, int r, int k) {
        this.k = k;
        this.r = r;
        this.stations = stations;
        List<Long> powerAvailable = new ArrayList<>();
        int n = stations.length;
        long runningTotal = 0;

        for (int i = 0; i <= r; i++) {
            if (i < n) {
                runningTotal += stations[i];
            }
        }

        powerAvailable.add(runningTotal);

        for (int i = 1; i < n; i++) {
            if (i - r - 1 >= 0) {
                runningTotal -= stations[i - r - 1];
            }
            if (i + r < n) {
                runningTotal += stations[i + r];
            }
            powerAvailable.add(runningTotal);
        }

        long left = Collections.min(powerAvailable);
        long right = (long) k;
        for (int station : stations) {
            right += station;
        }
        return binarySearch(left, right, powerAvailable);
    }

    private long binarySearch(long left, long right, List<Long> powerAvailable) {
        long answer = 0;
        while (left <= right) {
            long mid = left + (right - left) / 2;
            if (isPossible(mid, powerAvailable)) {
                answer = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return answer;
    }

    private boolean isPossible(long target, List<Long> powerAvailable) {
        long x = k;
        int n = stations.length;
        long[] powerDiff = new long[n + 1];  // ✓ Use long array
        long currentAdd = 0;  // ✓ Use long
        
        for (int i = 0; i < n; i++) {
            currentAdd += powerDiff[i];
            long currentPower = powerAvailable.get(i) + currentAdd;  // ✓ Use long
    
            if (currentPower < target) {
                long need = target - currentPower;
                x -= need;
                if (x < 0) return false;
    
                int pos = Math.min(i + r, n - 1);
    
                int left = Math.max(0, pos - r);
                int right = Math.min(n - 1, pos + r);
                powerDiff[left] += need;
    
                if (right + 1 <= n) {
                    powerDiff[right + 1] -= need;
                }
    
                if (left <= i) {
                    currentAdd += need;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        MaximizeTheMinimumPoweredCity sol = new MaximizeTheMinimumPoweredCity();
        int[] stations;
        int r, k;
        stations = new int[] { 1, 2, 4, 5, 0 };
        r = 1;
        k = 2;
        System.out.println("Output: " + sol.maxPower(stations, r, k) + ", expected: 5");

        stations = new int[] { 4, 4, 4, 4 };
        r = 0;
        k = 3;
        System.out.println("Output: " + sol.maxPower(stations, r, k) + ", expected: 4");
    }
}
