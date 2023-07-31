# HW02 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/hw/hw02/

from operator import add, mul, sub

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1

# Q1: Product
def product(n, f):
    sum = 1
    for x in range(1, n + 1):
        sum = sum * f(x)
    return sum





# Q2: Accumulate
def accumulate(combiner, base, n, f):
    total, k = base, 1
    while k <= n:
        total, k = combiner(total, f(k)), k + 1
    return total





def summation_using_accumulate(n, f):
    sum = 0
    for x in range(1, n + 1):
        sum = sum + f(x)
    return sum





def product_using_accumulate(n, f):
    mul = 1
    for x in range(1, n + 1):
        mul = mul * f(x)
    return mul


# Q3: Make Repeater
def make_repeater(h, n):
    def make_repeater2(b):
        total = b
        for x in range(1, n + 1):
            total = h(total)
        return total
    return make_repeater2