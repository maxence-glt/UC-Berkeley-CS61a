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
