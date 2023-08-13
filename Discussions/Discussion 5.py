# Discussion 5 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/disc/disc05.pdf

# 1.1
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)





def height(t):
    if is_leaf(t):
        return 0
    else:
        return 1 + height(branches(t))





# 1.2
def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)





def square_trees(t):
    sq_branches = [square_trees(x) for x in branches(t)]
    return tree(t[0] ** 2 , sq_branches)
    




numbers = tree(1, [tree(2, [tree(3),tree(4)]),tree(5,[tree(6,[tree(7)]),tree(8)])])   
numbers = [1, [2, [3], [4]], [5, [6, [7]], [8]]]





# 1.3
def find_path(tree, x):
    if label(tree) == x:
        return [label(tree)]
    path = [find_path(b, x) for b in branches(t)]
        
# Kinda lost on this one
    



t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])





#2.2
def add_this_many(x, el, lst):
    [lst.append(el) for y in lst[::-1] if y == x]





# 2.3
def group_by(s, fn):
    dict, placeholder = {}, []
    for x in range(0, ((fn(max(s) + 1)) + 1)):
        placeholder = []
        for y in s:
            if fn(y) == x:
                placeholder.append(y)
        if placeholder != []:
            dict[x] = placeholder
    return dict





# 1(a)
def partition_options(total, biggest):
    if total == biggest:
        return [biggest]
# stuck on this one as well, I hate how I'm forced to use their code format :(





def min_elements(T, lst):
    if T == 0:
        return 0
    return min([1 + min_elements(T - i, lst) for i in lst if T - i >= 0])