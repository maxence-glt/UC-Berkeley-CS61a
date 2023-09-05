# Lab 7 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/lab/lab07/

# Startup structures
class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)
    def is_leaf(self):
        return not self.branches
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)
    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
    




# Magic: The Lambda-ing
# Q2: Making Cards
class Card:
    cardtype = 'Staff'

    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def power(self, other_card):
        return (self.attack - (other_card.defense / 2))
    
    def __repr__(self):
        return '{}: {}, [{}, {}]'.format(self.name, self.cardtype, self.attack, self.defense)

    def copy(self):
        return Card(self.name, self.attack, self.defense)




# Q3: Making a Player
class Player:
    def __init__(self, deck, name):
        self.deck = deck
        self.name = name
        self.hand = [x for x in deck]

    def draw(self):
        assert not self.deck.is_empty(), 'Deck is empty!'

    def play(self, card_index):
        pass

# Cant get Deck class to work, import problems, etc





# Q4: Link to list
# Recursively
def link_to_list(link):
    total = []
    def helper(link):
        nonlocal total
        if link.rest == Link.empty:
            return [total.append(link.first)]
        else: 
            total.append(link.first)
            helper(link.rest)
        return total
    return helper(link)





# Q5: Cumulative mul
def cumulative_mul(t):
    if t.is_leaf(): return t.label
    for branch in t.branches:
        t.label = t.label * cumulative_mul(branch)
    return t.label





# Would do optional questions if the provided M:TL code worked