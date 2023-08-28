# Discussion 6 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/disc/disc06.pdf

# 1.2 
def memory(n):
    num = n
    def helper(x):
        nonlocal num
        num = x(num)
        return num
    return helper

f = memory(10)





# 1.3
def nonlocalist():
    get = lambda x: "Index out of range!"
    def prepend(value):
        nonlocal get
        f = get
        def get(i):
            if i == 0:
                return value
            return f(i - 1)
    return prepend, lambda x: get(x)


# prepend, get = nonlocalist()

# prepend(2)

# prepend(3)

# prepend(4)

# print(get(0))

# print(get(1))

# print(get(2))

# prepend(8)

# print(get(2))





# 2.1
def merge(a, b):
    while True:
        x, y = next(a), next(b)
        if x == y:
            yield x
            x, y = next(a), next(b)
        else:
            yield max(x, y)
            yield min(x, y)
            x, y = next(a), next(b)




def sequence(start, step):
    while True:
        yield start
        start += step

a = sequence(2, 3)

b = sequence(3, 2)

result = merge(a, b) 

print([next(result) for _ in range(10)])





# 2.2
def generate_subsets():
    x = [[]]
    n = 1
    while True:
        yield x
        x = x + [s + [n] for s in x]
        n += 1





# 2.3
def sum_paths_gen(t):
    if is_leaf(t):
        yield label(t)
    for x in branches(t):
        for y in sum_paths_gen(x):
            yield y + label(t)





# 1. Trie Recursion
def collect_words(t):
    if is_leaf(t):
        return label(t)
    words = []
    for x in branches(t):
        words += [label(t) + y for y in collect_words(x)]
    return words

def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)

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
