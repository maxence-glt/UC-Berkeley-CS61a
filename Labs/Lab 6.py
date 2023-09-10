# Lab 6 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/lab/lab06/

# Q1: Make Adder Increasing
def make_adder_inc(n):
    inc = -1
    def one_argument_function(x):
        nonlocal inc
        inc += 1
        return n + x + inc
    return one_argument_function





# Q2: Next Fibonacci
# Fib seq =  0, 1, 1, 2, 3, 5, 8, 13, 21, 34
def make_fib():
    a, b = 0, 1
    def next_fib():
        nonlocal a, b
        a, b = b, b + a
        return a
    return next_fib





# Q3: Scale
def scale(it, multiplier):
    i = 0
    while i < len(it):
        yield it[i] * 5
        i += 1





# Q4: Hailstone
def hailstone(n):
    while n != 1:
        yield n
        if ((n % 2) == 0):
            n = n // 2
        else:
            n = (n * 3) + 1
    yield n