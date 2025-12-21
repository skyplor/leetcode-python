class WaterBottlesIISolution {

    public int maxBottlesDrunk(int numBottles, int numExchange) {
        int bottlesDrunk = 0;
        int emptyBottles = 0;
        while (numBottles + emptyBottles >= numExchange) {
            bottlesDrunk += numBottles;
            emptyBottles += numBottles;
            numBottles = 0;
            while (emptyBottles >= numExchange) {
                emptyBottles -= numExchange;
                numExchange++;
                numBottles++;
            }
        }

        return bottlesDrunk + numBottles;
    }

    public static void main(String[] args) {
        WaterBottlesIISolution sol = new WaterBottlesIISolution();
        System.out.println("Output: " + sol.maxBottlesDrunk(13, 6) + ", expected: 15");
        System.out.println("Output: " + sol.maxBottlesDrunk(10, 3) + ", expected: 13");
    }
}