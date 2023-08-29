# Guerilla 2 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/disc/guer02.pdf

# 1.1
# Lists and dictionaries are mutable since you don't change the memory addresses
# of the already existing data when changing items

# 1.2
# Tuples and Ints are immutable as you do change the memory address of specific data

# 1.3
# No, as dictionaries are mutable, and its assigning an int to a key which works
# Yes since lists are unhashable and you can't assign dictionary keys to hashable types

# 1.5.1
# Append: adds data including data type to another data type, because you're adding a single entry
# Extend: Adds elements of data to another data structure, including iterables
# Append and Extend return None, while + returns the result of adding two things
# +: Combines two data entries into one object

# 1.5.2
# b = [1, 6, [7, 4], 5]
# a = [1, 2, [7, 4], 5]
# a and b

# 2.1 
# Construction and Deconstruction

# 2.2 
# The abstraction barrier is broken in simplify, when instead of calling numer or denom, they select an element from a list
# This code would run into an error if f1[1] didn't have a value attached to it

# 2.3.1
# If we are selecting individual variables instead of calling objects or funcs, bypassing the constructors/deconstructors

# 2.3.2
# It helps keep code organized and modular, allowing us to ignore on lower level specificities and focus on similar level tasks





# 3.1
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





# 3.2
def is_mini_heap(tree):
    print(tree)
    for x in branches(tree):
        if (label(tree) > label(x)) or (not is_mini_heap(x)):
            return False
    return True
        
    
    


# 3.3
def largest_product_path(tree):
    if is_leaf(tree): return label(tree)
    return max(label(tree) * largest_product_path(x) for x in branches(tree))
    




# 3.4
def max_tree(t):
    if is_leaf(t):
        return tree(t)
    else:
        new_branches = max 


t = (tree(1, [tree(5, [tree(7)]),tree(3,[tree(9),tree(4)]),tree(6)]))





# 4.3
def make_max_finder():
    total = 0
    def max_total(list):
        nonlocal total
        new_total = max(list)
        if new_total > total:
            total = new_total
        return total
    return max_total





# 4.4.a
# 23

# 4.4.b
# x = 14 from the f(x) frame

# 4.4.c
# no as its nonlocal





# 5.1
# An iterable is a container that holds values in an order that can be iterated sequentially
# An iterator is an obj that keeps track of position in sequence
# A generator yields values when called
# Generator = yield, Iterator = iter()

# 5.2
# next(new_list) raises an error as it isn't an iterator

# iter(new_list)[1] errors as you can't subscript an iterator

# for i in range... errors as you can't assign a length to an iterator

# 5.3
# The second function is a generator





# 5.4
def generate_constant(x):
    while True:
        yield x





# 5.5
def black_hole(seq, trap):
    seq = iter(seq)
    for x in seq:
        if x == trap:
                while True:
                    yield trap
        else:
            yield x





# 5.7 
def gen_inf(list):
    for x in list:
        list.append(x)
        yield x





# 5.8
def filter(iterable, fn):
    for x in iterable:
        if fn(x):
            yield x





# 5.9
# You could iterate on command, "lazy" eval