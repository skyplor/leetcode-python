import java.util.*;

class CountNumberOfTrapezoidsII {
    // Rational number class to avoid floating-point precision issues
    static class Rational {
        long num, den;
        
        Rational(long num, long den) {
            if (den == 0) {
                this.num = 1;
                this.den = 0; // represents infinity
            } else {
                long g = gcd(Math.abs(num), Math.abs(den));
                this.num = num / g;
                this.den = den / g;
                // Normalize: keep denominator positive
                if (this.den < 0) {
                    this.num = -this.num;
                    this.den = -this.den;
                }
            }
        }
        
        private long gcd(long a, long b) {
            return b == 0 ? a : gcd(b, a % b);
        }
        
        @Override
        public boolean equals(Object o) {
            if (!(o instanceof Rational)) return false;
            Rational r = (Rational) o;
            return num == r.num && den == r.den;
        }
        
        @Override
        public int hashCode() {
            return Long.hashCode(num) * 31 + Long.hashCode(den);
        }
    }
    
    public int countTrapezoids(int[][] points) {
        int res = 0;
        Map<Rational, List<Rational>> slopeToIntercepts = new HashMap<>();
        Map<Long, List<Rational>> midToSlopes = new HashMap<>();

        for (int i = 0; i < points.length; i++) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = i + 1; j < points.length; j++) {
                int x2 = points[j][0], y2 = points[j][1];

                Rational slope = getSlope(x1, y1, x2, y2);
                Rational intercept = getIntercept(x1, y1, x2, y2);

                slopeToIntercepts.computeIfAbsent(slope, k -> new ArrayList<>()).add(intercept);

                long mid = (long)(x1 + x2) * 10000L + (y1 + y2);
                midToSlopes.computeIfAbsent(mid, k -> new ArrayList<>()).add(slope);
            }
        }

        // Count trapezoid candidates
        for (List<Rational> intercepts : slopeToIntercepts.values()) {
            if (intercepts.size() == 1) continue;

            Map<Rational, Integer> interceptCount = new HashMap<>();
            for (Rational intercept : intercepts) {
                interceptCount.put(intercept, interceptCount.getOrDefault(intercept, 0) + 1);
            }

            int totalSum = 0;
            for (int count : interceptCount.values()) {
                res += totalSum * count;
                totalSum += count;
            }
        }

        // Subtract parallelograms
        for (List<Rational> slopes : midToSlopes.values()) {
            if (slopes.size() == 1) continue;

            Map<Rational, Integer> slopeCount = new HashMap<>();
            for (Rational slope : slopes) {
                slopeCount.put(slope, slopeCount.getOrDefault(slope, 0) + 1);
            }

            int totalSum = 0;
            for (int count : slopeCount.values()) {
                res -= totalSum * count;
                totalSum += count;
            }
        }

        return res;
    }

    public Rational getSlope(int x1, int y1, int x2, int y2) {
        int dx = x1 - x2;
        int dy = y1 - y2;
        return new Rational(dy, dx);
    }

    public Rational getIntercept(int x1, int y1, int x2, int y2) {
        int dx = x1 - x2;
        int dy = y1 - y2;
        if (x1 == x2) {
            return new Rational(x1, 1);
        }
        // y-intercept: b = y1 - (dy/dx)*x1 = (y1*dx - dy*x1)/dx
        return new Rational((long)y1 * dx - (long)dy * x1, dx);
    }
  
    public static void main(String[] args) {
        CountNumberOfTrapezoidsII sol = new CountNumberOfTrapezoidsII();
        System.out.println("Output: " + sol.countTrapezoids(new int[][]{{-3,2},{3,0},{2,3},{3,2},{2,-3}}) + ", expected: 2");
        System.out.println("Output: " + sol.countTrapezoids(new int[][]{{0,0},{1,0},{0,1},{2,1}}) + ", expected: 1");
        System.out.println("Output: " + sol.countTrapezoids(new int[][]{{71,-89},{-75,-89},{-9,11},{-24,-89},{-51,-89},{-77,-89},{42,11}}) + ", expected: 10");
    }
}
