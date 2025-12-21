class WaterBottlesSolution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int res = numBottles;
        while (numBottles >= numExchange) {
            int exchangedBottles = numBottles / numExchange;
            res += exchangedBottles;
            numBottles = exchangedBottles + (numBottles % numExchange);
        }

        return res;
    }

    public static void main(String[] args) {
        WaterBottlesSolution sol = new WaterBottlesSolution();
        System.out.println("Output: " + sol.numWaterBottles(9, 3) + ", expected: 13");
        System.out.println("Output: " + sol.numWaterBottles(15, 4) + ", expected: 19");
    }
}