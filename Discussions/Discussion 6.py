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
# def nonlocalist():




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

