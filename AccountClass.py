import numpy as np

class BankAccount:
    def __init__(self, bal = 0, name = "None"):
        self.bal = bal
        self.name = name
    def show(self):
        print(f'name: {self.name}, balance: {self.bal}')

ba = BankAccount(1000, "k2")

ba.show()

ba.bal = 2000

ba.show()