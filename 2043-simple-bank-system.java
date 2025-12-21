class SimpleBankSystem {
    long[] balance;

    public SimpleBankSystem(long[] balance) {
        this.balance = balance;
    }

    public boolean transfer(int account1, int account2, long money) {
        if (!isValid(account1) || !isValid(account2)) {
            return false;
        }
        if ((balance[account1 - 1] - money) >= 0) {
            balance[account1 - 1] -= money;
            balance[account2 - 1] += money;
            return true;
        }
        return false;
    }

    public boolean deposit(int account, long money) {
        if (!isValid(account)) {
            return false;
        }
        balance[account - 1] += money;
        return true;
    }

    public boolean withdraw(int account, long money) {
        if (!isValid(account)) {
            return false;
        }
        if (balance[account - 1] - money < 0) {
            return false;
        }
        balance[account - 1] -= money;
        return true;
    }

    private boolean isValid(int account) {
        return account > 0 && account <= balance.length;
    }

    public static void main(String[] args) {
        SimpleBankSystem bank = new SimpleBankSystem(new long[] { 10, 100, 20, 50, 30 });
        System.out.println(bank.withdraw(3, 10) + ", expected: true");
        System.out.println(bank.transfer(5, 1, 20) + ", expected: true");
        System.out.println(bank.deposit(5, 20) + ", expected: true");
        System.out.println(bank.transfer(3, 4, 15) + ", expected: false");
        System.out.println(bank.withdraw(10, 50) + ", expected: false");
    }
}
