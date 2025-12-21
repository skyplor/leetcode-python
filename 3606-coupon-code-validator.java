import java.util.*;

class CouponCodeValidator {
    public List<String> validateCoupons(String[] code, String[] businessLine, boolean[] isActive) {

        List<String> electronics = new ArrayList<>();
        List<String> grocery = new ArrayList<>();
        List<String> pharmacy = new ArrayList<>();
        List<String> restaurant = new ArrayList<>();

        for (int i = 0; i < code.length; i++) {
            String c = code[i];
            if (c.isBlank() || !c.matches("[A-Za-z0-9_]+") || !isActive[i]) {
                continue;
            }
            String business = businessLine[i];
            switch (business) {
                case "electronics":
                    electronics.add(c);
                    break;
                case "grocery":
                    grocery.add(c);
                    break;
                case "pharmacy":
                    pharmacy.add(c);
                    break;
                case "restaurant":
                    restaurant.add(c);
                    break;
                default:
                    break;
            }
        }
        Comparator<String> comparator = new Comparator<>() {
            @Override
            public int compare(String o1, String o2) {
                return o1.compareTo(o2);
            }
            
        };
        List<String> res = new ArrayList<>();
        electronics.sort(comparator);
        grocery.sort(comparator);
        pharmacy.sort(comparator);
        restaurant.sort(comparator);
        res.addAll(electronics);
        res.addAll(grocery);
        res.addAll(pharmacy);
        res.addAll(restaurant);
        return res;
    }

    public static void main(String[] args) {
        CouponCodeValidator sol = new CouponCodeValidator();
        System.out.println("Output: " + sol.validateCoupons(new String[] { "SAVE20", "", "PHARMA5", "SAVE@20" },
                new String[] { "restaurant", "grocery", "pharmacy", "restaurant" },
                new boolean[] { true, true, true, true }).toString() + ", expected: ['PHARMA5','SAVE20']");
        System.out.println("Output: "
                + sol.validateCoupons(new String[] { "GROCERY15", "ELECTRONICS_50", "DISCOUNT10" },
                        new String[] { "grocery", "electronics", "invalid" }, new boolean[] { false, true, true })
                + ", expected: ['ELECTRONICS_50']");
    }
}
