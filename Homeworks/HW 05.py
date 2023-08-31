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
        




# Q2: Preorder
# My first try which I feel like I cheated due to using isinstance, set, list const, and stuff
# that they obviously wouldn't want me using
def preorder(t):
    tot = []
    def helper(x):
        total = []
        if is_leaf(x):
            return label(x)
        else:
            for z in branches(x):
                total += [label(x), helper(z)]
            return total
    tot += helper(t)
    def order(x):
        if not isinstance(x, list):
            return [x]
        return [i for z in x for i in order(z)]
    tot = order(tot)
    return list(set(tot))





# Trial #2
def preorder(t):
    total = []
    if is_leaf(t):
        return [label(t)]
    else:
        total += [label(t)]
        for x in branches(t):
            total += preorder(x)
        return total


def tree(label, branches = []):
    for b in branches:
        assert is_tree(b), 'branches must be trees'
    return [label] + list(branches)
    
def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for b in branches(tree):
        if not is_tree(b):
            return False
    return True

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

# numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
# print(preorder(numbers))
# print(preorder(tree(2, [tree(4, [tree(6)])])))





# Q3: Store Digits
def store_digits(n):
    if not is_link(n):
        return link(n)
    else: 
        return link(n // (10 ** (len(str(n)) - 1)), store_digits(n % (10 ** (len(str(n)) - 1))))


# I don't have the linked list data structure so I can't really do this one





# Q4: Generate Paths
def generate_paths(t, value):
    total = []
    if label(t) == value:
        return [label(t)]
    if is_leaf(t): return []
    else:
        total += [label(t)]
        for x in branches(t):
            total += generate_paths(x, value)
        return total

t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
print(generate_paths(t1, 6))

#TODO Q4





# Q5: Is BST