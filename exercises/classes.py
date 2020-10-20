"""Class exercises"""


class BankAccount:
    """Bank account including an account balance."""
    def __init__(self, balance=0):
        self._balance = balance
        self.transactions = [('OPEN', self._balance, self._balance)]
        
    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if (amount > 0):
            self._balance += amount
            self.transactions.append(('DEPOSIT', amount, self._balance))
        else:
            print("deposited amount should be positive")
    def withdraw(self, amount):
        if (self._balance >= amount):
            self._balance -= amount
            self.transactions.append(('WITHDRAWAL', amount, self._balance))
        else:
            print("not enough funds to withdraw")
            return 1
    def transfer(self, otherAccount, amount):
        if self.withdraw(amount) != 1:
            otherAccount.deposit(amount)
    def __str__(self):
        return "balance={}".format(self._balance)
    def __repr__(self):
        return "{}(balance={})".format(type(self).__name__, self._balance)


class SuperMap:
    """Data structure for quickly finding objects based on their attributes."""
    def __init__(self, obj_list, indexes):
        self.obj_list = obj_list
        self.indexes = indexes
    def where(self, attr, val):
        result = set()
        if attr not in self.indexes:
            return result
        for obj in self.obj_list:
            if getattr(obj, attr) == val:
                result.add(obj)
        return result

import heapq
class MinHeap:
    """Heap-like data structure."""
    def __init__(self, iterable):
        self.iterable = iterable
        heapq.heapify(self.iterable)
    def pop(self):
        return heapq.heappop(self.iterable)
        
    def push(self, item):
        return heappush(self.heap, item)

    def peek(self):
        return self.iterable[0]


class Flavor:
    """Flavor of ice cream."""


class Size:
    """Ice cream size."""


class IceCream:
    """Ice cream to be ordered in our ice cream shop."""

from datetime import date
class Month:
    """Class representing an entire month."""
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __str__(self):
        return f"{self.year}-{self.month if self.month>9 else '0'+str(self.month)}"

    def __repr__(self):
        return f"{type(self).__name__}(year={self.year}, month={self.month})"

    def first(self):
        return date(self.year, self.month, 1)


class MonthDelta:
    """Class representing the difference between months."""


class Row:
    """Row class that stores all given arguments as attributes."""
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
