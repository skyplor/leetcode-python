from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.is_valid(account1) or not self.is_valid(account2):
            return False
        account1 -= 1
        account2 -= 1

        account1_after = self.balance[account1] - money
        if account1_after >= 0:
            self.balance[account1] = account1_after
            self.balance[account2] += money
            return True

        return False

    def deposit(self, account: int, money: int) -> bool:
        if not self.is_valid(account):
            return False
        account -= 1

        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.is_valid(account):
            return False
        account -= 1

        if self.balance[account] - money < 0:
            return False

        self.balance[account] -= money
        return True

    def is_valid(self, account: int) -> bool:
        return account > 0 and account <= len(self.balance)


obj = Bank([10, 100, 20, 50, 30])
print(f'{obj.withdraw(3, 10)}, expected: True')
print(f'{obj.transfer(5, 1, 20)}, expected: True')
print(f'{obj.deposit(5, 20)}, expected: True')
print(f'{obj.transfer(3, 4, 15)}, expected: False')
print(f'{obj.withdraw(10, 50)}, expected: False')
