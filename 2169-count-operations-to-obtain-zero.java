class CountOperationsToObtainZero {
    public int countOperations(int num1, int num2) {
        int ops = 0;
        while (num1 != 0 && num2 != 0) {
            if (num1 >= num2) num1 -= num2;
            else num2 -= num1;
            ops++;
        }
        return ops;
    }
  
    public static void main(String[] args) {
        CountOperationsToObtainZero sol = new CountOperationsToObtainZero();
        System.out.println("Output: " + sol.countOperations(2, 3) + ", expected: 3");
        System.out.println("Output: " + sol.countOperations(10, 10) + ", expected: 1");
    }
}
