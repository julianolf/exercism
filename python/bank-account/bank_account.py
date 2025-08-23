from enum import Enum
from threading import RLock


class BankAccount(object):
    AccountStatus = Enum('AccountStatus', {'CLOSED': 0, 'OPENED': 1})

    def __init__(self):
        self.tlock = RLock()
        self.open()
    
    def _check_account_status(self):
        if self.status == self.AccountStatus.CLOSED:
            raise ValueError('Closed account')

    def get_balance(self):
        self._check_account_status()
        return self.balance

    def open(self):
        self.balance = 0
        self.status = self.AccountStatus.OPENED

    def deposit(self, amount):
        with self.tlock:
            self._check_account_status()
            if amount < 0:
                raise ValueError('Negative amount is not accepted')
            self.balance += amount

    def withdraw(self, amount):
        with self.tlock:
            self._check_account_status()
            if amount < 0:
                raise ValueError('Negative amount is not accepted')
            if self.balance < amount:
                raise ValueError('Insufficient funds')
            self.balance -= amount

    def close(self):
        self.status = self.AccountStatus.CLOSED
