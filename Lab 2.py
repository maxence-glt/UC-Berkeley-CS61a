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
    print(sofar),
    def left():
        print("L")
    def right():
        print("R")   
    return left, right      #  Stuck on this one