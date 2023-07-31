# HW03 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/hw/hw03/

# Q1: Num sevens
def num_sevens(x):
    if x == 0:
        return 0
    if x % 10 == 7:
        return num_sevens(x // 10) + 1
    else:
        return num_sevens(x // 10)
    
# Q2: Ping-pong
def pingpong(n):
    i = 1
    def helper(n, i, z):
        if n == z:
            return 0
        if (num_sevens(z) > 0) or (z % 7 == 0 and z != 0):
            return i * -1 + helper (n, i * -1, z + 1)
        else: 
            return i + helper(n, i, z + 1)
    def num_sevens(x):
        if x == 0:
            return 0
        if x % 10 == 7:
            return num_sevens(x // 10) + 1
        else:
            return num_sevens(x // 10)
    return helper(n, i, 0)

# Q3: Count change
def count_change(total):
    index = 1
    def helper(total, index):
        if index >= total:
            return 0
        if index == 1:
            return 1 + helper(total, index * 2)
        else:
            return (total // index) + helper(total, index * 2)
    return helper(total, index)


