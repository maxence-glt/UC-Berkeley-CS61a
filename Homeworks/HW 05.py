# HW05 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/hw/hw05/

# Q1: Vending Machine
class VendingMachine:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.items = 0
        self.balance = 0
    def add_funds(self, amount):
        if self.items == 0:
            return f'Machine is out of stock. Here is your ${amount}.'
        else:
            self.balance += amount
        return f"Current Balance: ${self.balance}"
    def restock(self, x):
        self.items += x
        return f'Current {self.name} stock: {self.items}'
    def vend(self):
        if self.items == 0: return "Machine is out of stock."
        if self.balance < self.cost: return f'You must add ${self.cost - self.balance} more funds.'
        else:
            self.items -= 1
            self.change = self.balance - self.cost
            self.balance = 0
            if self.balance == 0:
                return f"Here is your {self.name}."
            return f"Here is your {self.name} and ${self.change} change."