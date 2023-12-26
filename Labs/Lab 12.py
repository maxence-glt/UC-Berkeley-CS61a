# Lab 12 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/lab/lab12/

# setup classes

from operator import *

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





# Q1: Prune Min
# Really messy first go at it
def prune_min_original(t1):
    def helper(t):
        print(t[0].is_leaf())

        if t[0].label > t[1].label:
            if t[1].is_leaf():
                return Tree(t[1].label)
            return Tree(t[1].label, [helper(t[1].branches)])

        else:
            if t[0].is_leaf():
                return Tree(t[0].label)
            return Tree(t[0].label, [helper(t[0].branches)])
    
    if t1.is_leaf():
        return t1

    else:
        t1.branches = [helper(t1.branches)]

    return t1

# I then learnt about the .remove() python func
def prune_min(t):
    if not t.is_leaf():
        left = t.branches[0]
        right = t.branches[1]
        if left.label > right.label:
            t.branches.remove(left)
            prune_min(right)
        else:
            t.branches.remove(right)
            prune_min(left)





# Q2: Remainder Generator
def remainders_generator(m):
    index = -1
    total = m
    while total != 0:
        def gen():
            i = 1
            while True:
                i += 1
                if (i - 1) % m == index:
                    yield i - 1
        index += 1
        yield gen()





# Q3: Fold Right
def foldr(link, fn, z):
    if link.rest is Link.empty:
        return fn(link.first, z)
    return fn(link.first, foldr(link.rest, fn, z))
    

    


# Q4: Map With Fold
def mapl(lst, fn):
    if lst.rest is Link.empty:
        return Link(fn(lst.first))
    return Link(fn(lst.first), mapl(lst.rest, fn))





# OPTIONAL QUESTIONS I WILL DO WHEN I GET FREE TIME
#TODO
