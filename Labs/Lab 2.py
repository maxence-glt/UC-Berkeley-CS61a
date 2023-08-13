# Lab 2 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/lab/lab02/

# Q3: Lambdas and Currying
def lambda_curry2(func):
    return lambda x: lambda y: func(x, y)





# Q4: Count van Count
def count_cond(condition):
    def count_cond2(i):
        sum = 0
        for x in range(1, i + 1):
            if condition(i, x):
                sum += 1
        return sum
    return count_cond2





# Q5: Both Paths
def both_paths(sofar="S"):
    print(sofar)
    def left():
        print(sofar)
        return both_paths(sofar="L")
    def right():
        print(sofar)
        return both_paths(sofar="R") 
    return left, right





# Q8: Composite Identity Function
def composite_identity(f, g):
    def compose(x):
        if (f(g(x)))  == (g(f(x))):
            return True
        else:
            return False
    return compose





# Q9: I Heard You Liked Functions...
def cycle(f1, f2, f3):
    def my_cycle(i):
        def identity(b):
            total, num = 1, 1
            for a in range(0, i + 1):
                if a == 0:
                    total = total * b
                else:
                    if num == 1:
                        total = f1(total)
                        num += 1
                    elif num == 2:
                        total = f2(total)
                        num += 1
                    elif num == 3:
                        total = f3(total)
                        num = 1
            return total
        return identity
    return my_cycle

# This lab gave me a migraine right after... lol