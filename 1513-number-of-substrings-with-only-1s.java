import java.util.*;
import java.util.Map.*;

class NumberOfSubstringsWithOnly1s {
    public int numSub(String s) {
        Map<Long, Long> oneGroupings = new HashMap<>();
        long onesCount = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '0') {
                oneGroupings.put(onesCount, oneGroupings.getOrDefault(onesCount, 0L) + 1);
                onesCount = 0;
                continue;
            }
            onesCount++;
        }
        oneGroupings.put(onesCount, oneGroupings.getOrDefault(onesCount, 0L) + 1);

        int res = 0;
        for (Entry<Long, Long> entry : oneGroupings.entrySet()) {
            long subgroup = entry.getKey(), count = entry.getValue();
            long temp = (long) ((count * (((subgroup) * (subgroup + 1)) / 2)) % (Math.pow(10, 9) + 7)) ;
            res += (int) temp;
            res %= Math.pow(10, 9) + 7;
        }

        return res;
    }
  
    public static void main(String[] args) {

    }
}
