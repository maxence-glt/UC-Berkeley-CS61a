# Discussion 2 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/disc/disc02.pdf

# 1.2
curry2 = lambda h: lambda x: lambda y: h(x, y)





# 1.5
def keep_ints(cond, n):
    for x in range(1, n + 1):
        if cond(x):
            print(x)





# 1.6