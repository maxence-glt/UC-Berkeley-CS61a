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
def make_keeper(n):
    def num(cond):
        for x in range(1, n + 1):
            if cond(x):
                print(x)
    return num





# 1.1 (Self reference section)
def print_delayed(x):
    def delay_print(y): 
        print(x)
        return print_delayed(y)
    return delay_print





# 1.2
def print_n(n):
    def inner_print(x):
        if n <= 0:
            print("done")
        else:
            print(x)
        return print_n(n - 1)
    return inner_print