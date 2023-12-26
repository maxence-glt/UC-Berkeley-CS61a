# Discussion 12 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/disc/disc12.pdf

# setup classes
from operator import add, mul

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

    # def __str__(self):
    #     string = '<'
    #     while self.rest is not Link.empty:
    #         string += str(self.first) + ' '
    #         self = self.rest
    #     return string + str(self.first) + '>'





# 1.1
def paths(x, y):
    if x == y:
        return [[x]]
    
    if x > y:
        return []
    
    else:
        a = [[x] + i for i in paths(x+1, y)]
        b = [[x] + i for i in paths(x*2, y)]
        return a + b





# 1.2
def merge(s1, s2):
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    elif s1[0] < s2[0]:
        return [s1[0]] + merge(s1[1:], s2)
    else:
        return [s2[0]] + merge(s1, s2[1:])

def mergesort(seq):
    l = len(seq)
    if l == 1:
        return seq

    if l == 2 and seq[0] > seq[1]:
        return [seq[1], seq[0]]
    
    if l == 2 and seq[1] > seq[0]:
        return [seq[0], seq[1]]

    else:
        return merge(mergesort(seq[:l//2]), mergesort(seq[l//2:]))





# 2.1
def long_paths_wrong(tree, n):
    print(tree, n)
    if tree.is_leaf() and n > 0:
        return []
    
    if tree.is_leaf() and n <= 0:
        return [tree.label]
    
    else:
        return [[tree.label] + long_paths(i, n-1) for i in tree.branches]
    
# couldnt solve it, had to look it up. answer below (which doesnt even work)

def long_paths(tree, n):
    paths = []
    if n <= 0 and tree.is_leaf():
        paths.append(tree.label)
    for b in tree.branches:
        for path in long_paths(b, n - 1):
            paths.append([tree.label, path])
    return paths

t = Tree(3, [Tree(4), Tree(4), Tree(5)])
left = Tree(1, [Tree(2), t])
mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
whole = Tree(0, [left, Tree(13), mid, right])

print(long_paths(whole, 2))





# 2.2
# def widest_level(t):
#     levels = []
#     x = [t]

#     while

#         levels = sum(, [])

#     return max(levels, key=len)



# t = Tree(3, [Tree(1, [Tree(1), Tree(5)]), Tree(4, [Tree(9, [Tree(2)])])])
# print(widest_level(t))





# 4.1
class Network:
    def __init__(self):
        self.friends = {}
    
    def add_friend(self, user1, user2):
        if user2 not in self.friends.get(user1, []):
            self.friends[user1] = self.friends.get(user1, []) + [user2]
        
        if user1 not in self.friends.get(user2, []):
            self.friends[user2] = self.friends.get(user2, []) + [user1]

    def degrees(self, user1, user2, n):
        if n == 1 and user2 in self.friends[user1]:
            return True
        
        elif n == 1 and user2 not in self.friends[user1]:
            return False

        for friend in self.friends[user1]:
            if self.degrees(friend, user2, n - 1):
                return True

        return False





# 5.1
def flip_two(lnk):
    print(lnk)
    if lnk.rest is Link.empty:
        return lnk
    
    else:
        lnk.first, lnk.rest = lnk.rest.first, Link(lnk.first, flip_two(lnk.rest.rest))
        return lnk





# 6.1
def repeated(f):
    g = lambda x: x
    while True:
        yield g
        def h(x, g=g):  # We capture the current `g` in the default argument
            return f(g(x))
        g = h     

# only way I could make this function work, thanks to JeremyJoe on the Python server for helping me out :P





# 6.3
def accumulate(iterable, f):
    it = iter(iterable)
    last = next(it)
    yield last
    for x in it:
        out = f(x, last)
        yield out
        last = out
