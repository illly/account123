class Account:
    def __init__(self, balance: object) -> None:
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, param):
        self._balance -= param