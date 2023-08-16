# Lab 1 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/lab/lab01/

# Q1: Make Adder Increasing
def make_adder_inc(n):
    inc = -1
    def one_argument_function(x):
        nonlocal inc
        inc += 1
        return n + x + inc
    return one_argument_function

adder1 = make_adder_inc(5)

adder2 = make_adder_inc(6)

print(adder1(2))

print(adder1(2)) # 5 + 2 + 1

print(adder1(10)) # 5 + 10 + 2

print([adder1(x) for x in [1, 2, 3]])

print(adder2(5))